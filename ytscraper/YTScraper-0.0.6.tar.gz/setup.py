# Copyright (c) 2020 Finbarrs Oketunji
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
#
# Created ~/.pypirc File With The Following Contents:
#
# [distutils]
# index-servers =
#   pypi

# [pypi]
# repository: https://pypi.python.org/pypi
# username: <username>
# password: <pass>
#
# python3 setup.py sdist bdist_wheel
# python3 setup.py sdist upload

import sys
from setuptools import setup, find_packages
from distutils.core import Extension

version = '0.0.6'

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst')) as f:
    long_description = f.read()

macros = []
if sys.platform.startswith('freebsd') or sys.platform == 'darwin':
    macros.append(('PLATFORM_BSD', '1'))
elif 'linux' in sys.platform:
    macros.append(('_GNU_SOURCE', ''))

setup(
    name="YTScraper",
    version=version,
    description="A command-line tool for downloading .torrent files from YTS.",
    long_description=long_description,
    author="Finbarrs Oketunji",
    author_email="oketunjifinbarrs@gmail.com",
    packages=find_packages(),
    install_requires=['requests', 'argparse', 'tqdm', 'fake-useragent'],
    entry_points={'console_scripts': 'ytscraper = yts.main:main'},
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: DFSG approved',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='yts yify scraper media download downloader torrent',
    license='MIT',
)