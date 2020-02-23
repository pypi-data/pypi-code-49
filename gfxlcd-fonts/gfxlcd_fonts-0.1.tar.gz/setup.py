# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as file_handler:
        return file_handler.read()

setup(
    name='gfxlcd_fonts',
    version='0.1',
    description='',
    keywords=['gfxlcd', 'cili'],
    long_description=(read('readme.md')),
    license='MIT',
    author='Bartosz Kościów',
    author_email='kosci1@gmail.com',
    py_modules=['gfxlcd_fonts'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',

    ],
    packages=find_packages(exclude=['tests*']),
)
