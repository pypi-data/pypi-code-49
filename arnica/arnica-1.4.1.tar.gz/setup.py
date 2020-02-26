#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='arnica',
    version='1.4.1',
    description='Open Source library CFD toolkit',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='CoopTeam-CERFACS',
    author_email='coop@cerfacs.com',
    url='',
    keywords=["ARNICA"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    license="CeCILL-B FREE SOFTWARE LICENSE AGREEMENT",
    packages=find_packages(exclude=('tests', 'docs')),
    setup_requires=['pytest-runner'],
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'mplcursors',
        'pandas',
        'h5py',
        'PyYAML>=3.13',
        'lxml',
        'pandas']
)
