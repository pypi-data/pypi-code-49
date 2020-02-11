#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['beautifultable', 'tzlocal', 'pandas']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Philippe Pariseau",
    author_email='phil.pariseau@gmail.com',
    python_requires='>=3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Shortwave CLI tools for SWLing and DXing!",
    entry_points={
        'console_scripts': [
            'swlookup=swtools.swlookup:main',
            'swling=swtools.swling:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    exclude_package_data={'': ['*.csv']},
    package_data={'': ['data/shortwave.sqlite3']},
    keywords='swtools',
    name='swtools',
    packages=find_packages(include=['swtools', 'swtools.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://gitlab.com/pparise/swtools',
    version='1.0.0',
    zip_safe=False,
)
