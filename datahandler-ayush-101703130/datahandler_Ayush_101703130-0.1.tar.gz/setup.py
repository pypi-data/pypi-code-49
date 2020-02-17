# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 19:49:25 2020

@author: Ayush130(101703130)
"""

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="datahandler_Ayush_101703130", # Replace with your own username
    version="0.1",
    author="Ayush/Ayush130",
    author_email="guptayush0022@gmail.com",
    description="Handling Missing values in a given data set and imputing them.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ayushgupta03/datahandler",
    download_url="https://github.com/Ayushgupta03/datahandler/archive/v_01.tar.gz",
    packages=["datahandler_Ayush_101703130"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
