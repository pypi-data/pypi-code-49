#!/usr/bin/env python
"""Create setup script for pip installation of python_utils"""
########################################################################
# File: setup.py
#  executable: setup.py
#
# Author: Andrew Bailey
# History: 12/09/17 Created
########################################################################

import sys
from os import path
from setuptools import setup, find_packages, dist

here = path.abspath(path.dirname(__file__))
# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="py3helpers",
    version='0.3.8',
    description='Python utility functions',
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/adbailey4/python_utils',
    author='Andrew Bailey',
    license='MIT',
    author_email='andbaile@ucsc.com',
    packages=find_packages(),
    extras_require={'seq_tools': ['Cython>=0.29.12', 'pysam>=0.15', 'biopython>=1.73', 'mappy>=2.16']},
    scripts=["py3helpers/bin/merge_methyl_bed_files.py"],
    install_requires=[
        'numpy>=1.14.2',
        'pandas>=0.23.4',
        'scikit-learn>=0.19.0',
        'matplotlib>=2.0.2',
        'boto3>=1.9'],
    python_requires='>=3.6',
    zip_safe=True,
    test_suite='tests',
    keywords='utility utils py3helpers',
)


