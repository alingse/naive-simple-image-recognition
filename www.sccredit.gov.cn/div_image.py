#coding=utf-8
#author@alingse
#2016.07.22

#import numpy as np

from utils import img2mat
from utils import strip_list
from utils import split_list
from utils import merge_indexs
import sys

split_kwargs = dict(col_rate = 0.7,row_rate=0.4,count=4)


def split_img(bin_img,col_rate=0.7,row_rate=0.4,count=None):
    
    mat = img2mat(bin_img)
    
    splits = []
    res_list = split_mat(mat,col_rate=col_rate,row_rate=row_rate,count=count)
    for res in res_list:
        tp,_ = res
        r1,r2,c1,c2 = tp
        _img = bin_img.crop((c1,r1,c2,r2))
        splits.append((tp,_img))

    return splits


def split_mat(mat,col_rate=0.7,row_rate = 0.4, count=None):
    #row,col = mat.shape
    #use merge later
    res_list = split_bycol(mat,rate=col_rate)
    
    col_indexs = [res[0] for res in res_list]
    #add merge
    if count != None:
        col_indexs = merge_indexs(col_indexs,count)


    splits = []
    for _index in col_indexs:
        c1,c2 = _index
        _mat = mat[:,c1:c2]
        _res_list = split_bycol(_mat.transpose(),rate=row_rate)
        row_indexs = [res[0] for res in _res_list]
        #add merge
        row_indexs = merge_indexs(row_indexs,1)
        r1,r2 = row_indexs[0]
        _mat = _mat[r1:r2,:]
        tp = (r1,r2,c1,c2)
        splits.append((tp,_mat))
    return splits

#可能之后根据 merge 自动调整rate ？？
#merge 在上层添加了，自动的逻辑，后面再写
#split by col
#default rate is 70% avg 
def split_bycol(mat,rate=0.7):

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
    res_list = split_img(bin_img,col_rate=0.7,row_rate=0.4,count=4)
    for res in res_list:
        tp,_img = res
        _img.save('test.'+'-'.join(map(str,tp))+'.jpg')
    
    
