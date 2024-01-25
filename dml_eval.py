import os

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

import torch
import torch.utils.data as Data
from torch.autograd import Variable
import gdown
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


def check_weight_file(path):
    url_mmwave = 'https://drive.google.com/file/d/1vJou1BnwCreCkqu-10mdg45tqARdGeU5/view?usp=sharing'
    url_rfid = 'https://drive.google.com/file/d/1fnPpXoCGjTs17Ia_4NuitRODybB_Xhwc/view?usp=sharing'
    url_wifi = 'https://drive.google.com/file/d/1RM2wEE3AjOv0aYKnOcMJMdx7PmQp3XNM/view?usp=sharing'
    if not (os.path.exists(os.path.join(path, 'model0_params.pth'))):
        print('downloading wifi weights file.')
        gdown.download(url_wifi, os.path.join(path, 'model0_params.pth'), quiet=False, fuzzy=True)
    else:
        print('wifi weights file already exists.')
    if not (os.path.exists(os.path.join(path, 'model1_params.pth'))):
        print('downloading rfid weights file.')
        gdown.download(url_rfid, os.path.join(path, 'model1_params.pth'), quiet=False, fuzzy=True)
    else:
        print('rfid weights file already exists.')
    if not (os.path.exists(os.path.join(path, 'model2_params.pth'))):
        print('downloading mmwave weights file.')
        gdown.download(url_mmwave, os.path.join(path, 'model2_params.pth'), quiet=False, fuzzy=True)
    else:
        print('mmwave weights file already exists.')



if __name__ == "__main__":
    model_name = "train_dml"
    scene = model_name.split('_')[-1]
    print(model_name)
    args = parse_opts()

    # Download weights file from Google Drive
    weight_file_path = './result/params/'
    check_weight_file(weight_file_path)

    starttime = datetime.datetime.now()
    '''========================= Dataset =========================='''
    test_dataset = XRFDataset.XRFBertDatasetNewMix(is_train=False, scene=scene)

    test_size = int(test_dataset.__len__())

    test_data = Data.DataLoader(dataset=test_dataset, batch_size=args.batch_size, shuffle=True, pin_memory=True,
                                num_workers=16)

    '''========================= Model =========================='''
    models = [
        resnet1d.resnet18_mutual(),  # WiFi
        resnet1d_rfid.resnet18_mutual(),  # RFID
        resnet2d.resnet18_mutual()  # MmWave
    ]

    test_loss = np.zeros([args.model_num])
    test_acc = np.zeros([args.model_num])
    temp_test = [0 for _ in range(args.model_num)]
    print("--------------Mutual Learning---------------")
    print("validate on {} samples.".format(test_size))
    max_acc = [0, 0, 0]
    conf_matrix = []
    correct_test = []
    testacc = []
    for m in range(args.model_num):
        # load models param
        models[m].load_state_dict(torch.load(f'./result/params/model{m}_params.pth'))
        models[m] = models[m].cuda()
        models[m].eval()
        conf_matrix.append([[0 for _ in range(args.class_num)] for _ in range(args.class_num)])
        correct_test.append(0)

    for samples_wifi, samples_rfid, samples_mmwave, labels, vectors in tqdm(test_data):
        with torch.no_grad():
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

            for i in range(args.model_num):
                prediction = model_outputs[i].data.max(1)[1]
                correct_test[i] += prediction.eq(labelsV.data).sum()
                conf_matrix[i] = get_conf_matrix(prediction, labels, conf_matrix[i])

    for m in range(args.model_num):
        acc = 100 * float(correct_test[m]) / test_size
        print("Model ", m, "Test accuracy:", acc)
        max_acc[m] = max(max_acc[m], acc)
        test_acc[m] = 100 * float(correct_test[m]) / test_size
        testacc.append(str(100 * float(correct_test[m]) / test_size)[0:6])

    '''======================================== Plot ============================================='''
    for m in range(args.model_num):
        if correct_test[m] > temp_test[m]:
            plt.matshow(conf_matrix[m], cmap=plt.cm.Reds)
            for i in range(len(conf_matrix[m])):
                for j in range(len(conf_matrix[m])):
                    plt.text(j, i, str(conf_matrix[m][i][j]), horizontalalignment='center',
                             verticalalignment='center',
                             fontsize=4)
            plt.ylabel('True label')
            plt.xlabel('Predicted label')
            # plt.show()
            if not os.path.exists('result/conf_matrix/' + model_name + '/') and not os.path.exists(
                    'result/weights/' + model_name + '/'):
                os.mkdir('result/conf_matrix/' + model_name + '/')
                os.mkdir('result/weights/' + model_name + '/')
            if not os.path.exists(
                    'result/conf_matrix/' + model_name + '/' + str(m) + '/') and not os.path.exists(
                'result/weights/' + model_name + '/' + str(m) + '/'):
                os.mkdir('result/conf_matrix/' + model_name + '/' + str(m) + '/')
                os.mkdir('result/weights/' + model_name + '/' + str(m) + '/')
            plt.savefig(
                'result/conf_matrix/' + model_name + '/' + str(m) + '/' + model_name + '_' +
                testacc[m] + '.jpg', dpi=300)
            write_to_file(conf_matrix[m],
                          'result/weights/' + model_name + '/' + str(m) + '/' + model_name + '_' + testacc[m])
            torch.save(models[m],
                       'result/weights/' + model_name + '/' + str(m) + '/' + model_name + '_' + testacc[m] + '.pkl')
            plt.close()
            temp_test[m] = correct_test[m]

    for m in range(args.model_num):
        print("max_accuracy: ", max_acc[m])
        if not os.path.exists('result/learning_curve/' + model_name + '/'):
            os.mkdir('result/learning_curve/' + model_name + '/')
        # for learning curves
        sio.savemat(
            'result/learning_curve/' + model_name + '/'
            + model_name + '_' + str(m) + '_test_loss' + '.mat', {'test_loss': test_loss[m]})
        sio.savemat(
            'result/learning_curve/' + model_name + '/'
            + model_name + '_' + str(m) + '_test_acc' + '.mat', {'test_acc': test_acc[m]})

    print(model_name)
    endtime = datetime.datetime.now()
    print(starttime)
    print(endtime)
    print((endtime - starttime).seconds)
