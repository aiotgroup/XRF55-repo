import os
import shutil

import torch
import torch.utils.data as Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import h5py
import csv
import time


def split_train_test_new(root_ns="./dataset/Raw_dataset/", dst_wr="./dataset/XRF_dataset/", split=14):

    dst_train_rfid = dst_wr + "train_data/RFID/"
    dst_train_wifi = dst_wr + "train_data/WiFi/"
    dst_train_mmwave = dst_wr + "train_data/mmWave/"

    dst_test_rfid = dst_wr + "test_data/RFID/"
    dst_test_wifi = dst_wr + "test_data/WiFi/"
    dst_test_mmwave = dst_wr + "test_data/mmWave/"

    if not os.path.exists(dst_train_rfid):
        os.mkdirs(dst_train_rfid)
    if not os.path.exists(dst_train_wifi):
        os.mkdirs(dst_train_wifi)
    if not os.path.exists(dst_train_mmwave):
        os.mkdirs(dst_train_mmwave)
    if not os.path.exists(dst_test_rfid):
        os.mkdirs(dst_test_rfid)
    if not os.path.exists(dst_test_wifi):
        os.mkdirs(dst_test_wifi)
    if not os.path.exists(dst_test_mmwave):
        os.mkdirs(dst_test_mmwave)


    for file in tqdm(os.listdir(root_ns + 'RFID/')):
        filename = file.split(".")[0]  # act name
        fileidx = filename.split("_")[0]  # act idx
        actidx = int(filename.split("_")[2])
        if actidx <= zoo: # out of 20 samples of each action for each person, the first "zoo" are selected as the training set and the rest as the test set.
            shutil.copy(root_ns + 'RFID/' + filename + ".npy", dst_train_rfid + filename + ".npy")
            shutil.copy(root_ns + 'WiFi/' + filename + ".npy", dst_train_wifi + filename + ".npy")
            shutil.copy(root_ns + "mmWave/" + filename + ".npy",dst_train_mmwave + filename + ".npy")
        else:
            shutil.copy(root_ns + 'RFID/' + filename + ".npy", dst_test_rfid + filename + ".npy")
            shutil.copy(root_ns + 'WiFi/' + filename + ".npy", dst_test_wifi + filename + ".npy")
            shutil.copy(root_ns + "mmWave/" + filename + ".npy",dst_test_mmwave + filename + ".npy")

if __name__ == '__main__':

    split_train_test_new(root_ns="./dataset/Raw_dataset/", dst_wr="./dataset/XRF_dataset/", split=14)
