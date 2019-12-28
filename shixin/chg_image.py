#coding=utf-8
#author@alingse

from PIL import Image
#from numpy import *
#import math

halt = (145,135,125)

def chg_img(img):
    nimg = Image.new('L',img.size)
    col,row = img.size

    for i in range(col):                    
        for j in range(row):
            pixel = img.getpixel((i,j))
            tmp = map(lambda x:x[0]<x[1],zip(pixel,halt))
            check = len(filter(lambda x:x,tmp))
            if check > 1:
                nimg.putpixel((i,j),255)
            else:
                nimg.putpixel((i,j),0)
                
    return nimg

if __name__ == '__main__':
    pass
    
