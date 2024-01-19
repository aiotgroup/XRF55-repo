import os
import datetime
import time

PATH_config = '.\config.txt'
PATH_RFID_exe = r"path\TagGesture\bin\Debug\TagGesture.exe"
PATH_save_video = r"F:/mkv_record/"


activity_order = [16, 17, 18, 20, 21, 22, 19, 2, 15, 26, 6, 9, 23, 31, 25, 29, 32, 30, 42, 43, 44, 34,
                  35, 38, 39, 41, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 4, 56, 37, 36, 14, 3, 10,
                  7, 12, 1, 13, 5, 27, 28, 33, 57, 8, 58, 24, 40, 11, 99]

with open(PATH_config, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    time_ = lines[3].replace('\n', '')
    people_id = lines[0].replace('\n', '')
    name = lines[0].replace('\n', '')+'_'+lines[1].replace('\n', '')
    is_5 = lines[2].replace('\n', '')
    order = int(lines[4])
    times = 2 if int(is_5) == 1 else 4
    print(times)

if order < len(activity_order)-1:

    os.system(r"start python .\azure_kinect_recorder.py --times={} --output={} --target_time={} --savepath={}"
              .format(f'"{times}"',f'"{name}"', f'"{time_}"',f'"{PATH_save_video}"'))
    os.system(r"start "+PATH_RFID_exe)
    os.system(r"start python .\soundbee.py")

    time.sleep(30)
    delay_time = datetime.timedelta(minutes=3)
    target_time = datetime.datetime.strptime(time_, "%Y-%m-%d %H:%M:%S") + delay_time

    print('next time: ' + str(target_time))
    if int(activity_order[order + 1]) < 10:
        print('next id: ' + people_id + '_' + '0' + str(activity_order[order+1]))
    else:
        print('next id: ' + people_id + '_' + str(activity_order[order + 1]))
    print('next order: ' + str(order+1))

    with open(PATH_config, 'w', encoding='utf-8') as f:
        f.write(people_id + '\n')
        if int(activity_order[order + 1]) < 10:
            f.write('0' + str(activity_order[order + 1]) + '\n')
        else:
            f.write(str(activity_order[order + 1]) + '\n')
        f.write(is_5 + '\n')
        f.write(str(target_time) + '\n')
        f.write(str(order+1))

else:
    print('end')
