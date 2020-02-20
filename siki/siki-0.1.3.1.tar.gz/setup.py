#!/usr/bin/evn python
#coding=utf-8

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="siki",
    version="0.1.3.1",
    author="Orlando Chen",
    author_email="seagochen@hotmail.com",
    description="A collection of tools that may be used to help users coding with Python in an easy way",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seagochen/Siki",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
