#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from distutils.core import setup

# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

def get_s4d_version():
    with open('s4d/__init__.py') as f:
        s = [l.rstrip() for l in f.readlines()]
        version = None
        for l in s:
            if '__version__' in l:
                version = l.split('=')[-1]
        if version is None:
            raise RuntimeError('Can not detect version from s4d/__init__.py')
        return eval(version)

setup(
    name='s4d',
    version=get_s4d_version(),
    author='Sylvain MEIGNIER',
    author_email='s4d@univ-lemans.fr',
    packages=['s4d', 's4d.alien', 's4d.clustering', 's4d.gui'],
    url='https://projets-lium.univ-lemans.fr/s4d/',
    download_url='http://pypi.python.org/pypi/s4d/',
    license='LGPL',
    platforms=['Linux, Windows', 'MacOS'],
    description='S4D: SIDEKIT for Diarization',
    long_description=open('README.txt').read(),
    install_requires=[
        "mock>=1.0.1",
        "nose>=1.3.4",
        "numpy>=1.13.3",
        "pyparsing >= 2.0.2",
        "python-dateutil >= 2.2",
        "scipy>=0.19.0",
        "six>=1.11.0",
        "matplotlib>=2.0.2",
        "torch >= 1.0",
        "torchvision",
        "PyYAML>=3.11",
        "h5py>=2.5.0",
        "pandas>=0.21.1",
        "PyAudio>=0.2.11",
        "bottleneck>=1.3.1",
        "setuptools>=38.5.2",
        "sidekit>=1.3.6.5",
        "scikit_learn>=0.22",
        "sortedcontainers>=1.5.9"
    ],
    package_data={'s4d': ['docs/*']},
    classifiers=[        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Scientific/Engineering",
        ]
)




