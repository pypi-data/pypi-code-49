# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:36:18 2020

@author: kbansal_be17
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlier_processing",
    version="0.0.2",
    author="Keshav Bansal",
    author_email="keshavbansal509@gmail.com",
    description="Eliminate records with outliers using z score value",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    py_modules=["outlier_processing"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
