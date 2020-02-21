#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 'chibi>=0.5.5', 'requests>=2.22.0', 'marshmallow==3.4.0' ]

setup(
    author="Dem4ply",
    author_email='dem4ply@gmail.com',
    python_requires='>=3.0',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="handle urls in a more easy and human way",
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='chibi_requests',
    name='chibi_requests',
    packages=find_packages(include=['chibi_requests', 'chibi_requests.*']),
    url='https://github.com/dem4ply/chibi_requests',
    version='0.3.0',
    zip_safe=False,
)
