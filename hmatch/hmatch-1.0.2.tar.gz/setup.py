#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup for tiky."""

from setuptools import setup, find_packages


INSTALL_REQUIRES = [
   'colorama',
]

setup(
    name='hmatch',
    version='1.0.2',
    description='Match HTTP response.',
    long_description='Bulk check http response body/text for regex string.',
    license='Free License',
    author='Elis',
    author_email='me@elis.cc',
    url='https://elis.cc/',
    keywords='check, website, http, response, match, body, regex, https',
    install_requires=INSTALL_REQUIRES,
    include_package_data=True,
    zip_safe=False,
	packages=find_packages(),
    py_modules=['hmatch'],
    entry_points={'console_scripts': ['hmatch = hmatch:main']},
)