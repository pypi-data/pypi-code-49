#!/usr/bin/env python
import io
import re

# Always prefer setuptools over distutils
from setuptools import setup

# To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name='daab',
    version='0.1.0',
    description='DNS as a database.',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Justin Duch',
    author_email='justin@justinduch.com',
    url='https://github.com/beanpuppy/dns-as-a-database',
    keywords="database dns",
    py_modules=['daab'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'digitalocean==1.15.0'
    ],
    test_suite='tests',
    license='MIT'
)
