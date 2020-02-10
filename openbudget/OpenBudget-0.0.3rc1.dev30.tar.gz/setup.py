#!/usr/bin/env python
# coding: utf-8

# Simple budget management planner
# Copyright (C) 2019 Yapbreak
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""
Package definition of OpenBudget
"""
from setuptools import setup
import openbudget


VERSION = openbudget.__version__

with open('README.rst') as readme_file:
    README = readme_file.read()

with open('requirements/prod.txt') as prod_file:
    REQUIREMENTS = prod_file.readlines()

SETUP_REQUIREMENTS = [
    'pytest-runner',
]

TEST_REQUIREMENTS = [
    'pytest'
]

setup(
    name='OpenBudget',
    version=VERSION,
    description='Simple budget management planner',
    long_description=README,
    author='Yapbreak',
    author_email='yapbreak@yapbreak.fr',
    url='https://gitlab.yapbreak.fr/olivaa/openbudget',
    packages=[
        'openbudget',
    ],
    package_dir={'openbudget': 'openbudget'},
    entry_points={
        'console_scripts': [
            'openbudget = openbudget.__main__:main',
        ]
    },
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=REQUIREMENTS,
    license='GNU/GPL v3',
    zip_safe=False,
    classifiers=[
        # Look at https://pypi.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords=(
        'openbudget'
    ),
    setup_requires=SETUP_REQUIREMENTS,
    test_suite='tests',
    test_requires=TEST_REQUIREMENTS,
)
