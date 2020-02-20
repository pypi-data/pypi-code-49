#!/usr/bin/env python3

"""
    Yuuki_Core
    ==========
    The LINE Protocol for Star Yuuki BOT
    
    https://gitlab.com/star-inc/yuuki_core
    
        This Source Code Form is subject to the terms of the Mozilla Public
        License, v. 2.0. If a copy of the MPL was not distributed with this
        file, You can obtain one at http://mozilla.org/MPL/2.0/.
    
        This Source Code Form is "Incompatible With Secondary Licenses", as
        defined by the Mozilla Public License, v. 2.0.
    
    Copyright 2020 Star Inc.(https://starinc.xyz) All Rights Reserved.
"""


from setuptools import setup
from os import path

with open(
    path.join(
        path.abspath(
            path.dirname(__file__)
        ),
        "README.rst"
    ),
        encoding="utf-8"
) as f:
    long_description = f.read()

setup(
    name="yuuki_core",
    version="6.5.1",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://gitlab.com/star-inc/yuuki_core",
    license="Mozilla Public License",
    description="The LINE Protocol for Star Yuuki BOT",
    author="Star Inc.",
    author_email="\"Star Inc.\" <star-inc@aol.com>",
    packages=["yuuki_core"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator"
    ],
    install_requires=["thrift"]
)
