#coding=utf-8
#author@alingse
#2016.07.20

from PIL import Image

import argparse
import os

from div_image import split_img

def split(binpath,splitpath):
    files = os.listdir(binpath)
    for file in files:
        if file.startswith('.'):
            continue 
        img = Image.open('{}/{}'.format(binpath,file))
        img = img.convert('L')
        res_list = split_img(img)

        for i,res in enumerate(res_list):
            tp,_img = res
            fname = '.'.join([file,str(i),'px'.join(map(str,tp)),'jpg'])
            _img.save('{}/{}'.format(splitpath,fname))

if __name__ == '__main__':  
    parser = argparse.ArgumentParser()
    parser.add_argument('binpath',nargs = '?',default = './bin_image',help='bin img save path')
    parser.add_argument('splitpath',nargs = '?',default='./split_image',help='split image save path')
    args = parser.parse_args()

    binpath = os.path.abspath(args.binpath)
    splitpath = os.path.abspath(args.splitpath)
    split(binpath,splitpath)
