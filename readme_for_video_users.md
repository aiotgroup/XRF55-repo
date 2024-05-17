When you have downloaded our XRF55 video dataset, you will get 19 × 58 .mkv videos and corresponding .txt timestamp files. The file naming format is **volunteer_index-action_index**.

> **19** is the number of volunteer data due to some volunteers not willing to disclose their videos.
> 
> (Index of available volunteers in Scene1: 03, 04, 05, 07, 08, 11, 19, 21, 22, 24; Scene2: 05, 24, 31; Scene3: 06, 07; Scene4: 03, 04, 13)
> 
> **58** is the number of action samples collected from each volunteer (XX-01~XX-58).

After you have checked the video data, if you need to extract the RGB, Depth and IR images from it, you need to execute the following two steps:

## Get RGB and Depth images from .mkv video

Make sure open3d is successfully installed before performing this step, and that `azure_kinect_viewer.py` can be executed correctly with the video displayed. Then execute [mkv2rgb_depth.py](./hardware%20tutorial/Kinect/mkv2rgb_depth.py) to generate the corresponding rgb and depth images.

## Get IR images from .mkv video

To extract IR images, we use a C++ project [mkv2ir.zip](.//hardware%20tutorial/Kinect/mkv2ir.zip). You can execute the main function of **transoform.cpp**. Simply change the paths to the read and save files.

## Notes:

For time saving purpose, there are some actions which are not collected according to action class. 

RFID, WiFi, mmWave have already been rearranged. However, the Kinect files are not segmented (one .mkv video contains 20 action samples) and have not been rearranged (pairs of actions and reset actions).

Type 1: Actions that are collected in pairs (Throwing something & Picking, Drinking & Put Something on the Table, Standing Up & Sitting Down).
![pair](./hardware%20tutorial/assets/re_arrange_pair.png)

Type 2: Actions that need time to reset (Wearing Hat, Put on Clothing, Fall on the Floor).
![even](./hardware%20tutorial/assets/re_arrange_even.png)

So after extracting the RGB, Depth and IR images from the .mkv, you need to do the next two steps:

### 1. Split RGB, Depth and IR images

As mentioned in Notes, the Kinect .mkv video is not segmented and rearranged, you need to execute [image_split.py](./hardware%20tutorial/Kinect/image_split.py) script to split the image, just modify the corresponding input and output file paths.

### 2. Rearrange RGB, Depth and IR images

After splitting all the data of one volunteer, there should be 58 * 20 = 1160 samples, after [image_rearrange.py](./hardware%20tutorial/Kinect/image_rearrange.py) script to rearrange the samples, you'll end up with 55 * 20 = 1100 samples.

