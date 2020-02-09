# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:57:59 2020

@author: kamakshi_behl
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlier_kamakshi", # Replace with your own username
    version="0.0.1",
    author="kamakshi/kamakshi_behl",
    author_email="kamakshi.behl22@gmail.com",
    description="This is a package for outlier remover using row remover method.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kamakshibehl/outlier_kamakshi.git",
    download_url="https://github.com/kamakshibehl/outlier_kamakshi/archive/0.0.1.tar.gz",
    packages=["outlier_kamakshi"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
