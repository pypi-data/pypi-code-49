#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Package setup."""
import codecs
import os

from setuptools import find_packages, setup

PROJECT = "axonius_api_client"
SHELL_CMD = "axonshell"
HERE = os.path.abspath(os.path.dirname(__file__))
VERSION_PATH = os.path.join(HERE, PROJECT, "version.py")


ABOUT = {}
with codecs.open(VERSION_PATH, "r", "utf-8") as fh:
    CONTENTS = "\n".join(a for a in fh.readlines() if not a.startswith("#"))
    exec(CONTENTS, ABOUT)


with codecs.open("README.md", "r", "utf-8") as f:
    README = f.read()


setup(
    name=ABOUT["__title__"],
    version=ABOUT["__version__"],
    description=ABOUT["__description__"],
    long_description=README,
    long_description_content_type="text/markdown",
    author=ABOUT["__author__"],
    author_email=ABOUT["__author_email__"],
    url=ABOUT["__url__"],
    packages=find_packages(),
    package_data={"": ["LICENSE"]},
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=[
        "requests[security,socks]",
        "click",
        "python-dotenv",
        "python-dateutil",
        'pyreadline ; platform_system == "Windows"',
        "pathlib2 ; python_version < '3.0'",
        "tabulate",
        "six>=1.14.0",
    ],
    keywords=["Axonius", "API Library"],
    tests_require=["pytest", "pytest-cov", "pytest-httpbin", "coverage"],
    license=ABOUT["__license__"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={"console_scripts": ["{}={}.cli:cli".format(SHELL_CMD, PROJECT)]},
)
