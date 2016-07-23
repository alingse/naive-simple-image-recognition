#coding=utf-8
#author@alingse
#2016.07.22

from PIL import Image
import numpy as np

from chg_image import chg_img
from div_image import split_mat
from div_image import split_img
from div_image import split_kwargs

from utils import img2mat
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


def multiply_list(*args):
    r = 1
    for arg in args:
        r *= arg
    return r 


def mat2array(mat,length):
    mlen = multiply_list(*mat.shape)
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
 

def classfiy(mat):
    global trainingData
    if trainingData == None:
        training(trainpath)
    dataSet,labels = trainingData
    N,length = dataSet.shape
    m_array = mat2array(mat,length)

    #diff
    diffMat = np.tile(m_array,(N,1)) - dataSet
    #diffMat**2




def read_img(img):
    pass

def read_mat(mat):
    pass









if __name__ == '__main__':    
    import sys
    img = Image.open('./split_image/1000.jpg.bmp.0.4px16px6px13.bmp')
    mat = img2mat(img)

    training(trainpath)

    classfiy(mat)