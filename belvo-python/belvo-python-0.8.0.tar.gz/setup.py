#!/usr/bin/env python
from os import path

from setuptools import setup

from belvo import __version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "requirements/base.txt")) as f:
    requirements = f.read().splitlines()

setup(
    version=__version__,
    description="Belvo Python SDK",
    python_requires=">=3.6, <4",
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
)
