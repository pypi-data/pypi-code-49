#!/usr/bin/env python
# -*- coding: utf-8 -*-

# For a fully annotated version of this file and what it does, see
# https://github.com/pypa/sampleproject/blob/master/setup.py

# To upload this file to PyPI you must build it then upload it:
# python setup.py sdist bdist_wheel  # build in 'dist' folder
# python -m twine upload dist/*  # 'twine' must be installed: 'pip install twine'

import ast
import io
import re
import os
from setuptools import find_packages, setup

EXCLUDE_FROM_PACKAGES = ["contrib", "docs", "tests*"]
CURDIR = os.path.abspath(os.path.dirname(__file__))

####! Run `pipenv lock --requirements > requirements.txt` prior to running setup.py
####TODO: put `pipenv lock --requirements > requirements.txt` in the makefile
with io.open(os.path.join(CURDIR, "requirements.txt"), "r", encoding="utf-8") as file:
    DEPENDENCIES  = file.read().splitlines()
    DEPENDENCIES = DEPENDENCIES[1:]

with io.open(os.path.join(CURDIR, "README.md"), "r", encoding="utf-8") as f:
    README = f.read()

def get_version():
    main_file = os.path.join(CURDIR, "bin", "ecmd")
    _version_re = re.compile(r"__version__\s+=\s+(?P<version>.*)")
    with io.open(main_file, "r", encoding="utf8") as f:
        match = _version_re.search(f.read())
        version = match.group("version") if match is not None else '"UNKNOWN"'
    return str(ast.literal_eval(version))


setup(
    name="eurekaroom",
    version=get_version(),
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
    ],
)