import logging
import torch
import csv
from torch.utils.data.dataset import Dataset, IterableDataset
import pandas as pd
import numpy as np
import h5py
log = logging.getLogger(__name__)

class XRFBertDatasetNewMix(Dataset):
    def __init__(self, file_path='./dataset/XRFDataset/', is_train=True, scene='dml'):
        super(XRFBertDatasetNewMix, self).__init__()
        self.word_list = np.load("./word2vec/bert_new_sentence_large_uncased.npy")
        self.file_path = file_path
        self.is_train = is_train
        self.scene = scene
        if self.is_train:
            self.file = self.file_path + self.scene + '_train.txt'
        else:
            self.file = self.file_path + self.scene + '_val.txt'
        file = open(self.file)
        val_list = file.readlines()
        self.data = {
            'file_name': list(),
            'label': list()
        }
        self.path = self.file_path + self.scene + '_new_data/'
        for string in val_list:
            self.data['file_name'].append(string.split(',')[0])
            self.data['label'].append(int(string.split(',')[2]) - 1)
        log.info("load XRF dataset")

    def __len__(self):
        return len(self.data['label'])

    def __getitem__(self, idx):
        file_name = self.data['file_name'][idx]
        label = self.data['label'][idx]
        vector = self.word_list[label]

        wifi_data = load_wifi(file_name, self.is_train, path=self.path)
        rfid_data = load_rfid(file_name, self.is_train, path=self.path)
        mmwave_data = load_mmwave(file_name, self.is_train, path=self.path)
        return wifi_data, rfid_data, mmwave_data, label, vector



def load_rfid(filename, is_train, path='./dataset/XRFDataset/'):
    if is_train:
        path = path + 'train_data/'
    else:
        path = path + 'test_data/'
    record = np.load(path + 'RFID/' + filename + ".npy")
    return torch.from_numpy(record).float()


def load_wifi(filename, is_train, path='./dataset/XRFDataset/'):
    if is_train:
        path = path + 'train_data/'
    else:
        path = path + 'test_data/'
    record = np.load(path + 'WiFi/' + filename + ".npy")
    return torch.from_numpy(record).float()


def load_mmwave(filename, is_train, path='./dataset/XRFDataset/'):
    if is_train:
        path = path + 'train_data/'
    else:
        path = path + 'test_data/'
    mmWave_data = np.load(path + 'mmWave/' + filename + ".npy")
    return torch.from_numpy(mmWave_data).float()

