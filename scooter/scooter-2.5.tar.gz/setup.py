#!/usr/bin/python

from setuptools import setup

setup(
    name       = 'scooter',
    version    = '2.5',
    packages   = ['scooter'],
    py_modules = ['scooter.gcc', 'scooter.llvm', 'build_script', 'remote_vs'],
    # http://stackoverflow.com/questions/12372336/how-do-i-make-pip-respect-requirements
    install_requires = [
        'quickfiles',
        'quickstructures',
        'ellbur-easyrun',
    ]
)

