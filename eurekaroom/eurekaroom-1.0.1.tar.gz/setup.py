#!/usr/bin/env python
# -*- coding: utf-8 -*-

# For a fully annotated version of this file and what it does, see
# https://github.com/pypa/sampleproject/blob/master/setup.py

import io
import os
from setuptools import find_packages, setup

EXCLUDE_FROM_PACKAGES = ["contrib", "docs", "tests*"]
CURDIR = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(CURDIR, "requirements.txt"), "r", encoding="utf-8") as file:
    DEPENDENCIES  = file.read().splitlines()
    DEPENDENCIES = DEPENDENCIES[1:]

with io.open(os.path.join(CURDIR, "README.md"), "r", encoding="utf-8") as f:
    README = f.read()

setup(
    name="eurekaroom",
    # Get the version from the most recent git tag
    #use_scm_version=True,
    #setup_requires=['setuptools_scm'],
    version = "1.0.1",
    author="Daniel Eguia",
    author_email="eguiamotion@gmail.com",
    description="A command-processor and RESTful server for use in escapenodes on RaspberryPi systems.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/growlf/eurekaroom.git",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    keywords=[],
    scripts=['bin/ecmd'],
    entry_points={},#"console_scripts": ["eurekaroom=eurekaroom.main:main"]},
    zip_safe=False,
    install_requires=DEPENDENCIES,
    test_suite="tests.test_project",
    python_requires=">=3.0.0",
    # license and classifier list:
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    license="License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
    ]
)