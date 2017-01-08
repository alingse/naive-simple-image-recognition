# coding=utf-8
# author@alingse
# 2016.07.20

from __future__ import print_function

import numpy as np
from PIL import Image
from StringIO import StringIO


def img2mat(img):
    col, row = img.size
    mat = np.zeros((row, col), dtype=np.int)
    for i in range(col):
        for j in range(row):
            p = img.getpixel((i, j))
            mat[j][i] = p
    return mat


def mat2array(mat, length):
    array = np.zeros(length)

    m_len = reduce(int.__mul__, mat.shape)
    m_array = mat.reshape(m_len)
    # 溢出
    m_len = min(length, m_len)
    array[:m_len] = m_array[:m_len]
    return array


def content2img(content):
    f = StringIO(content)
    img = Image.open(f)
    return img


def img2content(img):
    f = StringIO.StringIO()
    img.save(f)
    return f.getvalue()


def strip_list(elist, e):
    """
    like string strip
    """
    length = len(elist)
    for i in range(length):
        if e != elist[i]:
            break
    for j in range(length - 1, -1, -1):
        if e != elist[j]:
            break

    new = elist[i: j + 1]
    return ((i, j), new)


def split_list(elist, e):
    """
    like string split
    """
    splits = []

    start = 0
    for i, e_ in enumerate(elist):
        if e_ == e:
            _elist = elist[start: i]
            _split = ((start, i), _elist)
            splits.append(_split)

            start = i + 1

    _elist = elist[start:]
    _split = ((start, len(elist)), _elist)
    splits.append(_split)
    return splits


# what if auto merge ???计算商还是统一性？
# which is `close` and `small two`
# 策略是加了以后会怎样? 用迭代吗？
# ---  -- --   ---    ---- ----  --- --
# [(7,10),(11,14),(19,27)....]
# add closest and this is smallest

_m_diff = lambda x, y: y[0] - x[1]
_m_length = lambda x, y: y[1] - x[0]
_m_diff_length = lambda x, y: (_m_diff(x, y), _m_length(x, y))
_m_dl_cmpf = lambda dlx, dly: cmp(dlx[0], dly[0]) if dlx[0] != dly[0] else cmp(dlx[1], dly[1])


def merge_indexs(indexes, count):
    if len(indexes) <= count:
        return indexes

    size = len(indexes)
    df_len = [_m_diff_length(indexes[i - 1], indexes[i]) for i in range(1, size)]
    temp = zip(df_len, range(size - 1))
    temp = sorted(temp, key=lambda x: x[0], cmp=_m_dl_cmpf)

    # here just select the first(min) index
    x = temp[0][1]

    # x-left ---- next-right
    new = (indexes[x][0], indexes[x + 1][1])
    # merge one
    indexes = indexes[:x] + [new] + indexes[x + 2:]
    return merge_indexs(indexes, count)


def print_mat(mat, replace=str, log=None):
    if not log:
        log = lambda x: print(x, end='')

    row, col = mat.shape
    for i in range(row):
        for j in range(col):
            p = mat[i, j]
            log(replace(p))
        log('\n')


if __name__ == '__main__':
    alist = np.array([0,0,0,0,0,1,2,3,4,5,0,0,0,0,1,2,3,4,5,0,0,0,5,3,4,0,3,4,0,0],dtype=np.int) # NOQA
    # alist = [0,0,0,0,0,1,2,3,4,5,0,0,0,0,1,2,3,4,5,0,0,0,5,3,4,0,4,3,1,0,0]
    results = strip_list(alist, 0)
    indexes, newlist = results
    print(indexes)
    print(newlist)

    results = split_list(alist, 0)
    for r in results:
        indexes, newlist = r
        print(indexes, newlist)

    indexes = map(lambda res: res[0], filter(lambda res: res[1] != [], results))
    print(indexes)

    indexes = merge_indexs(indexes, 3)
    print(indexes)
    mat = np.arange(9, dtype=np.int).reshape((3, 3))
    print_mat(mat)
