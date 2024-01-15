import os

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

import torch
import torch.nn as nn
import torch.utils.data as Data
import torch.nn.functional as F
from torch.autograd import Variable
import mmd_loss
import numpy as np
import pandas as pd
from tqdm import tqdm
import scipy.io as sio
import matplotlib.pyplot as plt
import datetime
import XRFDataset
from opts import parse_opts
from model import resnet1d, resnet1d_rfid, resnet2d


def get_conf_matrix(pred, truth, conf_matrix):
    p = pred.tolist()
    l = truth.tolist()
    for i in range(len(p)):
        conf_matrix[l[i]][p[i]] += 1
    return conf_matrix


def write_to_file(conf_matrix, path):
    conf_matrix_m = conf_matrix
    for x in range(len(conf_matrix_m)):
        base = sum(conf_matrix_m[x])
        for y in range(len(conf_matrix_m[0])):
            conf_matrix_m[x][y] = format(conf_matrix_m[x][y] / base, '.2f')
    df = pd.DataFrame(conf_matrix_m)
    df.to_csv(path + '.csv')


if __name__ == "__main__":
    # Used to save the names of model parameters and subsequent evaluations.
    model_name = "train_dml"
    scene = model_name.split('_')[-1]
    print(model_name)
    starttime = datetime.datetime.now()
    args = parse_opts()

    '''========================= Dataset =========================='''
    # get data and label
    train_dataset = XRFDataset.XRFBertDatasetNewMix(is_train=True, scene=scene)
    # define train_dataset size
    train_size = int(train_dataset.__len__())
    # import train_data
    train_data = Data.DataLoader(dataset=train_dataset, batch_size=args.batch_size, shuffle=True, pin_memory=True,
                                 num_workers=16, drop_last=False)

    '''========================= Model =========================='''
    models = [
        resnet1d.resnet18_mutual(),  # WiFi
        resnet1d_rfid.resnet18_mutual(),  # RFID
        resnet2d.resnet18_mutual()  # MmWave
    ]

    optimizers = []
    schedulers = []
    for m in range(args.model_num):
        models[m] = models[m].cuda()
        optimizers.append(torch.optim.Adam(models[m].parameters(), lr=args.lr))
        schedulers.append(torch.optim.lr_scheduler.MultiStepLR(optimizers[m],
                                                               milestones=[40, 80, 120, 160],
                                                               gamma=0.5))

    train_loss = np.zeros([args.model_num, args.epoch])
    print("--------------Mutual Learning---------------")
    print("Train on {} samples.".format(train_size))

    loss_ce = nn.CrossEntropyLoss().cuda()
    loss_l1 = torch.nn.L1Loss().cuda()
    loss_diff = nn.KLDivLoss(reduction='batchmean').cuda()

    idx = 0
    if not os.path.exists('result/params/' + model_name + '/'):
        os.mkdir('result/params/' + model_name + '/')

    for epoch in range(args.epoch):
        print("Epoch:", epoch)
        '''======================================== Train ==========================================='''
        losses = []
        for m in range(args.model_num):
            # models[m] = models[m].cuda()
            models[m].train()
            losses.append(0)

        for (samples_wifi, samples_rfid, samples_mmwave, labels, vectors) in tqdm(train_data):
            samplesWifi = Variable(samples_wifi.cuda())
            samplesRfid = Variable(samples_rfid.cuda())
            samplesMmWave = Variable(samples_mmwave.cuda())
            labelsV = Variable(labels.cuda())
            vectorsV = Variable(vectors.cuda())

            model_outputs = [0 for _ in range(args.model_num)]
            model_vecs = [0 for _ in range(args.model_num)]

            model_outputs[0], model_vecs[0] = models[0](samplesWifi)
            model_outputs[1], model_vecs[1] = models[1](samplesRfid)
            model_outputs[2], model_vecs[2] = models[2](samplesMmWave)
            loss = []
            for i in range(args.model_num):
                ce_loss = loss_ce(model_outputs[i], labelsV)
                vec_ce_loss = loss_l1(model_vecs[i], vectorsV)
                diff_loss = 0
                for j in range(args.model_num):
                    if i != j:
                        diff_loss = diff_loss + loss_diff(F.log_softmax(model_outputs[i], dim=1),
                                                          F.softmax(Variable(model_outputs[j]), dim=1))

                loss.append(vec_ce_loss + ce_loss + diff_loss / (args.model_num - 1))
                losses[i] = losses[i] + loss[i].item()

            for i in range(args.model_num):
                optimizers[i].zero_grad()
            for i in range(args.model_num):
                loss[i].backward(retain_graph=True)
            for i in range(args.model_num):
                optimizers[i].step()
        for i in range(args.model_num):
            schedulers[i].step()

        for m in range(args.model_num):
            train_loss[m, epoch] = losses[m] / train_size
            print('Model ', m, ' train_loss: ', losses[m] / train_size)
        if epoch >= args.epoch-10:
            for m in range(args.model_num):
                torch.save(models[m].state_dict(), f'./result/params/{model_name}/model{m}_epoch{idx}.pth')
            idx += 1

    for m in range(args.model_num):
        if not os.path.exists('result/learning_curve/' + model_name + '/'):
            os.mkdir('result/learning_curve/' + model_name + '/')
        # for learning curves
        sio.savemat(
            'result/learning_curve/' + model_name + '/'
            + model_name + '_' + str(m) + '_train_loss' + '.mat', {'train_loss': train_loss[m]})

    print(model_name)
    endtime = datetime.datetime.now()
    print(starttime)
    print(endtime)
    print((endtime - starttime).seconds)
