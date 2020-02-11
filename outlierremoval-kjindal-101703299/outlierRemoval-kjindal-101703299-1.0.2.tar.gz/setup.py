# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:06:07 2020

@author: Kunal Jindal
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlierRemoval-kjindal-101703299", 
    version="1.0.2",
    author="Kunal Jindal",
    author_email="kjindal_be17@thapar.edu",
    description="A python package for removing outliers from a dataset using InterQuartile Range (IQR)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    License="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=["outlierRemoval_python"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={"console_scripts":["outlierRemoval=outlierRemoval_python.outlierRemoval:main"]},    
)
