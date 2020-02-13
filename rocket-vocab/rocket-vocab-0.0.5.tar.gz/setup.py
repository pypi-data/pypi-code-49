#!/usr/bin/env python3
#!-*-coding:utf8-*-
"""File setup.py"""
from setuptools import setup, find_packages
from distutils.core import setup
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
setup(
    name='rocket-vocab',
    version='0.0.5',
    packages=['rocket_vocab'],
    package_dir={'rocket_vocab': 'src/rocket_vocab'},
    # package_data={'rocket_vocab': ['src/data/*.json']},
    # package_data={'': ['*.txt', '*.json', '*.special', '*.huh']},
    include_package_data=True,
    license='MIT',
    description='learing vocabulary on terminal',
    author='huongnhd',
    author_email = 'huong.nhdh@gmail.com',
    url = 'https://github.com/huongnhdh/rocket-vocab',
    download_url = 'https://github.com/huongnhdh/rocket-vocab/archive/v005.tar.gz',
    keywords = ['vocab', 'terminal', 'true color'],
    install_requires=[
    ],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Education',
    'Topic :: System :: System Shells',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
    entry_points="""
    [console_scripts]
    rocket=rocket_vocab.rocket:main
    """
)
