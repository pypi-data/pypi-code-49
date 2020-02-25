# -*- coding: utf-8 -*-
"""
Created on Thu feb 20 16:06:07 2020

@author: Abhishek Sharma
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="outlier-asharma-3027", 
    version="1.1",
    author="Abhishek Sharma",
    author_email="asharma1_be17@thapar.edu",
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
