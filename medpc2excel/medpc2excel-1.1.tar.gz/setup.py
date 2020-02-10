# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:41:19 2020

@author: ycheng62
"""

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'medpc2excel',
    version = '1.1',
    auhtor = 'Yifeng Cheng',
    auhtor_email = 'cyfhopkins@gmail.com',
    description = 'A package for batch-convert medpc file to Excels',
    long_descprition = long_description,
    long_description_content_type='text/markdown',
    url = 'https://github.com/cyf203/medpc2excel',
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    python_requires='>=3.6'
    )