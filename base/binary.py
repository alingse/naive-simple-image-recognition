# coding=utf-8
# author@alingse

from PIL import Image

import click
import os

from bin_image import bin_img


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    subcommand = ctx.invoked_subcommand
    if subcommand not in ctx.command.commands:
        ctx.obj['default']()


@main.command()
@click.argument(
    'rawpath',
    default='./raw_image',
    type=click.Path(exists=True, dir_okay=True, file_okay=False))
@click.argument(
    'binpath',
    default='./bin_image',
    type=click.Path(exists=True, dir_okay=True, file_okay=False))
def binary(binpath, rawpath):
    """ change raw image to binary image
    """

    files = os.listdir(rawpath)
    files = filter(lambda x: not x.startswith('.'), files)

    for file in files:
        img = Image.open('{}/{}'.format(rawpath, file))
        bimg = bin_img(img)
        bimg.save('{}/{}.bmp'.format(binpath, file))

    click.echo('complete binary %d images' % len(files))


@main.command()
@click.argument(
    'file',
    type=click.Path(exists=True, dir_okay=False, file_okay=True))
def test(file):
    """
    test binary func.
    """
    img = Image.open(file)
    bimg = bin_img(img)
    bimg.save('{}.bmp'.format(file))


if __name__ == '__main__':
    main(obj={'default': binary})
