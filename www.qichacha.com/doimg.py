#coding=utf-8
from os import listdir
import os
import sys
import Image
from numpy import *
import math

test_dir='./test_data/'
result_dir='./IMG/'

argps=3.0/math.sqrt(10.0)+0.15

def dealimg(im):
    def Iscolor(t):
        #画图－正方形右上顶点，引两条线到左下两边中点
        #以内为灰度暗点，以外为彩色亮点。
        #可推广到3维/或者取正方形对角一定距离的平行线
        #以内为灰度点，以外为彩色点。
        lt=[]
        lt.append(255-max(t))
        lt.append(255-min(t))
        lts=(lt[0]*lt[0]+lt[1]*lt[1])
        lts=math.sqrt(2*lts)
        ps=sum(t)*1.0/(lts+0.1)
        if ps>argps:
            return True
        return False   
    nim=Image.new('RGB',im.size)
    col,raw=im.size
    for i in range(col):                    
        for j in range(raw):
            t=im.getpixel((i,j))
            nim.putpixel((i,j),(0,0,0))
            if Iscolor(t):
                nim.putpixel((i,j),(255,255,255))
    return nim

def dealimg2(im):
    #r,g,b = im.split()
    nim=Image.new('RGB',im.size)
    col,raw=im.size
    halt=(130,110,120)
    for i in range(col):                    
        for j in range(raw):
            t=im.getpixel((i,j))
            check=0
            if t[0]< halt[0]:check+=1
            if t[1]< halt[1]:check+=1
            if t[2]< halt[2]:check+=1
            if check>=1:
                nim.putpixel((i,j),(255,255,255))
            else:
                nim.putpixel((i,j),(0,0,0))
                
    return nim

Colorbit=256
Step=1
Len=Colorbit/Step

gen_level = lambda x:(x-1)/Step +1


def dealimg3(im):
    #r,g,b = im.split()
    nim=Image.new('RGB',im.size)
    col,raw=im.size
    color_count={}

    for i in range(col):                    
        for j in range(raw):
            t=im.getpixel((i,j))
            level=map(gen_level,t)
            level_str='_'.join(map(str,level))            
            if level_str not in color_count:
                color_count[level_str]=0
            color_count[level_str]+=1
    
    
    color_count_sorted=sorted(color_count.items(),cmp,lambda x:x[1],reverse=1)
    valid_level=[]
    valid_level.append(color_count_sorted[1][0])
    for i in range(col):                    
        for j in range(raw):
            t=im.getpixel((i,j))
            level=map(gen_level,t)
            level_str='_'.join(map(str,level))
            if level_str in valid_level:
                nim.putpixel((i,j),(255,255,255))
            else:
                nim.putpixel((i,j),(0,0,0))
                
    return nim


if __name__ == '__main__':
    
    testfile_list = listdir('test_data')
    for filenamei in testfile_list:
        print filenamei
        fname=test_dir+filenamei
        im=Image.open(fname)
        #newim=dealimg(im)
        #newim=dealimg2(im)
        newim=dealimg3(im)
        #newim.show()
        #if raw_input(':')=='':
        newim.save(result_dir+filenamei)
    
