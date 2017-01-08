# coding=utf-8
# 2015/04/24
# author@alingse

import click
import time

from down_image import get_img


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    if ctx.invoked_subcommand not in ctx.command.commands:
        ctx.obj['default']()


@main.command()
@click.option(
    '-t',
    '--type',
    type=click.Choice(['jpg', 'png', 'bmp']),
    default='jpg',
    help='image content type')
@click.option(
    '-c',
    '--count',
    type=int,
    default=900,
    help='download count')
@click.argument(
    'rawpath',
    default='./raw_image',
    type=click.Path(exists=True, dir_okay=True, file_okay=False))
def download(rawpath, count, type):
    """
    download raw image
    """
    start = 10 * count
    end = 11 * count

    i = start

    while i < end:
        content = get_img()
        if not content:
            # sleep
            click.echo('error sleep 3s')
            time.sleep(3)
            continue

        fname = '{}/{}.{}'.format(rawpath, i, type)

        f = open(fname, 'wb')
        f.write(content)
        f.close()

        click.echo('download no:{0} image'.format(i))
        i += 1
        # sleep
        time.sleep(0.7)


@main.command()
@click.argument(
    'file',
    type=click.File('wb'))
def test(file):
    content = get_img()
    if content is None:
        file.close()
        raise Exception('test download failed')

    file.write(content)
    file.close()


if __name__ == '__main__':
    main(obj={'default': download})
