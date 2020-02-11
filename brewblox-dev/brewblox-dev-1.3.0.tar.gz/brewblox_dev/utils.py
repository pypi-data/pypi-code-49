"""
Utility functions
"""

import pathlib
from distutils.util import strtobool
from glob import glob
from os import remove
from shutil import copy
from subprocess import STDOUT, check_call


def run(cmd: str):
    print(cmd)
    check_call(cmd, shell=True, stderr=STDOUT)


def confirm(question):
    print('{} [Y/n]'.format(question))
    while True:
        try:
            return bool(strtobool(input().lower() or 'y'))
        except ValueError:
            print('Please respond with \'y(es)\' or \'n(o)\'.')


def distcopy(source, destinations):

    for dest in destinations:
        if not dest or dest == '/':
            raise AssertionError(f'Removing "{dest}/*" is a BAD idea, hmkay?')

        pathlib.Path(dest).mkdir(parents=True, exist_ok=True)

        for f in glob(dest + '/*'):
            remove(f)

        for f in glob(source + '/*'):
            copy(f, dest + '/')
            print(f'{f} ==> {dest}')
