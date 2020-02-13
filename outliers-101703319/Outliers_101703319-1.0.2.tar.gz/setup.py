

#############################
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 16:06:07 2020

@author: Manav Kumar`
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Outliers_101703319", 
    version="1.0.2",
    author="Manav Kumar",
    author_email="manav1811kumar@gmail.com",
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
    packages=["Outliers"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={"console_scripts":["Outliers_file=Outliers.Outliers_file:main"]},    
)
