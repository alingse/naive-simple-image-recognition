# coding=utf-8
# author@alingse
# 2016.07.20

from PIL import Image

import click
import os

from split_image import split_img
from split_image import split_kwargs


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    subcommand = ctx.invoked_subcommand
    if subcommand not in ctx.command.commands:
        ctx.obj['default']()


@main.command()
@click.argument(
    'binpath',
    default='./bin_image',
    type=click.Path(exists=True, dir_okay=True, file_okay=False))
@click.argument(
    'splitpath',
    default='./split_image',
    type=click.Path(exists=True, dir_okay=True, file_okay=False))
def split(binpath, splitpath):
    files = os.listdir(binpath)
    files = filter(lambda x: not x.startswith('.'), files)

    for file in files:
        bimg = Image.open('{}/{}'.format(binpath, file))
        res_list = split_img(bimg, **split_kwargs)

        for i, res in enumerate(res_list):
            indexes, img = res
            fname = '.'.join([file, str(i), 'px'.join(map(str, indexes)), 'bmp'])
            img.save('{}/{}'.format(splitpath, fname))
    click.echo('complete split %d images' % len(files))


@main.command()
@click.argument(
    'file',
    type=click.Path(exists=True, dir_okay=False, file_okay=True))
def test(file):
    bimg = Image.open(file)
    res_list = split_img(bimg, **split_kwargs)

    for i, res in enumerate(res_list):
        indexes, img = res
        fname = '.'.join([file, str(i), 'px'.join(map(str, indexes)), 'bmp'])
        img.save(fname)


if __name__ == '__main__':
    main(obj={'default': split})
