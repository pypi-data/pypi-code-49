# -*- coding: utf-8 -*-
"""
Created on Sun Feb 09 19:49:25 2020

@author: ashwin_menon
"""
#Made by Ashwin Menon 101703120
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fill_missing_values_ashwin", # Replace with your own username
    version="0.0.3",
    author="ashwin_menon",
    author_email="ashwin.s.menon1999@gmail.com",
    description="A small package for filling missing values in the given dataset",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/ash-1999/fill_missing_values_ashwin",
    download_url="https://github.com/ash-1999/fill_missing_values_ashwin/archive/0.0.3.tar.gz",
    packages=["fill_missing_values_ashwin"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)