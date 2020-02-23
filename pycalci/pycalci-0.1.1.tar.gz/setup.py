
#!/usr/bin/python

from setuptools import find_packages


import os
from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="pycalci",
    version="0.1.1",
    author="Mugdha Dalal",
    author_email="mugdhadalal@gmail.com",
    url="https://github.com/mugdhadalal/pycalci",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
    ],
    install_requires=['fire>=0.1.1'],
    entry_points={"console_scripts": ["pycalci=pycalci:main"]},
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["pycalci"]),
)

