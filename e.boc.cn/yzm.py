# -*- coding: utf-8 -*-
#author@yilifang
#modify@shibin

import Image
import sys
import operator
from os import listdir
from numpy import *
import numpy as np
import StringIO


train_dir="./training_data_select/"

namehash={}
yzmLabels=[]
trainingMat= zeros((372,1600))
#----------------------------------------------------------------------
def show_pixel(im):
    (col, row) = im.size
    for j in range(0, row):
        for i in range(0, col):
            pixel = im.getpixel((i, j))
            if pixel[1] <200:
                sys.stdout.write(' ')
            else:
                sys.stdout.write('M')
        sys.stdout.write('\n')
#----------------------------------------------------------------------
def show_split_pixel(im,xs,xe,ys,ye):
    for j in range(xs, xe):
        for i in range(ys, ye):
            pixel = im.getpixel((i, j))
            if pixel[1] < 200:
                sys.stdout.write(' ')
            else:
                sys.stdout.write('M')
        sys.stdout.write('\n')
#----------------------------------------------------------------------    
def findColBorder(sequence):
    state=0
    startlist=[]
    endlist=[]
    for i in range(len(sequence)):
        if sequence[i]==0 and state==0:
            pass
        elif sequence[i]!=0 and state==0:
            state=1
            start=i
            startlist.append(start)
        elif sequence[i]==0 and state!=0:
            state=0
            end=i
            endlist.append(end)
        elif sequence[i]!=0 and state!=0:
            pass
    else:
        pass
    return (startlist,endlist)

#----------------------------------------------------------------------    
def findRowBorder(sequence):
    start=0
    end=len(sequence)
    for i in range(len(sequence)):
        if sequence[i]==0:
            pass
        elif sequence[i]!=0:
            start=i
            break
    for i in range(len(sequence)-1,0,-1):
        if sequence[i]==0:
            pass
        elif sequence[i]!=0:
            end=i+1
            break
    return (start,end)

#----------------------------------------------------------------------
def splitimg(im):
    (col, row) = im.size
    colCount=np.arange(col)
    rowCount=np.arange(row)
    for j in range(0, col):
        colCount[j]=0
    for i in range(0, row):
        rowCount[i]=0    
    for j in range(0, col):
        for i in range(0, row):
            pixel = im.getpixel((j, i))
            if pixel[1] <200:
                pass
            else:
                colCount[j]+=1
                #imMat[i][j]=1
    #类似直方图
    (ysList,yeList)=findColBorder(colCount)
    #if len(ysList)!=4:
    print len(ysList),len(yeList)
    xsList=[]
    xeList=[]
    new_ysList=[]
    new_yeList=[]
    if len(ysList)>=4 and len(yeList)>=4:
        for m in range(len(ysList)):
            for i in range(0, row):
                rowCount[i]=0                
            
            for i in range(0, row):
                for j in range(ysList[m], yeList[m]):
                    pixel = im.getpixel((j, i))
                    if pixel[1] <200:
                        pass
                    else:
                        rowCount[i]+=1
            
            (rowStart,rowEnd)=findRowBorder(rowCount)
            
            print rowEnd-rowStart+yeList[m]-ysList[m]
            if (rowEnd-rowStart+yeList[m]-ysList[m])<10:
                continue
            xsList.append(rowStart)            
            xeList.append(rowEnd)
            new_ysList.append(ysList[m])
            new_yeList.append(yeList[m])
            
    else:
        return (None,None,None,None)
    if len(xsList)!=4:
        #raw_input()
        print 'error-split-',len(xsList)
        return (None,None,None,None)
    return (xsList,xeList,new_ysList,new_yeList)            
    """
    图片分割
    """
#----------------------------------------------------------------------
def img2Mat(im,vlen):
    imgMat=zeros((1,vlen))
    nim=im.resize((15,20))
    (col, row) = nim.size
    for i in range(0, row):
        for j in range(0, col):
            pixel = nim.getpixel((j, i))
            if pixel[1] < 200:
                pass
            else:
                imgMat[0][40*i+j]=1
    return imgMat
    """
    """
#----------------------------------------------------------------------
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()     
    classCount={}          
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
#----------------------------------------------------------------------
def training():
    global yzmLabels
    global trainingMat
    trainingFileList = listdir(train_dir)           #load the training set
    m = len(trainingFileList)
    trainingMat = zeros((m,1600))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .gif
        classNumStr = fileStr.split('_')[0]
        yzmLabels.append(classNumStr)
        im = Image.open(train_dir+fileNameStr)
        trainingMat[i,:]=img2Mat(im,1600)
#----------------------------------------------------------------------
def yzmimage(im):
    training()
    strlist=[]    
    (xsList,xeList,ysList,yeList)=splitimg(im)
    #show_pixel(im)

    if xsList:
        for m in range(len(xsList)):
            #show_split_pixel(im,xsList[m],xeList[m],ysList[m],yeList[m])
            splitim=im.crop((ysList[m], xsList[m], yeList[m], xeList[m]))
            testMat=img2Mat(splitim,1600)
            classifierResult = classify0(testMat, trainingMat, yzmLabels, 3)
            strlist.append(classifierResult)
        return strlist
    else:
        return None    

def imgdata2img(imgdata):
    im=Image.open(StringIO.StringIO(imgdata))
    return im
def img2imgdata(img):
    f=StringIO.StringIO()
    im.save(f,format="jpeg")
    return f.getvalue()
#在内存中
def yzmimgdata(imgdata):
    im=imgdata2img(imgdata)
    return yzmimage(im)
#
def yzm(fname):
    im = Image.open(fname)
    return yzmimage(im)

