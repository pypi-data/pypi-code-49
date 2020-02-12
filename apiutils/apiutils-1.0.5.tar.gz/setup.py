#! /usr/bin/env python
# encoding: utf-8


"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))


EXCLUDE_FROM_PACKAGES = ['tests', ]

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = [l for l in f.read().splitlines() if l]

setup(
    name='apiutils',
    version='1.0.5',
    keywords='apiutils utils',
    description='apiutils',
    long_description=long_description,
    url='https://github.com/007gzs/apiutils',
    author='007gzs',
    author_email='007gzs@gmail.com',
    license='LGPL v3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: '
        'GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    install_requires=requirements,
    zip_safe=False,
    include_package_data=True,
    tests_require=[
        'pytest',
    ],
)
