# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 19:49:25 2020

@author: atishay_123(101703121)
"""

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="datahandler_Atishay_101703121", # Replace with your own username
    version="0.1",
    author="atishay_123",
    author_email="atishay21@gmail.com",
    description="Handling Missing values in a given data set and imputing them.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["datahandler_Atishay_101703121"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
