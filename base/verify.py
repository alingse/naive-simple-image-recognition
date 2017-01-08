# coding=utf-8
# author@alingse
# 2016.07.22

from PIL import Image
from itertools import groupby
from operator import itemgetter

import numpy as np
import os

from bin_image import bin_img
from split_image import split_mat
from split_image import split_kwargs

from utils import content2img
from utils import img2mat
from utils import mat2array


def load_train_maxsize(files):
    rows = [0]
    cols = [0]
    for file in files:
        names = file.split('.')
        indexes = names[-6].split('px')
        r1, r2, c1, c2 = map(int, indexes)
        rows.append(r2 - r1)
        cols.append(c2 - c1)

    return max(rows), max(cols)


def load_train_mat_label(trainpath, files):
    res_list = []
    for file in files:
        names = file.split('.')
        label = chr(int(names[-2]))

        img = Image.open('{}/{}'.format(trainpath, file))
        mat = img2mat(img)

        res_list.append((mat, label))
    return res_list


def training(trainpath):
    files = os.listdir(trainpath)
    files = filter(lambda x: not x.startswith('.'), files)

    max_size = load_train_maxsize(files)
    length = 3 * max_size[0] * max_size[1]

    res_list = load_train_mat_label(trainpath, files)

    N = len(res_list)

    dataSet = np.zeros((N, length))
    labels = []
    for i, res in enumerate(res_list):
        mat, label = res
        dataSet[i, :] = mat2array(mat, length)
        labels.append(label)

    return (dataSet, labels)


TRAIN_PATH = './train_image'
path = os.path.abspath(TRAIN_PATH)

# load while import
trainingData = training(path)


# 目前使用欧式平方距离其他以后再说
def distance(dataSet, matSet):
    # diff
    diffMat = matSet - dataSet
    diffMat_sq = diffMat**2
    distances = np.sqrt(diffMat_sq.sum(axis=1))
    return distances


def get_match_labal(labels, sims):
    get_label = itemgetter(0)
    get_sim = itemgetter(1)
    avg = lambda x: sum(x) * 1.0 / len(x)

    label_sims = zip(labels, sims)
    label_sims = sorted(label_sims, key=get_label)
    label_sims_gs = groupby(label_sims, key=get_label)

    label_sims = []
    for g in label_sims_gs:
        label_ = g[0]
        sims_ = map(get_sim, g[1])
        label_sims.append((label_, avg(sims_)))

    label_sims = sorted(label_sims, key=get_sim, reverse=True)
    return label_sims[0]


def classfiy(mat):
    dataSet, labels = trainingData

    N, length = dataSet.shape

    m_array = mat2array(mat, length)
    matSet = np.tile(m_array, (N, 1))

    # distance
    distances = distance(dataSet, matSet)
    # sims
    sims = 1 / (1 + distances)
    # label
    label, sim = get_match_labal(labels, sims)
    return label, sim


def read_mat(mat):
    res_list = split_mat(mat, **split_kwargs)

    result = []
    for res in res_list:
        _, mat_ = res
        result.append(classfiy(mat_))
    return result


def read_img(img):
    bimg = bin_img(img)
    mat = img2mat(bimg)
    result = read_mat(mat)
    return result


def read_content(content):
    img = content2img(content)
    result = read_img(img)
    return result
