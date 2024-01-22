import os
import datetime
import time

activity_order = [16, 17, 18, 20, 21, 22, 19, 2, 15, 26, 6, 9, 23, 31, 25, 29, 32, 30, 42, 43, 44, 34,
                  35, 38, 39, 41, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 4, 56, 37, 36, 14, 3, 10, 7,
                  12, 1, 13, 5, 27, 28, 33, 57, 8, 58, 24, 40, 11, 99]
with open('~\\params.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    vol_name = lines[0].replace('\n', '')
    act_name = lines[1].replace('\n', '')
    is_five = lines[2].replace('\n', '')
    time_ = lines[3].replace('\n', '')
    order = int(lines[4])

print(vol_name, act_name, is_five, time_, order)
if order < len(activity_order) - 1:

    # os.system('conda activate runRecordMmWave')
    # os.system(r"start python ~/soundbee.py")

    time.sleep(10)
    delay_time = datetime.timedelta(minutes=3)
    target_time = datetime.datetime.strptime(time_, "%Y-%m-%d %H:%M:%S.%f") + delay_time
    print('next time: ' + str(target_time))
    if int(activity_order[order + 1]) < 10:
        print('next id: ' + vol_name + '_' + '0' + str(activity_order[order + 1]))
    else:
        print('next id: ' + vol_name + '_' + str(activity_order[order + 1]))
    print('next order: ' + str(order + 1))

    with open('~\\params.txt', 'w', encoding='utf-8') as f:
        f.write(vol_name + '\n')
        if int(activity_order[order + 1]) < 10:
            f.write('0' + str(activity_order[order + 1]) + '\n')
        else:
            f.write(str(activity_order[order + 1]) + '\n')
        f.write(is_five + '\n')
        f.write(str(target_time) + ".000" + '\n')
        f.write(str(order + 1))

else:
    print('end')
