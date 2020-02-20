#!/usr/bin/env python
# -*- coding:utf-8 -*-
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Authors:
# - James Alexander Clark, <james.clark@ligo.org>, 2019
"""Setup script for IGWN lfn2pfns"""
import glob
import setuptools

with open("requirements.txt", 'r') as freq:
    LINES = freq.readlines()
    for LINE in enumerate(LINES):
        LINE = LINE[1].rstrip()

REQUIREMENTS = {"install": LINES}
SCRIPTS = glob.glob("bin/*")

setuptools.setup(
    name="igwn-rucio-lfn2pfn",
    version="0.0.4",
    author="James Alexander Clark",
    author_email="james.clark@ligo.org",
    packages=['igwn_lfn2pfn'],
    scripts=SCRIPTS,
    install_requires=REQUIREMENTS["install"],
    url="https://git.ligo.org/rucio/igwn-rucio-lfn2pfn",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    description="LFN2PFN algorithms for IGWN",
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
