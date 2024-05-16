# Kinect Hardware Tutorial

## Hardware preparation

![Azure Kinect DK](https://learn.microsoft.com/zh-cn/azure/kinect-dk/media/index/device-image.jpg)

You can find Microsoft Azure Kinect purchase links, hardware parameters, and development tutorials at this link: https://learn.microsoft.com/en-us/azure/kinect-dk/

## Install Azure Kinect Sensor SDK

The Sensor SDK has the following features that work once installed and run on the Azure Kinect DK:

- Depth camera access and mode control (a passive IR mode, plus wide and narrow field-of-view depth modes)
- RGB camera access and control (for example, exposure and white balance)
- Motion sensor (gyroscope and accelerometer) access
- Synchronized Depth-RGB camera streaming with configurable delay between cameras
- External device synchronization control with configurable delay offset between devices
- Camera frame meta-data access for image resolution, timestamp, etc.
- Device calibration data access

To learn more about Azure Kinect Sensor SDK, see [Using Sensor SDK](https://learn.microsoft.com/en-us/azure/kinect-dk/about-sensor-sdk).

In our project, we use the SDK to get the RGB, Depth and IR information of the corresponding video.

## Get the original .mkv video

1. You can use the officially provided recording process, the main environment is C++. https://learn.microsoft.com/en-us/azure/kinect-dk/record-sensor-streams-file
2. We also recommend using the recording solution given by open3d, tutorial link: https://www.open3d.org/docs/release/tutorial/sensor/azure_kinect.html

We use the second method to record, in their project, `azure_kinect_mkv_reader.py` only records .mkv video; `azure_kinect_viewer.py` is only used for displaying; `azure_kinect_mkv_reader.py` not only saves .mkv video, but also saves rgb and depth images, but it's not recommended, as the processing time is too slow, far from the 30 fps requirement.

![image-20240116173431240](./assets/kinect_view.png)

## Get RGB and Depth images from .mkv video

Make sure open3d is successfully installed before performing this step, and that azure_kinect_viewer.py can be executed correctly with the video displayed, then you can generate the corresponding rgb and depth images by executing  [mkv2rgb_depth.py](./mkv2rgb_depth.py) 

## Get IR images from .mkv video

To extract IR images, we use a C++ project [mkv2ir.zip](./mkv2ir.zip). You can execute the main function of **transoform.cpp**. Simply change the paths to the read and save files.
