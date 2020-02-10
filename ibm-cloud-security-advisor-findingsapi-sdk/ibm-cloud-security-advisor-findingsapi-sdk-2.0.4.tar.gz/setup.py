# coding: utf-8

"""
/*
 Copyright 2019 IBM Corp.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 */

"""

from setuptools import setup, find_packages  # noqa: H301


# read the contents of your README file
from os import path
import io

this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()



NAME = "ibm-cloud-security-advisor-findingsapi-sdk"
VERSION = "2.0.4"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "ibm_cloud_sdk_core>=0.2.0", "websocket-client==0.48.0"]

setup(
    name=NAME,
    version=VERSION,
    license='Apache 2.0',
    description="Findings API Client SDK",
    author='IBM Cloud',
    author_email='vkalangu@in.ibm.com, skairali@in.ibm.com, ashishth@in.ibm.com',
    url="https://github.com/ibm-cloud-security/security-advisor-findings-sdk-python",
    keywords=["Swagger", "Findings API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=long_description
)
