# -*- coding: utf-8 -*-
"""
Author: Amir Mofakhar <amir@mofakhar.info>
Date created: 2019-02-14
"""

import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name = 'execution_asserts',
    version = '0.0.3',
    author = 'Amir Mofakhar',
    author_email = 'amir@mofakhar.info',
    description = 'A collection of asserts for methods execution',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/pangan/execution_asserts',
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=['memory_profiler']

)
