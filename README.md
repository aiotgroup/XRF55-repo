# XRF55: A Radio Frequency Dataset for Human Indoor Action Analysis

Radio frequency(RF) devices such as Wi-Fi transceivers, radio frequency identification tags, and millimeter-wave radars have appeared in large numbers in daily lives. The presence and movement of humans can affect the propagation of RF signals, further, this phenomenon is exploited for human action recognition. Compared to camera solutions, RF approaches exhibit greater resilience to occlusions and lighting conditions, while also raising fewer privacy concerns in indoor scenarios. However, current works have many limitations, including the unavailability of datasets, insufficient training samples, and simple or limited action categories for specific applications, which seriously hinder the growth of RF solutions, presenting a significant obstacle in transitioning RF sensing research from the laboratory to a wide range of everyday life applications. To facilitate the transitioning, in this paper, we introduce and release a large-scale multiple radio frequency dataset, named XRF55, for indoor human action analysis. XRF55 encompasses 42.9K RF samples and 55 action classes of human-object interactions, human-human interactions, fitness, body motions, and human-computer interactions, collected from 39 subjects within 100 days. These actions were meticulously selected from 19 RF sensing papers and 16 video action recognition datasets. Each action is chosen to support various applications with high practical value, such as elderly fall detection, fatigue monitoring, domestic violence detection, etc. Moreover, XRF55 contains 23 RFID tags at 922.38MHz, 9 Wi-Fi links at 5.64GHz, one mmWave radar at 60-64GHz, and one Azure Kinect with RGB+D+IR sensors, covering frequency across decimeter wave, centimeter wave, and millimeter wave. In addition, we apply a mutual learning strategy over XRF55 for the task of action recognition. Unlike simple modality fusion, under mutual learning, three RF modalities are trained collaboratively and then work solely. We find these three RF modalities will promote each other. It is worth mentioning that, with synchronized Kinect, XRF55 also supports the exploration of action detection, action segmentation, pose estimation, human parsing, mesh reconstruction, etc., with RF-only or RF-Vision approaches.

## Prerequisites

- Linux
- Python 3.7
- CPU or NVIDIA GPU + CUDA CuDNN

## Getting Started

### Installation

- Clone this repo:

```bash
git clone https://github.com/aiotgroup/XRF55-repo.git
cd XRF55-repo
```

- Install [PyTorch](http://pytorch.org) and other dependencies (e.g., torchvision, torch, numpy).
  - For pip users, please type the command `pip install -r requirements.txt`.
  - For Conda users, you can create a new Conda environment using `conda env create -f environment.yml`.

### XRF train/test

- Download [XRF dataset](https://www.kaggle.com/xrfdataset/xrf55):
  - Download the `dataset.zip`, unzip it and move it to `./dataset/Raw_dataset/`

- Split train/test data:

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

### File Structrue
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
