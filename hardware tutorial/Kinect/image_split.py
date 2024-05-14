import os
from datetime import datetime
import shutil

def process_timestamp_file(file_path):
    timestamps = []
    with open(file_path, 'r') as f:
        for line in f:
            timestamps.append(datetime.strptime(line.strip(), '%Y-%m-%d %H:%M:%S.%f'))
    return timestamps


def find_start_time(timestamps):
    for idx, timestamp in enumerate(timestamps):
        if timestamp.second == 0:  # Found the start time
            return idx
    return None


def move_image(image_path, start_time, end_time, output_directory, file_name, i):
    output_rgb = os.path.join(output_directory, 'color', f"{file_name}_{i:02}")
    output_depth = os.path.join(output_directory, 'depth', f"{file_name}_{i:02}")
    output_ir = os.path.join(output_directory, 'ir', f"{file_name}_{i:02}")
    if not os.path.exists(output_rgb):
        os.makedirs(output_rgb)
        os.makedirs(output_depth)
        os.makedirs(output_ir)
    for index in range(start_time, end_time):
        if os.path.exists(os.path.join(image_path, 'color', str(index) + '.png')):
            shutil.copy2(os.path.join(image_path, 'color', str(index) + '.png'), os.path.join(output_rgb, str(index) + '.png'))
            shutil.copy2(os.path.join(image_path, 'depth', str(index) + '.png'), os.path.join(output_depth, str(index) + '.png'))
            shutil.copy2(os.path.join(image_path, 'ir', str(index) + '.png'), os.path.join(output_ir, str(index) + '.png'))
        else:
            continue


def split_video(image_path, start_time, output_directory, file_name):
    frame = 30
    for i in range(20):
        end_time = start_time + 5 * frame
        move_image(image_path, start_time, end_time, output_directory, file_name, i+1)
        if i != 9:
            start_time = end_time + 1 * frame
        else:
            start_time = end_time + 10 * frame


def main():
    image_path = 'F:/mkv_record/XX_XX/'  # The rgb, depth and ir directory generated in the previous step
    timestamp_file = 'F:/mkv_record/XX_XX.txt'  # mkv corresponding timestamp file
    output_directory = 'F:/mkv_output'  # Split image save directory
    timestamps = process_timestamp_file(timestamp_file)
    file_name = timestamp_file.split('\\')[-1].split('.')[0]
    start_time = find_start_time(timestamps)
    if start_time is None:
        print("Could not find a timestamp on the minute mark in your file.")
        return

    split_video(image_path, start_time, output_directory, file_name)


if __name__ == "__main__":
    main()
