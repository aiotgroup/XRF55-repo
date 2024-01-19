import datetime
from time import sleep


import winsound

file = open(".\config.txt")
data = file.readlines()
collect_mode = data[2].split("\n")[0]
st = data[3].split("\n")[0]

print(collect_mode, st)

if collect_mode == "1":
    action_length = 5
    sound_loop_time = 10
    outer_loop_time = 2
else:
    action_length = 10
    sound_loop_time = 5
    outer_loop_time = 4

# Doesn't start executing until a certain point
target_time = datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S")

# Cue 10s in advance
prepare_to_start = True
print(target_time - datetime.timedelta(seconds=10))
while prepare_to_start:
    if datetime.datetime.now() > (target_time - datetime.timedelta(seconds=10)):
        winsound.Beep(3333, 200)
        winsound.Beep(3333, 200)
        prepare_to_start = False

dt = datetime.datetime.now()
while dt < target_time:
    dt = datetime.datetime.now()


time_list = []
tip_list = []
temp_time = target_time
for outer in range(outer_loop_time):
    for i in range(sound_loop_time):
        time_list.append(temp_time)
        temp_time = temp_time + datetime.timedelta(seconds=action_length)
        time_list.append(temp_time)
        temp_time = temp_time + datetime.timedelta(seconds=1)
    temp_time = temp_time + datetime.timedelta(seconds=9)

curr_i = 0
while curr_i < len(time_list):
    if datetime.datetime.now() > time_list[curr_i]:
        if curr_i % 2 == 1:
            winsound.Beep(2222, 200)
        else:
            winsound.Beep(1111, 200)
        curr_i = curr_i + 1
    # sleep(0.1)
winsound.Beep(800, 250)
winsound.Beep(800, 250)