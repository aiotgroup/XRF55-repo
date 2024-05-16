## 介绍视频文件如何收集的，成对收集

### 

## Split RGB, Depth and IR images

As mentioned in Notes, the Kinect .mkv video is not segmented and rearranged, and after getting the RGB, Depth, and IR images based on the first two steps, you need to execute [image_split.py](./hardware%20tutorial/Kinect/image_split.py) script to split the image, just modify the corresponding input and output file directories.

## Rearrange RGB, Depth and IR images

After splitting all the data of one volunteer, there should be 58 * 20 = 1160 samples, after [image_rearrange.py](./hardware%20tutorial/Kinect/image_rearrange.py) script to rearrange the samples, you'll end up with 55 * 20 = 1100 samples as network input.

## Notes:
For time saving purpose, there are some actions which are not collected according to action class. 

RFID, WiFi, mmWave have already been rearranged. However, the Kinect files are not segmented and have not been rearranged. Here are the tips.

Type 1: Actions that are collected in pairs.
![pair](./hardware%20tutorial/assets/re_arrange_pair.png)


Type 2: Actions that need time to reset.
![even](./hardware%20tutorial/assets/re_arrange_even.png)
