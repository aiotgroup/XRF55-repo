# mmWave Tutorial

## Preparation

### Hardware
- IWR6843ISK, 5V/>2.5A power supply, micro USB cable (cables are part of the kit)
- DCA1000EVM, 5V/>2.5A power supply, micro USB cable, Ethernet cable (cables are part of the kit)  

### Software
- mmWave Studio 
- Matlab Runtime Engine v8.5.1
- mmwave studio sdk
- UniFlash  
- Matlab  

## Official Tutorial from TI Website
You can find all you need from tutorials or documents from TI Offical Website:  https://www.ti.com/

Tutorial:
https://www.ti.com/video/series/mmwave-training-series.html 

<ul>
    <li>Fundamentals of FMCW technology and mmWave sensors </li>
    <li> How to use DCA1000EVM and IWR6843ISK </li>
    <li >How to use the mmWave Studio to collect data </li>
</ul>


## Data Collection
#### Step 1: Prepare All Software and Hardware

#### Step 2: Parameter Configuration for mmWave Studio
In our project, we use set the parameters as follow: 
[param_configuration.lua](\resource\param_configuration.lua)

## Data Preprocessing
#### Interpret Raw ADC data captured from mmWave Studio
Offical Documentation:\
https://www.ti.com/lit/pdf/swra581?keyMatch=MMWAVE%20SENSOR%20RAW%20DATA%20CAPTURE%20USING%20THE%20DCA1000%20BOARD%20AND%20MMWAVE%20STUDIO

In our project: 
The mmWave data we provided in the link are the transformed version of Raw ADC data, and have already been segmented.

**Data Dimensions:** 
frame * tx * sample_num * rx_num * chirp_num

Code for interpreting raw data:
[readDCA1000_6843.m](\resource\readDCA1000_6843.m)
```
data = readDCA1000_6843(read_path, numADCSamples);
data = reshape(data,rx_num,sample_num,tx_num,chirp_num,data_framenum);
data = permute(data,[5,3,2,1,4]);    

... Here we omit the code for data segementation ...
```

