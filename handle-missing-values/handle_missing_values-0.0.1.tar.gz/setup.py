# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:40:32 2020

@author: Keshav Bansal
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="handle_missing_values",
    version="0.0.1",
    author="Keshav Bansal",
    author_email="keshavbansal509@gmail.com",
    description="Handle missing values in a csv file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    py_modules=["handle_missing_values"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
