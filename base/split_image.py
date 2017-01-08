# coding=utf-8
# author@alingse
# 2016.07.22

# import numpy as np

from utils import img2mat
# from utils import strip_list
from utils import split_list
from utils import merge_indexs

split_kwargs = dict(
    col_rate=0.7,
    row_rate=0.4,
    count=4)


# col_rate=0.7, row_rate=0.4, count=None
def split_img(bimg, **kwargs):
    if kwargs == {}:
        kwargs = split_kwargs

    mat = img2mat(bimg)

    splits = []
    results = split_mat(mat, **kwargs)
    for result in results:
        indexes, _ = result
        r1, r2, c1, c2 = indexes
        img = bimg.crop((c1, r1, c2, r2))
        splits.append((indexes, img))

    return splits


def split_mat(mat, col_rate=0.7, row_rate=0.4, count=None):
    # row, col = mat.shape
    # use merge later
    res_list = split_bycol(mat, rate=col_rate)
    col_indexs = [res[0] for res in res_list]

    # merge column
    if count is not None:
        col_indexs = merge_indexs(col_indexs, count)

    splits = []
    for col in col_indexs:
        c1, c2 = col
        mat_ = mat[:, c1:c2]

        res_list = split_bycol(mat_.transpose(), rate=row_rate)
        row_indexs = [res[0] for res in res_list]

        # add merge/ row count is 1
        row_indexs = merge_indexs(row_indexs, count=1)
        r1, r2 = row_indexs[0]

        mat_ = mat_[r1:r2, :]
        indexes = (r1, r2, c1, c2)
        splits.append((indexes, mat_))

    return splits


# 可能之后根据 merge 自动调整rate ？？
# merge 在上层添加了，自动的逻辑，后面再写
# split by col
# default rate is 70% avg
def split_bycol(mat, rate=0.7):
    row, col = mat.shape

    col_list = sum(mat)
    total = sum(col_list)

    threhold = float(total) * rate / col

    col_list /= threhold

    res_list = split_list(col_list, 0)

    res_list = filter(lambda res: res[1] != [], res_list)
    return res_list


if __name__ == '__main__':
    import sys
    from PIL import Image
    bin_img = Image.open(sys.argv[1])
    res_list = split_img(bin_img, col_rate=0.7, row_rate=0.4, count=4)
    for res in res_list:
        indexes, img = res
        fname = '-'.join(map(str, indexes))
        img.save('test.{}.jpg'.format(fname))
