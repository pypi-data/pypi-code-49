#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name="name_prettier",
    version="0.1",
    packages=find_packages(),
    package_data={
        "": ["*.json"]
    }
)
