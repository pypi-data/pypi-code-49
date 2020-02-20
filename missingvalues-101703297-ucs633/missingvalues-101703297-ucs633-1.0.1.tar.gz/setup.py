# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:06:07 2020

@author: Kunal Bajaj
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="missingvalues-101703297-ucs633", 
    version="1.0.1",
    author="Kunal Bajaj",
    author_email="kbajaj_be17@thapar.edu",
    description="A python package to handle Missing Values using SimpleImputer Class",
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
    packages=["missingvalues"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={"console_scripts":["missingvalues-101703297=missingvalues.missingValues:main"]},    
)
