# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 

@author: ashu
"""
#Made by Ashutosh Gupta 101703118
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AshutoshGupta_101703118_Outlier_removal",
    version="0.0.2",
    author="Ashutosh Gupta",
    author_email="agupta12_be17@thapar.edu",
    description="A small example package for removal of outliers in the given dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ashutosh2539/Outliers_removal",
    download_url="https://github.com/ashutosh2539/Outliers_removal.git",
    keywords = ['command-line', 'Outliers', 'outlier-removal','row-removal'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
