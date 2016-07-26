#coding=utf-8
#author@alingse
#2016.07.20

from __future__ import print_function
import numpy as np
from PIL import Image
from StringIO import StringIO

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


def content2img(content):
    f = StringIO(content)
    img = Image.open(f)
    return img

def img2content(img):
    f = StringIO.StringIO()
    img.save(f)
    return f.getvalue()


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

#what if auto merge ???计算商还是统一性？
#which is `close` and `small two`
#策略是加了以后会怎样? 用迭代吗？
#---  -- --   ---    ---- ----  --- --
#[(7,10),(11,14),(19,27)....]
#add closest and this is smallest
_m_diff = lambda x,y:y[0] - x[1]
_m_length = lambda x,y:y[1] - x[0]
_m_diff_length = lambda x,y:(_m_diff(x,y),_m_length(x,y))
_m_dl_cmpf = lambda dlx,dly: cmp(dlx[0],dly[0]) if dlx[0]!=dly[0] else cmp(dlx[1],dly[1])

def merge_indexs(indexs,count):    
    if len(indexs) <= count:
        return indexs
    size = len(indexs)
    df_len = [_m_diff_length(indexs[i-1],indexs[i]) for i in range(1,size)]
    temp = zip(df_len,range(size-1))
    temp_sorted =sorted(temp,key=lambda x:x[0],cmp=_m_dl_cmpf)
    _tmp = temp_sorted[0]
    #here just select the first
    i = _tmp[1]
    _index = (indexs[i][0],indexs[i+1][1])
    _indexs = indexs[:i] + [_index] + indexs[(i+2):]
    return merge_indexs(_indexs,count)

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
    alist = np.array([0,0,0,0,0,1,2,3,4,5,0,0,0,0,1,2,3,4,5,0,0,0,5,3,4,0,3,4,0,0],dtype=np.int)
    #alist = [0,0,0,0,0,1,2,3,4,5,0,0,0,0,1,2,3,4,5,0,0,0,5,3,4,0,4,3,1,0,0]
    result = strip_list(alist,0)
    tp,blist = result
    print(tp)
    print(blist)
    result = split_list(alist,0)
    for res in result:
        tp,blist = res
        print(tp,blist)
    indexs = map(lambda res:res[0],filter(lambda res:res[1] != [],result))
    print(indexs)
    indexs = merge_indexs(indexs,3)
    print(indexs)
    mat = np.arange(9,dtype=np.int).reshape((3,3))
    print_mat(mat)


