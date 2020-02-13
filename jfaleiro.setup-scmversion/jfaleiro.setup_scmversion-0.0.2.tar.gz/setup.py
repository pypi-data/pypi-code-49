#!/usr/bin/env python
#
#  setup_scmversion - Builds a pythonic version number sbased on scm tags and branches.
#
#  Copyright (C) 2019 Jorge M. Faleiro Jr.
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import pathlib

from setuptools import find_packages, setup

import setup_scmversion

tests_require = [
    'pytest',
    'pytest-cov',
    'PyHamcrest',
    'coverage',
    'mock',
    'behave',
]

setup_requires = [
    'setupext_janitor',
    'coverage',
]

setup(
    name='jfaleiro.setup_scmversion',
    version=setup_scmversion.__version__,
    description='Builds a pythonic version number based on scm tags and branches',
    long_description=(pathlib.Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    author='Jorge M. Faleiro Jr.',
    author_email='j@falei.ro',
    url='https://gitlab.com/jfaleiro/setup_scmversion',
    license="Affero GPL, see LICENSE for details",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'scmversion=setup_scmversion:main',
        ],
    },
    py_modules=[
        'setup_scmversion',
    ],
    tests_require=tests_require,
    setup_requires=setup_requires,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
