#coding=utf-8
#author@alingse

from PIL import Image

import argparse
import os

halt = (145,135,125)

def chg_img(img):
    nim = Image.new('L',img.size)
    col,row = img.size
    for i in range(col):                    
        for j in range(row):
            pixel = img.getpixel((i,j))
            tmp = map(lambda x:x[0]<x[1],zip(pixel,halt))
            check = len(filter(lambda x:x,tmp))
            if check > 1:
                nim.putpixel((i,j),255)
            else:
                nim.putpixel((i,j),0)
                
    return nim


def main(rawpath,binpath):
    files = os.listdir(rawpath)
    for file in files:
        if file.startswith('.'):
            continue 
        img = Image.open('{}/{}'.format(rawpath,file))
        bin_img = chg_img(img)
        bin_img.save('{}/{}'.format(binpath,file))


if __name__ == '__main__':  
    parser = argparse.ArgumentParser()
    parser.add_argument('rawpath',nargs = '?',default = './raw_image',help='raw img save path')
    parser.add_argument('binpath',nargs = '?',default='./bin_image',help='bin image save path')
    args = parser.parse_args()

    rawpath = os.path.abspath(args.rawpath)
    binpath = os.path.abspath(args.binpath)
    main(rawpath,binpath)

    

    
