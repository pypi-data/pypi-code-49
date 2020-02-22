#!/usr/bin/python

from setuptools import setup

setup(
    name       = 'ellbur-easyrun',
    version    = '0.3',
    py_modules = ['ellbureasyrun'],
    install_requires = [
        'quickfiles',
        'quickstructures'
    ]
)

