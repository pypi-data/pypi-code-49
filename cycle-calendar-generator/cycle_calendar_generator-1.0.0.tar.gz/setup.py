#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['openpyxl', 'ics']

setup_requirements = [ ]

test_requirements = ['pyfakefs']

setup(
    author="Ryan William Maynard Oldford",
    author_email='ryan.oldford@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Generates iCal files for class schedules for schools using an N-day cycle",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='cycle_calendar_generator',
    name='cycle_calendar_generator',
    packages=find_packages(include=['cycle_calendar_generator']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ROldford/cycle_calendar_generator',
    version='1.0.0',
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'cycle_calendar_generator = cycle_calendar_generator.__main__:main'
        ]
    }
)
