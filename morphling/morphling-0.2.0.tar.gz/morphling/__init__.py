"""
morpling is a library for transforming text in different format
"""
__version__ ='0.2.0'

import click
from morphling.copy import Copy
from morphling.input import Reader
from morphling.output import Writer
from morphling.word import create_hashtag_list, create_word_list
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

@click.command()
@click.option('--src', help='Location where intput file live.')
@click.option('--des', help='Location where output file will be placed. Note that it the directory must exist.')
def word_list(src, des):
    """This function create list of word in binary format file.
    """
    create_word_list(src, des)
    print("Completed")

@click.command()
@click.option('--src', help='Location where intput file live.')
@click.option('--des', help='Location where output file will be placed. Note that it the directory must exist.')
def hashtag_list(src, des):
    """This function create list of hashtag in binary format file.
    """
    create_hashtag_list(src, des)
    print("Completed")

script.add_command(clean_csv)
script.add_command(word_list)
script.add_command(hashtag_list)