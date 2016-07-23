#coding=utf-8
#author@alingse
#2016.07.20

from __future__ import print_function
import numpy as np
from PIL import Image

def img2mat(img):
    col,row = img.size
    mat = np.zeros((row,col),dtype=np.int)
    for i in range(col):
        for j in range(row):
            p = img.getpixel((i,j))
            mat[j][i] = p
    return mat

def mat2img(mat):
    pass

#like string strip
def strip_list(elist,e):
    i = 0 
    length = len(elist)
    for i in range(length):
        if e != elist[i]:
            break
    j = 0 
    for j in range(length-1,-1,-1):
        if e != elist[j]:
            break

    _elist = elist[i:j+1]
    return ((i,j),_elist)

#like string split
def split_list(elist,e):
    splits = []

    _elist = []
    start = 0
    for index,_e in enumerate(elist):
        if _e == e:
            _elist = elist[start:index]
            _split = ((start,index),_elist)            
            splits.append(_split)

            start = index+1
            
    _elist = elist[start:]
    _split = ((start,len(elist)),_elist)            
    splits.append(_split)

    return splits

#print mat 
def print_mat(mat,replace=lambda x:x,log=lambda x:print(x,end="")):
    row,col = mat.shape
    for i in range(0, row):
        for j in range(0, col):
            p = mat[i,j]
            _p = replace(p)
            log(_p)
        log('\n')


if __name__ == '__main__':
    alist = np.array([0,0,0,0,0,1,2,3,4,5,0,0,0,0,1,2,3,4,5,0,0,0,5,3,4,0,0,0],dtype=np.int)
    alist = [0,0,0,0,0,1,2,3,4,5,0,0,0,0,1,2,3,4,5,0,0,0,5,3,4,0,0,0]
    result = strip_list(alist,0)
    tp,blist = result
    print(tp)
    print(blist)
    result = split_list(alist,0)
    for res in result:
        tp,blist = res
        print(tp,blist,type(blist))
    mat = np.arange(9,dtype=np.int).reshape((3,3))
    print_mat(mat)


