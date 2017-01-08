# coding=utf-8
# 2015/04/27
# author@alingse

from PIL import Image

import click
import os

from utils import img2mat
from utils import print_mat


def show_pixel(mat):
    replace = lambda x: 'M' if x == 255 else ' '
    print_mat(mat, replace=replace)


digit = map(str, range(10))
alpha = map(chr, range(ord('a'), ord('z') + 1))
alnum = digit + alpha


def get_chars(chars, upper, without):
    if chars == 'digit':
        chars = digit
    elif chars == 'alpha':
        chars = alpha
    elif chars == 'alnum':
        chars = alnum

    chars = filter(lambda c: c not in without, chars)

    if upper:
        chars = list(set(map(str.upper, chars) + chars))

    return chars


@click.command()
@click.option(
    '--without',
    type=unicode,
    help='remove the char, like: --without \'o01lI\'',
    default='')
@click.option(
    '--upper',
    is_flag=True,
    default=False)
@click.option(
    '-c',
    '--chars',
    type=click.Choice(['digit', 'alpha', 'alnum']),
    default='digit',
    help='choose chars')
@click.option(
    '--count',
    type=int,
    default=3,
    help='tarin sample number per char')
@click.argument(
    'trainpath',
    default='./train_image',
    type=click.Path(exists=True, dir_okay=True, file_okay=False))
@click.argument(
    'splitpath',
    default='./split_image',
    type=click.Path(exists=True, dir_okay=True, file_okay=False))
def rename(splitpath, trainpath, count, **kwargs):
    chars = get_chars(**kwargs)

    chars_map = {}
    for char in chars:
        chars_map[char] = count

    files = os.listdir(splitpath)
    files = filter(lambda x: not x.startswith('.'), files)

    for file in files:

        img = Image.open('{}/{}'.format(splitpath, file))
        mat = img2mat(img)
        show_pixel(mat)

        while True:
            char = raw_input('enter the char (if want pass just press  `Enter`):')
            if char == '':
                break
            if char not in chars_map:
                click.echo('!!! char `{}` not in the chars,please check'.format(char))
                continue
            elif chars_map[char] > 0:
                chars_map[char] -= 1
                i = chars_map[char]
                fname = '.'.join([file, str(i), char, str(ord(char)), 'bmp'])
                img.save('{}/{}'.format(trainpath, fname))

            break

        miss = filter(lambda x: x[1] > 0, chars_map.iteritems())
        # check miss
        if not miss:
            break

        miss = map(lambda x: '`{0}`#{1}'.format(*x), miss)
        click.echo('still miss chars : {}'.format(','.join(miss)))


if __name__ == '__main__':
    rename()
