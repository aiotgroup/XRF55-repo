# XRF55: A Radio Frequency Dataset for Human Indoor Action Analysis

This repository is a more detailed introduction to XRF55, containing **code**, **hardware tutorials**, and **instructions for downloading the video dataset**. If you have any questions about the above, please submit an issue and we will try to answer them as promptly as possible!

Our project page: [https://aiotgroup.github.io/XRF55](https://aiotgroup.github.io/XRF55/)

## If you want to understand or learn how our devices collect data:

[Click here](https://github.com/aiotgroup/XRF55-repo/tree/main/hardware%20tutorial) for an explanation of how the WiFi, mmWave, RFID, and Kinect devices are initialized, data collected, and processed for the device.

## If you want to download our video dataset but have questions about it:

[readme_for_video_users.md](./readme%20for%20video%20users.md) will help you to process the downloaded XRF55 video dataset correctly!

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
