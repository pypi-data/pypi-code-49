# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "aspose-cells"
VERSION = "19.12.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["JPype1 >= 0.7.0"]

setup(
    name=NAME,
    version=VERSION,
    description="Python API to read, write, manipulate & convert Microsoft Excel® files without any dependency. Create & manipulate Workbooks, Worksheets, Pivot Tables, Charts, Sparklines, Conditional Formatting & more. Convert Excel to PDF, XPS, HTML, images & metafiles.",
    author="Aspose",
    author_email="cells@aspose.com",
    url="https://products.aspose.com/cells/python-java",
    keywords=["Excel API", "Spreadsheet API", "aspose", "cells", "java"],
    install_requires=REQUIRES,
    packages=['asposecells'],
    include_package_data=True,
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'License :: Other/Proprietary License'
    ],
    platforms=[
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows Vista',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.5',
)
