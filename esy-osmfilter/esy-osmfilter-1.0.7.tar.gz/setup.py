# -*- coding: utf-8 -*-

import pathlib
import setuptools 

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setuptools.setup(
    name="esy-osmfilter",
    version="1.0.7",
    description="Filtering of OSM pbf-files and exporting to geojson",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/osmfilter",
    author="Adam Pluta",
    author_email="Adam.Pluta@dlr.de",
    package_dir={'':'src'},
    packages=setuptools.find_namespace_packages(where='src'),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
     python_requires='>=3.6',
     install_requires=['protobuf >= 3, < 4', 'esy-osm-pbf >= 0'],
            
)
