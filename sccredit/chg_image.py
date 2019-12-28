#coding=utf-8
#author@alingse

from PIL import Image
import sys

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


if __name__ == '__main__':
    testf = sys.argv[1]
    img = Image.open(testf)
    nim = chg_img(img)
    nim.save(testf+'.chg.jpg')
    pass

