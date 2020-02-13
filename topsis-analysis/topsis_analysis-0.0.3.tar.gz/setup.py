# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:36:42 2020

@author: kbansal_be17
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="topsis_analysis", # Replace with your own username
    version="0.0.3",
    author="Keshav Bansal",
    author_email="keshavbansal509@gmail.com",
    description="topsis analysis of csv file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    py_modules=["topsis_analysis"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
