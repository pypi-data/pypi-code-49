# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:56:10 2020

@author: HP
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsis-ashita_khurana", # Replace with your own username
    version="0.0.1",
    author=" Author: Ashita",
    author_email="ashitakhurana99@gmail.com",
    description="An topsis aproach",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)