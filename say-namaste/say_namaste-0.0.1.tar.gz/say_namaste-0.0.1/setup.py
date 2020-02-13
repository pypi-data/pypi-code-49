# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:29:45 2020

@author: kbansal_be17
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="say_namaste", # Replace with your own username
    version="0.0.1",
    author="Keshav Bansal",
    author_email="keshavbansal509@gmail.com",
    description="Hello!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
