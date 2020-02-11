#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-alphamoon',
    version='0.1.9',
    author='Jakub Binkowski',
    author_email='jakub.binkowski@alphamoon.ai',
    maintainer='Jakub Binkowski',
    maintainer_email='dev@alphamoon.ai, jakub.binkowski@alphamoon.ai',
    license='MIT',
    url='https://gitlab.com/alphamoon/internal_tools/pytest_alphamoon',
    description='Static code checks used at Alphamoon',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    py_modules=['pytest_alphamoon'],
    python_requires='>=3.6',
    install_requires=['pytest>=3.5.0'],
    packages=['pytest_alphamoon'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'init_check = pytest_alphamoon.init_check',
            'import_check = pytest_alphamoon.import_check',
            'notebook_check = pytest_alphamoon.notebook_check'
        ],
    },
)
