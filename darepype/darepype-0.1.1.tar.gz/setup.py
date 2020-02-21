#!/usr/bin/env python
""" PYPI setup file for darepype package
"""

from setuptools import setup

# This call to setup() does all the work
setup(
    name="darepype",
    version="0.1.1",
    description="DAta REduction PYPEline framework",
    long_description = open("README.md",'rb').read().decode().strip(),
    long_description_content_type="text/markdown",
    url="https://github.com/berthoud/darepype",
    author="HAWC Team",
    author_email="marcberthoud@uchicago.edu",
    license="GNU GPL v3+",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=["darepype","darepype.drp","darepype.tools"],
    include_package_data=True,
    install_requires=["configobj"]
)

""" Run / Install with:
        python setup.py build sdist --format=gztar
    CHECK IT:
        tar tzf dist/*.tar.gz
        twine check dist/darepype-0.1.0.tar.gz
    Upload it:
        twine upload dist/*

"""
