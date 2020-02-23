"""Installing intructions for misc_tools package.

Intended to be used within a Python 3 environment.
Developed by Rodrigo Rivero.
https://github.com/rodrigo1392

"""

import os

import setuptools
from pathlib import Path


root = Path(__file__).parent
os.chdir(str(root))


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

with open("requirements.txt") as f:
    INSTALL_REQUIRES = [i.strip('\n') for i in f.readlines()]

setuptools.setup(
    name="pymiscell",
    version="0.0.1",
    author="Rodrigo Rivero",
    author_email="rodrigo.m.rivero13@gmail.com",
    description="A package with miscellaneous, common use tools",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/rodrigo1392/pymiscell",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
                ],
    python_requires='>=3.6',
    install_requires=INSTALL_REQUIRES,
    )
