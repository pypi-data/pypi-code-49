# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 

@author: ashu
"""
#Made by Ashutosh Gupta 101703118
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AshutoshGupta_101703118_Fill_Missing_Values",
    version="0.0.1",
    author="Ashutosh Gupta",
    author_email="agupta12_be17@thapar.edu",
    description="A small package for filling missing values in the given dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords = ['command-line', 'Missing values', 'missing-values'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)
