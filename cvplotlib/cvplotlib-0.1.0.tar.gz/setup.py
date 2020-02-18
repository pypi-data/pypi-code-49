#!/usr/bin/env python

import os
import pkg_resources
import sys

from pathlib import Path
from setuptools import setup, find_packages

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

pkg_name = "cvplotlib"

cwd = Path(__file__).parent.resolve()
# Get __version__ variable
exec(open(cwd / pkg_name / '_version.py').read())

setup(
    name=pkg_name,
    version=__version__,
    description='simple argparse wrapper with some syntactic sugar',
    author='Dimitri Korsch, Christoph Theiß',
    author_email='korschdima@gmail.com, theisz.cm@gmail.com',
    license='MIT License',
    packages=find_packages(),
    zip_safe=False,
    setup_requires=[],
    # no requirements yet
    # install_requires=install_requires,
    package_data={'': ['requirements.txt']},
    data_files=[('.', ['requirements.txt'])],
    include_package_data=True,
)
