# This file is needed by Python's setuptools for local installation from the pypi.org index (pip install linalg_simple)

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="linalg_simple",
    version="0.0.3",
    author="Thomas Grusz",
    author_email="thomas.grusz@gmail.com",
    description="Simple Linear Algebra Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thomasgrusz/linalg_pkg",
    packages=["linalg"],
    python_requires=">=3.6",
    zip_safe=False,
)
