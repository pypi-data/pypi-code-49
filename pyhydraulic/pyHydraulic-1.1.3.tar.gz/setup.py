#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read()

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Bruce Lee",
    author_email='lee@njit.edu.cn',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="pyHydraulic using PyQt5",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pyHydraulic',
    name='pyHydraulic',
    #packages=find_packages(include=['_template']),
    packages=find_packages(include=['pyHydraulic*'], exclude=['tests*']),
    package_data={'': ['qss/*']},
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/nanjing-institute-of-technology/pyHydraulic.git',
    version='1.1.03',
    zip_safe=False,
)
