#!/usr/bin/env python

import setuptools
import testgithook

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testgithook",
    version=testgithook.__version__,
    author="Stefan Helmert",
    author_email="info@entroserv.de",
    description="only testing python automatic versioning and deployment",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.entroserv.de/",
    packages=setuptools.find_packages(),
    include_package_data=False,
    install_requires=[
    ],
    license = 'https://www.fsf.org/licensing/licenses/agpl-3.0.html',
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
)

