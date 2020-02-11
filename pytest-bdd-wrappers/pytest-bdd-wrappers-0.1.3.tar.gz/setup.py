#!/usr/bin/env python
import os

from setuptools import setup
from setuptools import find_packages


def path_in_project(*path):
    return os.path.join(os.path.dirname(__file__), *path)


setup(
    version="0.1.3",
    install_requires=[
        'pytest<5;python_version<"3.5"',
        'pytest;python_version>="3.4"',
        "pytest-bdd",
    ],
    tests_require=["mock"],
    python_requires=">=2.7",
    packages=find_packages(
        include=path_in_project('istock*'),
        exclude=['tests*'],
    ),
    entry_points={
        "pytest11": [
            "pytest_bdd_wrappers = pytest_bdd_wrappers.plugin",
        ]
    },
)
