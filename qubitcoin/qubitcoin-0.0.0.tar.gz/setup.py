# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:30:30 2018

@author: shane
"""

import os
import shutil
import sys

from setuptools import setup

# Old pip doesn't respect `python_requires'
if sys.version_info < (3, 6, 5):
    ver = ".".join([str(x) for x in sys.version_info[0:3]])
    print("ERROR: bitq requires Python 3.6.5 or later to install")
    print("HINT: You're running Python " + ver)
    exit(1)

# cd to parent dir of setup.py
os.chdir(os.path.dirname(os.path.abspath(__file__)))
shutil.rmtree("dist")

CLASSIFIERS = [
    "Intended Audience :: End Users/Desktop",
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]

REQUIREMENTS = []

README = open("README.rst").read()

PKG_NAME = "qubitcoin"

setup(
    name=PKG_NAME,
    author="gamesguru",
    author_email="mathmuncher11@gmail.com",
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    python_requires=">=3.6.5",
    packages=["qc"],
    entry_points={"console_scripts": ["qc=qc.__main__:main"]},
    description="P2P anonymous cryptocurrency protocol",
    long_description=README,
    long_description_content_type="text/x-rst",
    url="https://github.com/gamesguru/bitq",
    license="GPL v3",
    version="0.0.0",
)

# Clean up
shutil.rmtree(f"{PKG_NAME}.egg-info", True)
shutil.rmtree(f"__pycache__", True)
shutil.rmtree(f".pytest_cache", True)
