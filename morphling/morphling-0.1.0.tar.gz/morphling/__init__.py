"""
morpling is a library for transforming text in different format
"""
__version__ ='0.1.0'

import click
from morphling.copy import Copy
from morphling.input import Reader
from morphling.output import Writer

@click.group()
def script():
    pass

@click.command()
@click.option('--src', help='Location where intput file live.')
@click.option('--des', help='Location where output file will be placed. Note that it the directory must exist.')
def clean_csv(src, des):
    """This function will rewrite csv file with double qoute embrace a string
        when it is in different line.
    """
    reader = Reader()
    writer = Writer()
    obj = Copy(reader, writer)
    obj.restruct_csv(src, des)
    print("Completed")

script.add_command(clean_csv)