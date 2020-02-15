#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import find_packages, setup, Command


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-wa-e2e-plugin',
    version='0.1.2',
    author='Chaps SD',
    author_email='drumchaps@gmail.com',
    maintainer='Chaps SD',
    maintainer_email='drumchaps@gmail.com',
    license='MIT',
    url='https://github.com/chaps/pytest-wa-e2e-plugin',
    description='Pytest plugin for testing whatsapp bots with end to end tests   ',
    long_description=read('README.rst'),
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    install_requires=['pytest>=3.5.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'wa-e2e-plugin = pytest_wa_e2e_plugin',
        ],
    },
)
