#coding=utf-8
#author@alingse

from PIL import Image

import argparse
import os

from chg_image import chg_img

def binary(rawpath,binpath):
    files = os.listdir(rawpath)
    for file in files:
        if file.startswith('.'):
            continue 
        img = Image.open('{}/{}'.format(rawpath,file))
        bin_img = chg_img(img)
        bin_img.save('{}/{}.bmp'.format(binpath,file))


if __name__ == '__main__':  
    parser = argparse.ArgumentParser()
    parser.add_argument('rawpath',nargs = '?',default = './raw_image',help='raw img save path')
    parser.add_argument('binpath',nargs = '?',default='./bin_image',help='bin image save path')
    args = parser.parse_args()

    rawpath = os.path.abspath(args.rawpath)
    binpath = os.path.abspath(args.binpath)
    binary(rawpath,binpath)