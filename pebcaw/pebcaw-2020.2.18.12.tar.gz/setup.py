#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import setuptools

def main():
    setuptools.setup(
        name             = 'pebcaw',
        version          = '2020.02.18.0012',
        description      = 'monitor internet connection security',
        long_description = long_description(),
        url              = 'https://github.com/wdbm/pebcaw',
        author           = 'Will Breaden Madden',
        author_email     = 'wbm@protonmail.ch',
        license          = 'GPLv3',
        packages         = setuptools.find_packages(),
        install_requires = [
                           'docopt',
                           'shijian==2018.6.2.1644'
                           ],
        entry_points     = {
                           'console_scripts': ('pebcaw = pebcaw.__init__:main')
                           },
        zip_safe         = False
    )

def long_description(filename='README.md'):
    if os.path.isfile(os.path.expandvars(filename)):
        try:
            import pypandoc
            long_description = pypandoc.convert_file(filename, 'rst')
        except ImportError:
            long_description = open(filename).read()
    else:
        long_description = ''
    return long_description

if __name__ == '__main__':
    main()
