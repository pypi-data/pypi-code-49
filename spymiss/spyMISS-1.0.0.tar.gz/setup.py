# -*- coding: utf-8 -*-
from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="spyMISS",
    version="1.0.0",
    description="'Missing values'",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/manavsharma136",
    author="Manav Sharma",
    author_email="manavsharma136@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["missing"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "spyMISS=missing.MissingData:main",
        ]
    },
)
