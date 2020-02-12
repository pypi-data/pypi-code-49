#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

__author__ = 'Colin Bitterfield'

import io
import pip

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

from setuptools import setup, find_packages

PACKAGE_NAME = 'mkpreview'
DESCRIPTION = 'mkpreview creates previews from movie files '\
              'Support for all FFMPEG video types.'


def read(*filenames, **kwargs):
    """Gets file content"""
    encoding = kwargs.get("encoding", "utf-8")
    sep = kwargs.get("sep", "\n")
    buf = list()
    for filename in filenames:
        with io.open(filename, encoding=encoding) as open_file:
            buf.append(open_file.read())
    return sep.join(buf)


def get_parsed_req(req_file):
    """Gets requirement from file"""
    parsed_req = parse_requirements(req_file, session=False)
    return (str(ir.req) for ir in parsed_req)


REQUIREMENTS = get_parsed_req('requirements/prod.txt')
TEST_REQUIREMENTS = get_parsed_req('requirements/test.txt')
SETUP_REQUIREMENTS = ['pytest-runner==4.2']


setup(
    python_requires='>=3.5',
    name=PACKAGE_NAME,
    version='0.4.3',
    author='Colin Bitterfield',
    author_email='colin@bitterfield.com',
    description=DESCRIPTION,
    long_description=read('README.rst') + '\n\n' + read('CHANGELOG.rst'),
    keywords='',
    packages=find_packages(include=[PACKAGE_NAME], exclude='tests'),
    entry_points={
        'console_scripts': [
            'mkpreview = mkpreview.mkpreview:main'
        ]
    },
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    include_package_data=True,
    setup_requires=SETUP_REQUIREMENTS,
    test_suite='tests',
    url='https://github.com/cbitterfield/mkpreview.git',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Environment :: Console',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
    ],

    license="MIT license",

)
