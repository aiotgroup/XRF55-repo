# XRF55 Q&A

**We'll be updating this document with questions and answers!**

**If you have any questions outside of the documentation, please submit an issue or send us an email and we will respond promptly.**

------

#### Q1

**Wi-Fi data dimensions from 1000 × 1 × 3 × 3 × 30 to 1000 × 270, does data[:, 0:30] represent the 30 subcarriers of the received signal at the first antenna of the first Rx, with data[:, 30:60] being the second antenna of the first Rx, and so forth?**

Yes, the first 90 are all the subcarriers of the first receiving device, where the first 30 are the subcarriers of the first receiving antenna, and so on. [2024-4-5 23:03:33]

#### Q2

**Why does the wifi data of XRF55 have both dat and mat files?**

Some of wifi raw datas with prefixes 04, 07, 12 are saved in .mat format, which is normal, due to the difference in our pre-processing. 

**So are they the same csi data processed in two ways, or are they just different csi's?**

Same csi, you can use the load method in matlab to read them, and their contents are the same as the .dat files. [2024-7-9 17:12:19]

#### Q3

**Why rfid data is downsampled from 150x23 to 148x23 in the time dimension?**

The rfid receipts are not stable, theoretically each sample receives 150 pieces of data. In reality it will be one or two less, so downsample to 148. [2024-7-9 20:43:44]

------

To be updated

