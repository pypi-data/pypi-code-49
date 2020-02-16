# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:42:57 2020

@author: Arpit Singla
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Missing_values_101703112", 
    version="0.09",
    author="Ashi Kothari",
    author_email="ashikothari10@gmail.com",
    description="Python Package to find missing values in a dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AshiKothari/Missing_values",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['Missing_Value=Missing_Values_101703112.Missing_Values_101703112:main'],
    },
    python_requires='>=3.6',
)
