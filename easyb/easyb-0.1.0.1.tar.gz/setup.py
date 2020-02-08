#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
#    Copyright (C) 2019, Kai Raphahn <kai.raphahn@laburec.de>
#

from setuptools import setup, find_packages
import easyb

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = find_packages(where=".", exclude=["tests", "tests.console", "tests.data", "tests.device"])

setup(
    name=easyb.__name__,
    license=easyb.__license__,
    version=easyb.__version__,
    description=easyb.__description__,
    author=easyb.__author__,
    author_email=easyb.__email__,
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    scripts=[
        'easyb-tool.py',
    ],
    url='https://github.com/TheUncleKai/pyeasyb',
    packages=packages,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Other/Nonlisted Topic',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        'colorama',
        "pyserial"
    ]
)
