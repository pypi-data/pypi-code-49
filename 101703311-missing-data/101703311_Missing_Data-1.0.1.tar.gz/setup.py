# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20  2020

@author: Lokesh Arora

"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="101703311_Missing_Data", 
    version="1.0.1",
    author="Lokesh Arora",
    author_email="3lokesharora@gmail.com ",
    description="A python package for handling the missing data from the dataset",
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
    packages=["data"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={"console_scripts":["handledata=data.handledata:main"]},    
)
