#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


def get_version():
    with open("fattureincloud/__init__.py") as f:
        for line in f:
            if line.startswith("__version__"):
                return eval(line.split("=")[-1])


with open("README.md", "r") as readme_file:
    readme = readme_file.read()

setup(
    name="fattureincloud",
    version=get_version(),
    description="Fatture In Cloud API SDK",
    long_description=readme,
    author="Federico Torresan",
    author_email="federico.torresan@quentral.com",
    license="LGPLv3",
    url="https://github.com/fedetorre/python-fattureincloud",
    packages=find_packages(),
    install_requires=["requests>=2.22.0"],
    python_requires=">=3.6.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    extras_require={},
)