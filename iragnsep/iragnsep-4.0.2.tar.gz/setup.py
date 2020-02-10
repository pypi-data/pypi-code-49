#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iragnsep", # Replace with your own username
    version="4.0.2",
    author="Emmanuel Bernhard",
    author_email="manu.p.bernhard@gmail.com",
    description="Fits of IR SEDs including AGN contribution.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/ebernhard/iragnsep/src/master/",
    install_requires=['numpy', 'matplotlib', 'astropy', 'scipy', 'pandas', 'emcee', 'numba', 'tqdm'],
    packages=['iragnsep'],
    package_data={'iragnsep': ['Filters/*.csv', 'B18_full.csv']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

#install_requires=['emcee'],