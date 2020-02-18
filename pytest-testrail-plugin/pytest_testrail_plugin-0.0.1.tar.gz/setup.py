#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup


def get_long_description():
    with open("README.md", encoding="utf8") as f:
        return f.read()


def get_packages(package):
    return [
        dirpath
        for dirpath, dirnames, filenames in os.walk(package)
        if os.path.exists(os.path.join(dirpath, "__init__.py"))
    ]


setup(
    name='pytest_testrail_plugin',
    version='0.0.1',
    author='Max Ponomarev',
    author_email='maxim.ponomarev@cashwagon.com',
    url='https://git.cashwagon.com/billing/pytest-testrail-plugin',
    python_requires=">=3.7",
    install_requires=[
        'pytest',
        'requests>=2.20.0, <3',
        'PyYAML>=5.3, <6'
    ],
    license="BSD",
    description="PyTest plugin for TestRail",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    packages=get_packages('pytest_testrail_plugin'),
    include_package_data=True,
    data_files=[("", [])],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Programming Language :: Python :: 3.7",
    ],
    zip_safe=False,
    entry_points={'pytest11': ['pytest-testrail-plugin = pytest_testrail_plugin.conftest']}
)
