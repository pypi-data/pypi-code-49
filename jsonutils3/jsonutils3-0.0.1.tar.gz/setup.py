#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages

import jsonutils

setup(

    name='jsonutils3',

    version=jsonutils.__version__,

    packages=find_packages(),
    author="LavaPower",
    author_email="lavapower84@gmail.com",
    description="A lib to use json easly.",
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),

    include_package_data=True,

    url='http://github.com/LavaPower/jsonutils',

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
    ],
    install_requires=[]

 
)