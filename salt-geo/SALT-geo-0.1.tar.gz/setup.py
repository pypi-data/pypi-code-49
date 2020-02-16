#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 05:42:52 2020

@author: Sal
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SALT-geo", # Replace with your own username
    version="0.1",
    author='Salvatore G. Candela',
    author_email='Sal@OffToFindAdventure.com',
    description='Personal toolbox centered around geospatial processing',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitlab.com/Offtofindadventure/salt',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)