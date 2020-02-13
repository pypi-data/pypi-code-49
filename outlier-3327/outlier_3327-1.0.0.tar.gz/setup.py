# -*- coding: utf-8 -*-
from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="outlier_3327",
    version="1.0.0",
    description="'OUTLIER ROW REMOVAL PACKAGE'",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="",
    author="Manjot khaira",
    author_email="khairamanjot2@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["out"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "outlier_3327==out.outlier:main",
        ]
    },
)
