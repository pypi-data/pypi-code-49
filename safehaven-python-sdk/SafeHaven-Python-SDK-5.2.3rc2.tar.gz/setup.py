#!/usr/bin/env python
#
# Installer Script for SafeHaven Python SDK
#
from __future__ import print_function, absolute_import, unicode_literals
import io
import os
from setuptools import setup, find_packages

# Read in version file
with io.open('dgpy/version.py', 'rt') as fd:
    code = compile(fd.read(), 'dgpy/version.py', 'exec')
    exec(code)

# Use README.rst as long description
with io.open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'rt') as readme:
    long_description = readme.read()

setup(
    name="SafeHaven-Python-SDK",
    description='SafeHaven Python SDK',
    long_description=long_description,
    keywords="SafeHaven DRaaS Disaster Recovery CAM AWS CLC Azure",
    classifiers=[ # See https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
    ],
    install_requires=['grpcio', 'grpcio-tools', 'PyYAML', 'future', 'configparser', 'wrapt'],
    packages=find_packages(),
    package_data=dict(dgpy=['test_commands/*.py', 'test_commands/example_configurations/*']),
    license='Apache License 2.0',
    zip_safe=True,

    # The following fields are similar to the information in the .deb package:
    version=__version__, # Set in version file
    author='CenturyLink',
    author_email='help@ctl.io',
    url='https://github.com/CenturyLinkCloud/PublicKB/tree/master/Disaster%20Recovery',
)
