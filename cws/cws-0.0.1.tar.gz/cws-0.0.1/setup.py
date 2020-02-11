#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requisites = []

setup(
    name='cws',
    version='0.0.1',
    description='Crossword solver',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Viet Hung Nguyen',
    author_email='hvn@familug.org',
    url='https://github.com/hvnsweeting/crossword-solver',
    license='MIT',
    classifiers=[
        'Environment :: Console',
    ],
    scripts=['cws'],
    install_requires=requisites
)
