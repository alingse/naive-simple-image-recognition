#coding=utf-8
#author@alingse
#2016.07.22

from PIL import Image
import numpy as np
from itertools import groupby
import operator

from chg_image import chg_img
from div_image import split_mat
from div_image import split_img
from div_image import split_kwargs

from utils import img2mat
from utils import print_mat
import argparse
import os


def load_train_maxsize(files):
    rows = [0]
    cols = [0]
    for file in files:
        names = file.split('.')
        rrcc = names[-6].split('px')
        rrcc = map(int,rrcc)
        r1,r2,c1,c2 = rrcc
        rows.append(r2-r1)
        cols.append(c2-c1)
    
    return (max(rows),max(cols))


def load_train_mat_label(trainpath,files):
    res_list = []
    for file in files:
        names = file.split('.')
        _ord = int(names[-2])
        label = chr(_ord)
        img = Image.open('{}/{}'.format(trainpath,file))
        mat = img2mat(img)
        res_list.append((mat,label))
    return res_list


def mat2array(mat,length):    
    mlen = reduce(operator.mul,mat.shape,1)
    _m_array = mat.reshape(mlen)
    if mlen > length:
        _m_array = _m_array[:length]
        mlen = length
    m_array = np.zeros(length)
    m_array[:mlen] = _m_array

    return m_array


trainpath = os.path.abspath('./train_image')

global trainingData
trainingData = None
#trainingData
def training(trainpath):
    files = os.listdir(trainpath)
    files = filter(lambda x:not x.startswith('.'),files)


    max_size = load_train_maxsize(files)
    res_list = load_train_mat_label(trainpath,files)

    length = 4*max_size[0]*max_size[1]
    N = len(res_list)
    dataSet = np.zeros((N,length))
    labels = []
    for i,res in enumerate(res_list):
        mat,label = res
        m_array = mat2array(mat,length)
        dataSet[i,:] = m_array
        labels.append(label)

    global trainingData
    trainingData = (dataSet,labels)
 
#目前使用欧式平方距离其他以后再说
def distance(dataSet,matSet):
    #diff
    diffMat = matSet - dataSet
    diffMat_sq = diffMat**2
    distances = np.sqrt(diffMat_sq.sum(axis=1))
    return distances


# use what distance ?
def classfiy(mat):
    global trainingData
    if trainingData == None:
        training(trainpath)
    dataSet,labels = trainingData
    
    N,length = dataSet.shape

    m_array = mat2array(mat,length)
    matSet = np.tile(m_array,(N,1))

    distances = distance(dataSet,matSet)
    #----耗时吗？
    #相似性
    sims = 1/(1+distances)
    _get_label = lambda x:x[0]
    _get_sim = lambda x:x[1]
    _avg = lambda x:sum(x)*1.0/len(x)

    label_sims = sorted(zip(labels,sims),key=_get_label)
    #通过label 来group，相关性相加,求均值？
    label_sims = groupby(label_sims,key=_get_label)
    label_simsum = map(lambda y:(y[0],_avg(map(_get_sim,y[1]))),label_sims)
    #按照相关性排序
    label_simsum_sort = sorted(label_simsum,key=_get_sim,reverse=-1)
    label,sim = label_simsum_sort[0]
    #print(label,sim)
    #print(label_simsum_sort)
    return (label,sim)


def read_raw_img(raw_img):
    bin_img = chg_img(raw_img)
    mat = img2mat(bin_img)
    #print_mat(mat,replace=lambda x:' ' if x<200 else 'M')
    result = read_mat(mat)
    return result


def read_mat(mat):
    res_list = split_mat(mat,**split_kwargs)
    result = []
    for res in res_list:
        tp,_mat = res
        #print_mat(_mat,replace=lambda x:' ' if x<200 else 'M')
        label,sim = classfiy(_mat)
        result.append((label,sim))
    return result


if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--classfiy',action='store',help='give a split image ')
    parser.add_argument('-r','--readraw',action='store',help='give a raw image')
    args = parser.parse_args()
    if args.classfiy != None:

        img = Image.open(args.classfiy)
        mat = img2mat(img)
        result = classfiy(mat)
        print(result)

    if args.readraw != None:
        raw_img = Image.open(args.readraw)
        labels = read_raw_img(raw_img)
        print(labels)
