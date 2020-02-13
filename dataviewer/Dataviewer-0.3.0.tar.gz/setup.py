# -*- coding: utf-8 -*-
# This tool allows the user to visualize a certain directory with subfolders 
# containing files, allowing easy navigation and display of images, tables
# and links to the contained files.
# Copyright (C) 2020  IMDC NV

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
from setuptools import setup, find_packages
try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""
try:
    version = open("version").read()
except IOError:
    version = ""

setup(
    name="Dataviewer",
    version=version,
    description="Dataviewer for project files",
    license="GPL-3.0-or-later",
    author="kdd",
    author_email="kobededecker@gmail.com",
    url="https://gitlab.com/imdc/apps/dataviewer",
    packages=find_packages(),
    include_package_data=True,
    scripts=[r'bin\viewer.bat', r'bin\viewer.py'],
    install_requires=['flask', 'flask_cors'],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)
