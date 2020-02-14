#!/usr/bin/env python

import glob
from setuptools import setup, find_packages
import os
import setuptools

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Maxime De Waegeneer",
    author_email="mdewaegeneer@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="A variety of utilities to build high-level flatbuffers structures",
    entry_points={"console_scripts": ["flatmake=flatmake.cli:main", ], },
    install_requires=[],
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"flatmake": ["py.typed"]},
    include_package_data=True,
    keywords="flatmake",
    name="flatmake",
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=[os.path.splitext(os.path.basename(path))[0]
                for path in glob.glob('src/*.py')],
    setup_requires=[],
    url="https://github.com/dweemx/flatmake",
    version="0.4.1",
    zip_safe=False,
)
