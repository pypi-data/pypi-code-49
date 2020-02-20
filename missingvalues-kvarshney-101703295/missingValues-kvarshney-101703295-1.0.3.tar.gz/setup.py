# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 16:06:07 2020

@author: Kunal Jindal
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="missingValues-kvarshney-101703295", 
    version="1.0.3",
    author="Kshitiz Varshney",
    author_email="kvarshney_be17@thapar.edu",
    description="A python package to handle Missing Values using SimpleImputer Class",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kv6737/missingValues",
    License="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=["missingValues_python"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={"console_scripts":["missingValues=missingValues_python.missingValues:main"]},    
)
