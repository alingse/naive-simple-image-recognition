#coding=utf-8
#author@alingse
#2016.07.22

#import numpy as np

from utils import img2mat
from utils import strip_list
from utils import split_list

import sys


def split_img(bin_img,col_rate=0.7,row_rate=0.4):
    
    mat = img2mat(bin_img)
    
    splits = []
    res_list = split_mat(mat,col_rate=0.7,row_rate=0.4)
    for res in res_list:
        tp,_ = res
        r1,r2,c1,c2 = tp
        _img = bin_img.crop((c1,r1,c2,r2))
        splits.append((tp,_img))

    return splits


def split_mat(mat,col_rate=0.7,row_rate = 0.4):
    #row,col = mat.shape
    #use merge later
    res_list = split_bycol(mat,rate=col_rate)
    
    col_index = [res[0] for res in res_list]

    splits = []
    for _index in col_index:
        c1,c2 = _index
        _mat = mat[:,c1:c2]
        _res_list = split_bycol(_mat.transpose(),rate=row_rate)
        row_index = [res[0] for res in _res_list]
        #print row_index
        #just pick first one,use merge later
        r1,r2 = row_index[0]
        _mat = _mat[r1:r2,:]
        tp = (r1,r2,c1,c2)
        splits.append((tp,_mat))
    return splits


def merge_split(res_list,count):    
    if len(res_list) == count:
        return res_list
    return res_list[:count]


#split by col
#default rate is 70% avg 
def split_bycol(mat,rate=0.7):

    #以后再 添加，一步步写先，不考虑一次全搞定
    '''
    if type(cnt) != list:
        cnt = [cnt]
    min_cnt = min(cnt)
    max_cnt = max(cnt)
    '''
    row,col = mat.shape

    col_list = sum(mat)

    total = sum(col_list)
    threhold = total*rate/col

    col_list /= threhold
    _splits = split_list(col_list,0)
    res_list = filter(lambda res: res[1] != [],_splits)
    return res_list


if __name__ == '__main__':
    from PIL import Image
    bin_img = Image.open(sys.argv[1])
    res_list = split_img(bin_img,col_rate=0.7,row_rate=0.4)
    for res in res_list:
        tp,_img = res
        _img.save('test.'+'-'.join(map(str,tp))+'.jpg')
    
    
