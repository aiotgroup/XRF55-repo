# XRF55: A Radio Frequency Dataset for Human Indoor Action Analysis

## Dataset Download Links

| Data | SDP | Kaggle | Note |
| --- | --- | --- | --- |
| mmWave, WiFi, and RFID | [SDP](https://www.sdp8.org/Dataset?id=705e08e7-637e-49a1-aff1-b2f9644467ae) | [Part 1](https://www.kaggle.com/datasets/whisperyi/xrf55-2), [Part 2](https://www.kaggle.com/datasets/whisperyi/xrf55-2) | Part 1 includes action samples from 3 individuals in scenes 2, 3, and 4, and 11 individuals in scene 1 (92.29 GB). Part 2 includes action samples from 19 individuals in scene 1 (92.29 GB). |
| WiFi and RFID raw data | - | [Kaggle](https://www.kaggle.com/datasets/xrfdataset/xrf55-rawdata) | 46.06 GB. |
| mmWave raw dataset | - | - | The previous network-disk link has expired and is temporarily unavailable. |
| mmWave RA, RD, and AD maps | [SDP](https://www.sdp8.org/Dataset?id=705e08e7-637e-49a1-aff1-b2f9644467ae) | - | Range-angle (RA), range-Doppler (RD), and angle-Doppler (AD) maps are available on SDP. |
| Video RGB | - | [Kaggle](https://www.kaggle.com/datasets/airslab2020/xrf55-rgb-depth-ir) | RGB videos from 19 participants who agreed to public release, 1280x720, downsampled to 15 fps, 43.36 GB. |
| Video Depth | - | [Part 1](https://www.kaggle.com/datasets/airslab2020/xrf55-depth-scene1), [Part 2](https://www.kaggle.com/datasets/airslab2020/xrf55-depth-scenes2-4) | Part 1 contains scene 1 (174.74 GB). Part 2 contains scenes 2, 3, and 4 (42.5 GB). Downsampled to 15 fps, 512x512. |
| Video IR | - | [Part 1](https://www.kaggle.com/datasets/airslab2020/xrf55-ir-scene1-part1), [Part 2](https://www.kaggle.com/datasets/airslab2020/xrf55-ir-scene1-part2-scenes2-4) | Part 1 contains infrared clips from scene 1 subjects 01 through 19 (189.1 GB). Part 2 contains scene 1 subjects 20 through 30 and all subjects in scenes 2 through 4 (193.37 GB). Downsampled to 15 fps, 512x512. |
| 2D pose, 3D pose, and human mesh | - | - | Processing is in progress and will be uploaded after completion. |
| mmWave point cloud | [SDP](https://www.sdp8.org/Dataset?id=705e08e7-637e-49a1-aff1-b2f9644467ae) | - | Available on SDP. |

## Action Classes

| Action Class ID (b) | Action Name |
| --- | --- |
| 1 | carrying weight |
| 2 | mopping the floor |
| 3 | using a phone |
| 4 | throwing something |
| 5 | picking something |
| 6 | putting something on the table |
| 7 | cutting something |
| 8 | wearing a hat |
| 9 | putting on clothing |
| 10 | blowing dry hair |
| 11 | combing hair |
| 12 | brushing teeth |
| 13 | drinking |
| 14 | eating |
| 15 | smoking |
| 16 | shaking hands |
| 17 | hugging |
| 18 | handing something to someone |
| 19 | kicking someone |
| 20 | hitting someone with something |
| 21 | choking someone's neck |
| 22 | pushing someone |
| 23 | body weight squats |
| 24 | Tai Chi |
| 25 | boxing |
| 26 | weightlifting |
| 27 | hula hooping |
| 28 | jumping rope |
| 29 | jumping jack |
| 30 | high leg lifting |
| 31 | waving |
| 32 | clapping hands |
| 33 | falling on the floor |
| 34 | jumping |
| 35 | running |
| 36 | sitting down |
| 37 | standing up |
| 38 | turning |
| 39 | walking |
| 40 | stretching |
| 41 | patting on the shoulder |
| 42 | playing Er-Hu |
| 43 | playing Ukulele |
| 44 | playing drum |
| 45 | foot stamping |
| 46 | shaking head |
| 47 | nodding |
| 48 | drawing a circle |
| 49 | drawing a cross |
| 50 | pushing |
| 51 | pulling |
| 52 | swiping left |
| 53 | swiping right |
| 54 | swiping up |
| 55 | swiping down |

This repository is a more detailed introduction to XRF55, containing **code**, **hardware tutorials**, and **instructions for downloading the video dataset**. If you have any questions about the above, please submit an issue and we will try to answer them as promptly as possible!

Our project page: [https://aiotgroup.github.io/XRF55](https://aiotgroup.github.io/XRF55/)

## If you want to understand or learn how our devices collect data:

[Click here](https://github.com/aiotgroup/XRF55-repo/tree/main/hardware%20tutorial) for an explanation of how the WiFi, mmWave, RFID, and Kinect devices are initialized, data collected, and processed for the device.

## If you want to reproduce our experiments:

### Prerequisites

- Linux
- Python 3.7
- CPU or NVIDIA GPU + CUDA CuDNN

### Getting Started

#### Installation

- Clone this repo:

```bash
git clone https://github.com/aiotgroup/XRF55-repo.git
cd XRF55-repo
```

- Install [PyTorch](http://pytorch.org) and other dependencies (e.g., torchvision, torch, numpy).
  - For pip users, please type the command `pip install -r requirements.txt`.
  - For Conda users, you can create a new Conda environment using `conda env create -f environment.yml`.

#### XRF train/test

- Download [XRF dataset](https://www.kaggle.com/xrfdataset/xrf55):
  - Download the `dataset.zip`, unzip it and move it to `./dataset/Raw_dataset/`

- Split train/test data:
(Used only for split train and test sets, you can rewrite the script to meet different needs)
```
python split_train_test.py 
```

- Generate label file:

```
python generate_txt.py 
```

- Train a model:

```bash
python dml_train.py 
```

- Test the model:

```bash
python dml_eval.py 
```

#### File Structrue
```bash
.
│  dml_eval.py
│  dml_train.py
│  environment.yaml
│  generate_txt.py
│  opts.py
│  README.md
│  requirements.txt
│  split_train_test.py
│  XRFDataset.py
├─dataset
│  ├─Raw_dataset
│  │  ├─mmWave
│  │  │      XX_XX_XX.npy
│  │  ├─RFID
│  │  │      XX_XX_XX.npy
│  │  └─WiFi
│  │          XX_XX_XX.npy
│  └─XRF_dataset
│      ├─test_data
│      │  ├─mmWave
│      │  │      XX_XX_XX.npy
│      │  ├─RFID
│      │  │      XX_XX_XX.npy
│      │  └─WiFi
│      │          XX_XX_XX.npy
│      └─train_data
│          ├─mmWave
│          │      XX_XX_XX.npy
│          ├─RFID
│          │      XX_XX_XX.npy
│          └─WiFi
│                  XX_XX_XX.npy  
├─model
│      resnet1d.py
│      resnet1d_rfid.py
│      resnet2d.py
├─result
│  ├─conf_matrix
│  ├─learning_curve
│  ├─params
│  └─weights
└─word2vec
        bert_new_sentence_large_uncased.npy
```

## Citations

If you find our works useful in your research, please consider citing:
```BibTeX
@article{wang2024xrf55,
  title={XRF55: A Radio Frequency Dataset for Human Indoor Action Analysis},
  author={Wang, Fei and Lv, Yizhe and Zhu, Mengdie and Ding, Han and Han, Jinsong},
  journal={Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies},
  issue={1},
  volume={8},
  year={2024},
  publisher={ACM New York, NY, USA}
}
```
