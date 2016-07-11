#coding=utf-8
from os import listdir

import yzm

from getimg import get_imgdata
from doimg import dealimg3 as  dealimg
from makeyzm import showimg
from yzm import imgdata2img,img2imgdata,yzmimgdata,yzm,yzmimage,show_pixel

def main():
    #test--web
    for i in range(10):
        imgdata=get_imgdata()
        im=imgdata2img(imgdata)
        nim=dealimg(im)
        show_pixel(nim)
        print ''.join(yzmimage(nim))    
        raw_input()

    test_dir="./test_data/"
    testfile_list = listdir('test_data')
    for filenamei in testfile_list:
        fname=test_dir+filenamei
        #showimg(fname).start()
        imgdata=open(fname,'r').read()
        im=imgdata2img(imgdata)
        nim=dealimg(im)
        show_pixel(nim)
        result=yzmimage(nim)
        #nimgdata=img2imgdata(nim)
        #result=yzmimgdata(nimgdata)
        #result=yzm(fname)
        print ''.join(result)
        raw_input()


if __name__ == '__main__':
    main()

