# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 19:49:25 2020

@author: eternal_demon
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datahandler_bhanu", # Replace with your own username
    version="0.1",
    author="Bhanu/eternal_demon",
    author_email="aggarwal.bhanu02@gmail.com",
    description="Handling Missing values in a given data set and imputing them.",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/eternaldemon/datahandler",
    download_url="https://github.com/eternaldemon/datahandler/archive/0.1.tar.gz",
    packages=["datahandler_bhanu"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
