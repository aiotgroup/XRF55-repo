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

#### Q4

**How can I find the corresponding labels for each `.npy` file in the XRF55 dataset?**

**A:** The label information for each file in the dataset is encoded directly within its filename. The naming format is `a_b_c.npy`, with the following structure:

* **`a`**: Represents the unique ID of the volunteer.
* **`b`**: Represents the action class ID. This ID corresponds directly to the action classes listed in **Table 2** on page 9 of our paper, "XRF55: A Radio Frequency Dataset for Human Indoor Action Analysis."
* **`c`**: Represents the sequence number for the repetition of the action performed by that volunteer.

For example, a file named `15_4_3.npy` indicates that this is the 3rd repetition of action class 4 (throwing something) performed by volunteer 15.

For your convenience, here is the complete mapping of the action class ID (`b`) to the specific action, as presented in Table 2 of the paper:

| Action Class ID (b) | Action Name                    |
| :------------------ | :----------------------------- |
| 1                   | carrying weight                |
| 2                   | mopping the floor              |
| 3                   | using a phone                  |
| 4                   | throwing something             |
| 5                   | picking something              |
| 6                   | putting something on the table |
| 7                   | cutting something              |
| 8                   | wearing a hat                  |
| 9                   | putting on clothing            |
| 10                  | blowing dry hair               |
| 11                  | combing hair                   |
| 12                  | brushing teeth                 |
| 13                  | drinking                       |
| 14                  | eating                         |
| 15                  | smoking                        |
| 16                  | shaking hands                  |
| 17                  | hugging                        |
| 18                  | handing something to someone   |
| 19                  | kicking someone                |
| 20                  | hitting someone with something |
| 21                  | choking someone's neck         |
| 22                  | pushing someone                |
| 23                  | body weight squats             |
| 24                  | Tai Chi                        |
| 25                  | boxing                         |
| 26                  | weightlifting                  |
| 27                  | hula hooping                   |
| 28                  | jumping rope                   |
| 29                  | jumping jack                   |
| 30                  | high leg lifting               |
| 31                  | waving                         |
| 32                  | clapping hands                 |
| 33                  | falling on the floor           |
| 34                  | jumping                        |
| 35                  | running                        |
| 36                  | sitting down                   |
| 37                  | standing up                    |
| 38                  | turning                        |
| 39                  | walking                        |
| 40                  | stretching                     |
| 41                  | patting on the shoulder        |
| 42                  | playing Er-Hu                  |
| 43                  | playing Ukulele                |
| 44                  | playing drum                   |
| 45                  | foot stamping                  |
| 46                  | shaking head                   |
| 47                  | nodding                        |
| 48                  | drawing a circle               |
| 49                  | drawing a cross                |
| 50                  | pushing                        |
| 51                  | pulling                        |
| 52                  | swiping left                   |
| 53                  | swiping right                  |
| 54                  | swiping up                     |
| 55                  | swiping down                   |

[2025-10-15 17:14:55]

------

To be updated


