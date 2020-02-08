#! /usr/bin/env python

import sys
import os

cflags = os.environ.get("CFLAGS", "")
os.environ["CFLAGS"] = cflags + " -fno-strict-aliasing"

from setuptools import setup
from distutils.core import Extension

description = """
The PySubnetTree package provides a Python data structure SubnetTree
that maps subnets given in CIDR notation (incl. corresponding IPv6
versions) to Python objects. Lookups are performed by longest-prefix
matching.
"""

with open('README') as file:
    long_description = file.read()

setup(name="pysubnettree",
    version="0.32", # Filled in automatically.
    maintainer="The Zeek Project",
    maintainer_email="info@zeek.org",
    license="BSD",
    description=description,
    py_modules=['SubnetTree'],
    url="https://github.com/zeek/pysubnettree",
    ext_modules = [
        Extension("_SubnetTree",
            sources=["SubnetTree.cc", "patricia.c", "SubnetTree_wrap.cc"],
            depends=["include/SubnetTree.h", "include/patricia.h"],
            include_dirs=["include/"])
        ]
)

