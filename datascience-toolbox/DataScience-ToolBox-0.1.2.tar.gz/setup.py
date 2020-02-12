#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Data Science - ToolBox - A collection of Data Science helper functions for Lambda School
'''

import setuptools
import sys
import os


REQUIRED = [
    'numpy',
    'pandas',
    'spacy'
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    setuptools.setup(
    name="DataScience-ToolBox",
    version = "0.1.2",
    author = "Johann Augustine",
    description = "A set of python modules for machine learning and data mining",
    long_description = LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/DataLovecraft/DataScience-Tools",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires = REQUIRED,
    classifiers=["Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ]
    )
