# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:42:57 2020

"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Missing_Values_101703122", 
    version="0.09",
    author="Avani Agarwal",
    author_email="avaniagarwal1999@gmail.com",
    description="To Handle missing values in a dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Avani-Agarwal1999/Missing_Values_101703122.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['Missing_Value=Missing_Values_101703122.Missing_Values_101703122:main'],
    },
    python_requires='>=3.6',
)
