#coding=utf-8
#2015/04/27
#author@alingse
from __future__ import print_function

from PIL import Image

import argparse
import os

from utils import img2mat
from utils import print_mat


def show_pixel(mat):
    replace = lambda x:'M' if x != 0 else ' '
    print_mat(mat,replace=replace)


def rename(splitpath,trainpath,chars,cnt=3):
    _chars = {}
    for char in chars:
        print(char,cnt)
        _chars[char] = cnt
    
    files = os.listdir(splitpath)
    for file in files:
        img = Image.open('{}/{}'.format(splitpath,file))
        #img = img
        mat = img2mat(img)
        show_pixel(mat)

        while True:
            char = raw_input('enter the char (if want pass just press  `Enter`):')
            if char == '':
                break
            if char not in _chars:
                print('char `{}` not in the chars,please check'.format(char))
            elif _chars[char] <= 0:
                break
            else:
                _chars[char] -= 1
                i = _chars[char]
                fname = '.'.join([file,str(i),char,str(ord(char)),'bmp'])
                img.save('{}/{}'.format(trainpath,fname))
                break
        #check miss
        print('still miss chars : ',end='')
        miss = False
        for char in _chars:
            need = _chars[char]
            if  need >0:
                miss = True
                print('`{}`#{},'.format(char,need),end='')
        print('')
        if miss == False:
            break


if __name__ == '__main__':
    
    digit = map(str,range(10))
    alpha = map(chr,range(ord('a'),ord('z')+1))
    alnum = digit + alpha

    parser = argparse.ArgumentParser()
    parser.add_argument('splitpath',nargs = '?',default='./split_image',help='split image save path')
    parser.add_argument('trainpath',nargs = '?',default = './train_image',help='train img save path')
    #use it later
    parser.add_argument('-c','--chars',choices=['digit','alpha','alnum'],default='digit',action='store')
    parser.add_argument('--count',default=3,type=int,help='the choosed image count per char,default is 3')
    parser.add_argument('--withoutO',action='store_true',help='remove the `o` and `0`')
    parser.add_argument('--withoutL',action='store_true',help='remove the `l` and `1`')
    parser.add_argument('--upper',action='store_true',help='if you rellay need upper')
    args = parser.parse_args()

    splitpath = os.path.abspath(args.splitpath)
    trainpath = os.path.abspath(args.trainpath)
    cnt = args.count

    if args.chars == 'digit':
        chars = digit
    if args.chars == 'alpha':
        chars = alpha
    if args.chars == 'alnum':
        chars = alnum

    if args.withoutO:
        f = lambda x:x not in ['O'.lower(),str(2-2)]
        chars = filter(f,chars)
    if args.withoutL:
        f = lambda x:x not in ['L'.lower(),str(3-2)]
        chars = filter(f,chars)

    if args.upper:
        chars = list(set(map(str.upper,chars) + chars))
    
    #or user can modify chars here
    chars = ['b','d']
    rename(splitpath,trainpath,chars,cnt=cnt)






