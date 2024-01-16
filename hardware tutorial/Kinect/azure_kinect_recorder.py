# --------------------------------------------------------------------------------------------------
# command：python .\azure_kinect_recorder.py --times={} --output={} --target_time={} --savepath={}
# --------------------------------------------------------------------------------------------------

# examples/python/reconstruction_system/sensors/azure_kinect_recorder.py

import argparse
import datetime
import open3d as o3d



class RecorderWithCallback:

    def __init__(self, config, device, filename, align_depth_to_color):
        # Global flags
        self.flag_exit = False
        self.flag_record = True
        self.filename = filename

        self.align_depth_to_color = align_depth_to_color
        self.recorder = o3d.io.AzureKinectRecorder(config, device)
        if not self.recorder.init_sensor():
            raise RuntimeError('Failed to connect to sensor')

    def escape_callback(self, vis):
        self.flag_exit = True
        if self.recorder.is_record_created():
            print('Recording finished.')
        else:
            print('Nothing has been recorded.')
        return False

    def space_callback(self, vis):
        if self.flag_record:
            print('Recording paused. '
                  'Press [Space] to continue. '
                  'Press [ESC] to save and exit.')
            self.flag_record = False

        elif not self.recorder.is_record_created():
            if self.recorder.open_record(self.filename):
                print('Recording started. '
                      'Press [SPACE] to pause. '
                      'Press [ESC] to save and exit.')
                self.flag_record = True

        else:
            print('Recording resumed, video may be discontinuous. '
                  'Press [SPACE] to pause. '
                  'Press [ESC] to save and exit.')
            self.flag_record = True

        return False

    def run(self):
        glfw_key_escape = 256
        glfw_key_space = 32
        vis = o3d.visualization.VisualizerWithKeyCallback()
        vis.register_key_callback(glfw_key_escape, self.escape_callback)
        vis.register_key_callback(glfw_key_space, self.space_callback)

        vis.create_window('recorder', 1920, 540)
        if self.recorder.open_record(self.filename):
            print('Recording started. '
                  'Press [SPACE] to pause. '
                  'Press [ESC] to save and exit.')
            self.flag_record = True

        vis_geometry_added = False
        with open(args.savepath + args.output + '.txt', 'w+') as file:
            while not self.flag_exit:
                rgbd = self.recorder.record_frame(self.flag_record,
                                                  self.align_depth_to_color)
                if rgbd is None:
                    continue

                if not vis_geometry_added:
                    vis.add_geometry(rgbd)
                    vis_geometry_added = True

                vis.update_geometry(rgbd)
                vis.poll_events()
                vis.update_renderer()

                t = datetime.datetime.now()
                file.write(str(t) + '\n')
                if(t>=over_time):
                    self.flag_exit = True

        self.recorder.close_record()
        file.close()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Azure kinect mkv recorder.')
    parser.add_argument('--config', type=str, help='input json kinect config')
    parser.add_argument('--output', type=str, help='output mkv filename')
    parser.add_argument('--list',
                        action='store_true',
                        help='list available azure kinect sensors')
    parser.add_argument('--device',
                        type=int,
                        default=0,
                        help='input kinect device id')
    parser.add_argument('-a',
                        '--align_depth_to_color',
                        action='store_true',
                        default=True,
                        help='enable align depth image to color')
    parser.add_argument('--times', type=int, help='收两次还是收四次', default=2)
    parser.add_argument('--savepath', type=str, help='要保存mkv的路径，包括时间戳 eg:./mkv_record/', default="F:/mkv_record/")
    parser.add_argument('--target_time', type=str, help='when time to start eg:2022-09-30 14:24:00', default='2022-09-30 14:24:00')
    args = parser.parse_args()

    if args.list:
        o3d.io.AzureKinectSensor.list_devices()
        exit()

    if args.config is not None:
        config = o3d.io.read_azure_kinect_sensor_config(args.config)
    else:
        config = o3d.io.AzureKinectSensorConfig()

    if args.output is not None:
        filename = args.savepath + args.output + '.mkv'
    else:
        filename = '{date:%Y-%m-%d-%H-%M-%S}.mkv'.format(
            date=datetime.datetime.now())
    print('Prepare writing to {}'.format(filename))

    device = args.device
    if device < 0 or device > 255:
        print('Unsupported device id, fall back to 0')
        device = 0
    tiqian_time = datetime.timedelta(seconds=-2)
    target_time = datetime.datetime.strptime(args.target_time, "%Y-%m-%d %H:%M:%S") + tiqian_time
    if args.times == 2:
        over_time = target_time + datetime.timedelta(seconds=128) - tiqian_time
    else:
        over_time = target_time + datetime.timedelta(seconds=246) - tiqian_time
        # over_time = target_time + datetime.timedelta(seconds=246) - tiqian_time
    # 当前日期时间
    print("Start time at:", target_time)
    print("Over time at:", over_time)
    dt = datetime.datetime.now()
    while(dt<target_time):
        dt = datetime.datetime.now()

    r = RecorderWithCallback(config, device, filename,
                             args.align_depth_to_color)
    r.run()
