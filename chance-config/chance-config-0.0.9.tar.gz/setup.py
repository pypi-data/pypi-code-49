#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: setup.py
# Author: Jimin Huang <huangjimin@whu.edu.cn>
# Date: 19.10.2017
from __future__ import absolute_import
from setuptools import setup


setup(
    name='chance-config',
    version='0.0.9',
    description='The config for chancefocus',
    url='https://git.chancefocus.com/transaction/common/chance-config.git',
    author='Jimin Huang',
    author_email='jimin@chancefocus.com',
    license='MIT',
    packages=['chanconfig'],
    install_requires=[
        'nose>=1.3.7',
        'PyYAML>=3.11',
        'coverage>=5.0',
        'attrdict>=2.0.0',
        'flake8>=3.3.0',
        'chance-mock-logger>=0.0.2',
    ],
    zip_safe=False,
)
