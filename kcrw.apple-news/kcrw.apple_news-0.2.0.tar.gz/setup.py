#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

###################################################################

KEYWORDS = ['Apple News', 'REST API', 'KCRW']
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
]

###################################################################


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['requests[security]', 'six', 'Click', 'click-log', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    name="kcrw.apple_news",
    author="Alec Mitchell",
    author_email="alecpm@gmail.com",
    version="0.2.0",
    description="Library for using the Apple News API",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/x-rst",
    license="MIT license",
    url="https://github.com/KCRW-org/kcrw.apple_news",
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    install_requires=requirements,
    include_package_data=True,
    packages=find_packages(include=['kcrw.apple_news']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False,
    entry_points='''
        [console_scripts]
        apple_news_api=kcrw.apple_news.command:cli
    '''
)
