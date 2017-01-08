# coding=utf-8
# author@alingse
# 2017.01.09

import click

from verify import read_content


@click.command()
@click.argument('file', type=click.File('rb'))
def main(file):
    """
    test verify
    """
    content = file.read()
    result = read_content(content)
    chars = map(lambda x: x[0], result)

    click.echo(result)
    click.echo(chars)


if __name__ == '__main__':
    main()
