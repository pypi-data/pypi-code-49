#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Poezio OMEMO plugin
    Copyright (C) 2019 Maxime “pep” Buquet <pep@bouah.net>
    This file is part of poezio-omemo.

    See the file LICENSE for copying permission.
"""

import os
from typing import Any, Dict
from setuptools import setup


MODULE_FILE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'poezio_omemo', 'version.py'
)

def get_version() -> str:
    """Returns version by looking at poezio_version/version.py"""

    version: Dict[str, Any] = {}
    with open(MODULE_FILE_PATH) as file:
        exec(file.read(), version)

    if '__version__' in version:
        return version['__version__']
    return 'missingno'


DESCRIPTION = ('Poezio OMEMO plugin')
VERSION = get_version()
with open('README.rst', encoding='utf8') as readme:
    LONG_DESCRIPTION = readme.read()

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Topic :: Internet :: XMPP',
    'Topic :: Security :: Cryptography',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name="poezio-omemo",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    author='Maxime Buquet',
    author_email='pep@bouah.net',
    url='https://lab.louiz.org/poezio/poezio-omemo',
    license='GPLv3',
    platforms=['any'],
    packages=['poezio_omemo'],
    entry_points={'poezio_plugins': 'omemo = poezio_omemo'},
    install_requires=['poezio', 'slixmpp-omemo'],
    classifiers=CLASSIFIERS,
)
