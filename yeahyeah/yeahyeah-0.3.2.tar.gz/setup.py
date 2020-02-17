#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'pyyaml', 'clockifyclient', 'python-dateutil',
                'lark-parser']

setup_requirements = ['pytest-runner']

test_requirements = ['pytest', 'click', 'clockifyclient', 'python-dateutil']

setup(
    author='Sjoerd Kerkstra',
    author_email='w.s.kerkstra@protonmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    description='Command line launch manager. Do things quick yeah yeah I know '
                'just do it come on move',
    entry_points={
        'console_scripts': ['yeahyeah=yeahyeah.cli:yeahyeah', 'jj=yeahyeah.cli:yeahyeah']
    },
    install_requires=requirements,
    license='MIT license',
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='yeahyeah',
    name='yeahyeah',
    packages=find_packages(include=['yeahyeah', 'yeahyeah_plugins*'], exclude=['*tests']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sjoerdk/yeahyeah',
    version='0.3.2',
    zip_safe=False,
)
