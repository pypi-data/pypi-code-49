""" Setup the package.

To install this in development mode:
    pip install --editable .
"""

import os
from setuptools import setup, find_packages

# ---------------------------------------------------------------------

# read the contents README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "holiday-oracle",
    version = "0.1.1",
    description = "Provides access to global holidays via the Off Chain Data API.",
    author = "Off Chain Data",
    author_email = "hello@offchaindata.com",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OffChainData/holiday-oracle-python",
    packages = find_packages(),
    install_requires = [
        "click==7.0",
        "pytest==5.3.5"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts = [ "bin/offchain" ]
)
