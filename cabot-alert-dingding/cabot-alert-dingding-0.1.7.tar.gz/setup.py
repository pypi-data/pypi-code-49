#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
if sys.version_info[0] < 3:
    with open(os.path.join(BASE_DIR, 'README.md')) as f:
        long_description = f.read()
else:
    with open(os.path.join(BASE_DIR, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
    
setup(
    name='cabot-alert-dingding',
    version='0.1.7',
    description='A Dingding plugin for Cabot',
    long_description=long_description,
    author='hanya',
    author_email='464975798@qq.com',
    url='https://github.com/hanya070603',
    packages=find_packages(),
    download_url = 'https://github.com/hanya070603/',
    long_description_content_type="text/markdown",
    keywords = ['cabot', 'dingding', 'status check'],
)
