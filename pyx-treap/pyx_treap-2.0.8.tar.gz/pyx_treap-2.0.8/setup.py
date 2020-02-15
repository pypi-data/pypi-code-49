
"""Package up the Cython version of the treap module."""

import os
import sys
import subprocess

from setuptools import setup, Extension
from Cython.Build import cythonize
# from distutils.extension import Extension

version = '2.0.8'


def is_newer(filename1, filename2):
    """Return True if filename1 is newer than filename2."""
    time1 = os.stat(filename1).st_mtime
    time2 = os.stat(filename2).st_mtime

    if time1 > time2:
        return True
    else:
        return False


def m4_it(infilename, outfilename, define):
    """
    Create outfilename from infilename in a make-like manner.

    If outfilename doesn't exit, create it using m4.
    If outfilename exists but is older than infilename, recreate it using m4.
    """
    build_it = False

    if os.path.exists(outfilename):
        if is_newer(infilename, outfilename):
            # outfilename exists, but is older than infilename, build it
            build_it = True
    else:
        # outfilename does not exist, build it
        build_it = True

    if build_it:
        try:
            subprocess.check_call('set -x; pwd; m4 -D"%s"=1 < "%s" > "%s"' % (define, infilename, outfilename), shell=True)
        except subprocess.CalledProcessError:
            sys.stderr.write('You need m4 on your path to build this code\n')
            sys.exit(1)


if os.path.exists('../m4_treap.m4'):
    m4_it('../m4_treap.m4', 'pyx_treap.pyx', 'pyx')

extensions = [
    Extension("pyx_treap", ["pyx_treap.pyx"]),
    ]

setup(
    name='pyx_treap',
    # ext_modules=[Extension(name='pyx_treap', sources=['pyx_treap.c'])],
    ext_modules=cythonize(extensions),
    version=version,
    description='Python implementation of treaps',
    long_description="""
A set of python modules implementing treaps is provided.

Treaps perform most operations in O(log2(n)) time, and are innately sorted.
They're very nice for keeping a collection of values that needs to
always be sorted, or for optimization problems in which you need to find
the p best values out of q, when p is much smaller than q.

A module is provided for treaps that enforce uniqueness.

A pure python version is included, as is a Cython-enhanced version for performance.
""",
    author='Daniel Richard Stromberg',
    author_email='strombrg@gmail.com',
    url='http://stromberg.dnsalias.org/~dstromberg/treap/',
    platforms='Cross platform',
    license='Apache v2',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Cython",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        ],
    install_requires=[
        "treap",
        "cython",
        ],
    )
