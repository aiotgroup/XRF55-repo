## Notes:

For time saving purpose, there are some actions which are not collected according to action class. 

RFID, WiFi, mmWave have already been rearranged. However, the Kinect files are not segmented (one .mkv video contains 20 action samples) and have not been rearranged (pairs of actions and reset actions).

Type 1: Actions that are collected in pairs (Throwing something & Picking, Drinking & Put Something on the Table, Standing Up & Sitting Down).
![pair](./hardware%20tutorial/assets/re_arrange_pair.png)

Type 2: Actions that need time to reset (Wearing Hat, Put on Clothing, Fall on the Floor).
![even](./hardware%20tutorial/assets/re_arrange_even.png)

So after taking the .mkv and extracting the RGB, Depth and IR images, you need to do the next two steps:

### 1.Split RGB, Depth and IR images

As mentioned in Notes, the Kinect .mkv video is not segmented and rearranged, and after getting the RGB, Depth, and IR images based on the first two steps, you need to execute [image_split.py](./hardware%20tutorial/Kinect/image_split.py) script to split the image, just modify the corresponding input and output file directories.

### 2.Rearrange RGB, Depth and IR images

After splitting all the data of one volunteer, there should be 58 * 20 = 1160 samples, after [image_rearrange.py](./hardware%20tutorial/Kinect/image_rearrange.py) script to rearrange the samples, you'll end up with 55 * 20 = 1100 samples as network input.

