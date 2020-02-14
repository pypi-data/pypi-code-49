#!/usr/bin/env python

from __future__ import absolute_import, print_function

import os
import os.path
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

NAME = "libtridens"

PACKAGE_DATA = {'': [
                     'LICENSE.txt',
                     'pasteurize.py',
                     ],
                'tests': ['*.py'],
                }

VERSION = "0.0.1"
DESCRIPTION = "`future` fork that allows you to compile `ipy`-compatible code"
AUTHOR = "Ed Schofield"
AUTHOR_EMAIL = "ed@pythoncharmers.com"
FORK_AUTHOR = "kjczarne"
URL="https://python-future.org"
LICENSE = "MIT"
KEYWORDS = "pasteurize ironpython ipy"
PACKAGES = [
    "libpasteurize",
    "libpasteurize.fixes"
]
CLASSIFIERS = [
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "License :: OSI Approved",
    "License :: OSI Approved :: MIT License",
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
]

setup_kwds = {}


# * Important *
# We forcibly remove the build folder to avoid breaking the
# user's Py3 installation if they run "python2 setup.py
# build" and then "python3 setup.py install".

try:
    # If the user happens to run:
    #     python2 setup.py build
    #     python3 setup.py install
    # then folders like "copyreg" will be in build/lib.
    # If so, we CANNOT let the user install this, because
    # this may break his/her Python 3 install, depending on the folder order in
    # sys.path. (Running "import html" etc. may pick up our Py2
    # substitute packages, instead of the intended system stdlib modules.)
    SYSTEM_MODULES = set([
                          '_dummy_thread',
                          '_markupbase',
                          '_thread',
                          'builtins',
                          # Catch the case that configparser is in the build folder
                          # from a previous version of `future`:
                          'configparser',
                          'copyreg',
                          'html',
                          'http',
                          'queue',
                          'reprlib',
                          'socketserver',
                          'tkinter',
                          'winreg',
                          'xmlrpc'
                         ])

    if sys.version_info[0] >= 3:
        # Do any of the above folders exist in build/lib?
        files = os.listdir(os.path.join('build', 'lib'))
        if len(set(files) & set(SYSTEM_MODULES)) > 0:
            print('ERROR: Your build folder is in an inconsistent state for '
                  'a Python 3.x install. Please remove it manually and run '
                  'setup.py again.', file=sys.stderr)
            sys.exit(1)
except OSError:
    pass

setup(name=NAME,
      version=VERSION,
      author=AUTHOR + ', forked by: ' + FORK_AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      description=DESCRIPTION,
      license=LICENSE,
      keywords=KEYWORDS,
      entry_points={
          'console_scripts': [
              'neptunize = libpasteurize.main:main'
          ]
      },
      install_requires=['future'],  # lib2to3 is another req but it's part of the stdlib
      package_dir={'': 'src'},
      packages=PACKAGES,
      package_data=PACKAGE_DATA,
      include_package_data=True,
      python_requires=">=2.6, !=3.0.*, !=3.1.*, !=3.2.*",
      classifiers=CLASSIFIERS,
      **setup_kwds
     )
