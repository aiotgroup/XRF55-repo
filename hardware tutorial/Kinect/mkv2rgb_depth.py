# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# command：python ./mkv2rgb_depth.py --input='mkv/path/x.mkv' --output="output/path"

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import argparse
import open3d as o3d
import os
import json
import sys

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(pwd, '..'))
from initialize_config import initialize_config


class ReaderWithCallback:

    def __init__(self, input, output):
        self.flag_exit = False
        self.flag_play = True
        self.input = input
        self.output = output
        self.pcd_list = []
        self.reader = o3d.io.AzureKinectMKVReader()
        self.reader.open(self.input)
        if not self.reader.is_opened():
            raise RuntimeError("Unable to open file {}".format(args.input))

    def escape_callback(self, vis):
        self.flag_exit = True
        return False

    def space_callback(self, vis):
        if self.flag_play:
            print('Playback paused, press [SPACE] to continue.')
        else:
            print('Playback resumed, press [SPACE] to pause.')
        self.flag_play = not self.flag_play
        return False

    def run(self):
        glfw_key_escape = 256
        glfw_key_space = 32

        # vis = o3d.visualization.VisualizerWithKeyCallback()
        # vis.create_window("Visualizer", 960, 540)

        vis = o3d.visualization.VisualizerWithKeyCallback()
        vis.register_key_callback(glfw_key_escape, self.escape_callback)
        vis.register_key_callback(glfw_key_space, self.space_callback)

        vis_geometry_added = False
        vis.create_window('reader', 1080, 720)

        print(
            "MKV reader initialized. Press [SPACE] to pause/start, [ESC] to exit."
        )

        if self.output is not None:
            abspath = os.path.abspath(self.output)
            metadata = self.reader.get_metadata()
            o3d.io.write_azure_kinect_mkv_metadata(
                '{}/intrinsic.json'.format(abspath), metadata)

            config = {
                'path_dataset': abspath,
                'path_intrinsic': '{}/intrinsic.json'.format(abspath)
            }
            initialize_config(config)
            with open('{}/config.json'.format(abspath), 'w') as f:
                json.dump(config, f, indent=4)

        idx = 1
        while not self.reader.is_eof() and not self.flag_exit:
            if self.flag_play:
                rgbd = self.reader.next_frame()
                if rgbd is None:
                    continue
                if not vis_geometry_added:
                    vis.add_geometry(rgbd)
                    vis_geometry_added = True
                if self.output is not None:
                    color_filename = '{0}/color/{1}.png'.format(
                        self.output, idx)
                    print('Writing to {}'.format(color_filename))
                    o3d.io.write_image(color_filename, rgbd.color)

                    depth_filename = '{0}/depth/{1}.png'.format(
                        self.output, idx)
                    print('Writing to {}'.format(depth_filename))
                    o3d.io.write_image(depth_filename, rgbd.depth)
                    # color_raw = o3d.io.read_image(color_filename)
                    # depth_raw = o3d.io.read_image(depth_filename)
                    # noinspection PyArgumentList
                    # PointCloud
                    # rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color=rgbd.color, depth=rgbd.depth, convert_rgb_to_intensity=False)
                    # # noinspection PyArgumentList
                    # point_cloud = o3d.geometry.PointCloud.create_from_rgbd_image(image=rgbd_image,
                    #                                                              intrinsic=o3d.camera.PinholeCameraIntrinsic(
                    #                                                                  o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault),
                    #                                                              extrinsic=np.array(
                    #                                                                  [[1., 0., 0., 0.], [0., 1., 0., 0.],
                    #                                                                   [0., 0., 1., 0.], [0., 0., 0., 1.]]))
                    # point_cloud.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
                    # point_cloud_filename = "{0}/pcd/{1}.pcd".format(self.output, idx)
                    # o3d.io.write_point_cloud(point_cloud_filename, point_cloud)
                    # print("Writing to {}".format(point_cloud_filename))

                    # self.pcd_list.append(point_cloud_filename)
                    # read_pcd = o3d.io.read_point_cloud(point_cloud)
                    idx += 1

                    # vis.update_geometry(point_cloud)
                    vis.update_geometry(rgbd)

            # except NameError:
            #     pass
            vis.poll_events()
            vis.update_renderer()

        self.reader.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Azure kinect mkv reader.')
    parser.add_argument('--input',
                        type=str,
                        required=True,
                        help='input mkv file')
    parser.add_argument('--output',
                        type=str,
                        help='output path to store color/ and depth/ and pcd/ images')
    args = parser.parse_args()

    if args.input is None:
        parser.print_help()
        exit()

    if args.output is None:
        print('No output path, only play mkv')
    elif os.path.isdir(args.output):
        print('Output path {} already existing, only play mkv'.format(
            args.output))
        # args.output = None
    else:
        try:
            os.mkdir(args.output)
            os.mkdir('{}/color'.format(args.output))
            os.mkdir('{}/depth'.format(args.output))
            # os.mkdir('{}/pcd'.format(args.output))
        except (PermissionError, FileExistsError):
            print('Unable to mkdir {}, only play mkv'.format(args.output))
            args.output = None

    reader = ReaderWithCallback(args.input, args.output)
    reader.run()
