# coding=utf-8
# author@alingse

from PIL import Image

halt = (145, 135, 125)


def bin_img(img):
    nim = Image.new('L', img.size)
    col, row = img.size
    for i in range(col):
        for j in range(row):
            pixel = img.getpixel((i, j))
            tmp = map(lambda x: x[0] < x[1], zip(pixel, halt))
            check = len(filter(None, tmp))
            p = 255 if check > 1 else 0
            nim.putpixel((i, j), p)

    return nim


if __name__ == '__main__':
    import sys
    fname = sys.argv[1]
    img = Image.open(fname)
    nim = bin_img(img)
    nim.save(fname+'.bin.bmp')
