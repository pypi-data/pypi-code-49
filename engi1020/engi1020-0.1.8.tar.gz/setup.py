# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="engi1020",
    version="0.1.8",
    description="Software library for Engineering 1020: Introduction to Programming at Memorial University.",
    license="MIT",
    author="Jonathan Anderson, Lori Hogan",
    packages=find_packages(),
    entry_points='''
        [console_scripts]
        arduino=engi1020.arduino.cli:cli
    ''',
    install_requires=[
        'click',
        'matplotlib',
        'nanpy',
    ],
    long_description=open("README.rst").read(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ]
)
