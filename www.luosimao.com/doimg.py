#coding=utf-8
from os import listdir
import os
import sys
import Image
from numpy import *
import math

test_dir='./test_data/'
result_dir='./IMG/'

Colorbit=256
Step=2
Len=Colorbit/Step

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
    col,row=im.size
    for i in range(col):                    
        for j in range(row):
            t=im.getpixel((i,j))
            nim.putpixel((i,j),(0,0,0))
            if Iscolor(t):
                nim.putpixel((i,j),(255,255,255))
    return nim

def dealimg2(im):
    #r,g,b = im.split()
    nim=Image.new('RGB',im.size)
    col,row=im.size
    halt=(130,130,130)
    for i in range(col):            
        for j in range(row):
            t=im.getpixel((i,j))
            if sum(t)<sum(halt)+15 or min(t)<100:
            #check=1
            #if t[0]< halt[0]:check+=1
            #if t[1]< halt[1]:check+=1
            #if t[2]< halt[2]:check+=1
            #if check>=2:
                nim.putpixel((i,j),(255,255,255))
            else:
                nim.putpixel((i,j),(0,0,0))
                
    return nim
"""
def dealimg3(im):
    nim=Image.new('RGB',im.size)
    col,row=im.size
    color_count={}
    for i in range(Len):
        color_count[i]={}
        for j in range(Len):
            color_count[i][j]={}
            for k in range(Len):
                color_count[i][j][k]=0
    for i in range(col):
        for j in range(row):
            t=im.getpixel((i,j))
            color_count[t[0]/Step][t[1]/Step][t[2]/Step]+=1
    
    color_list=[]
    for i in range(Len):
        for j in range(Len):
            for k in range(Len):
                if color_count[i][j][k]==0:
                    continue
                color=(color_count[i][j][k],(i,j,k))
                color_list.append(color)
    sortcmp=lambda x,y:x[0]-y[0]
    sort_list=sorted(color_list,cmp=sortcmp,reverse=True)
    back=sort_list[0]
    number={}
    for i in range(2,5):
        t=sort_list[i][1]
        check=0
        if t[0]<50:check+=1
        if t[1]<50:check+=1
        if t[2]<50:check+=1
        if check<2:
            continue
        number[t]=sort_list[i][0]
    print number
    for i in range(col):
        for j in range(row):
            t=im.getpixel((i,j))
            tcolor=(t[0]/Step,t[1]/Step,t[2]/Step)
            if tcolor==back[1]:
                nim.putpixel((i,j),(0,0,0))
            if tcolor in number:    
                nim.putpixel((i,j),(255,255,255))
            else:
                nim.putpixel((i,j),(0,0,0))
                #continue
                #if ==back[1][0] and t[1]/Step==back[1][1] and t[2]/Step==back[1][2]:
            
    
    #for i in range(10):
    #    print sort_list[i]
    return nim
"""
if __name__ == '__main__':
    
    testfile_list = listdir('test_data')
    for filenamei in testfile_list:
        print filenamei
        fname=test_dir+filenamei
        im=Image.open(fname)
        #newim=dealimg(im)
        newim=dealimg2(im)
        #exit()
        #if row_input(':')=='':
        #    newim.show()
        newim.save(result_dir+filenamei)
    
