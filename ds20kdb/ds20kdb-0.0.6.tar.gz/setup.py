#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Setuptool script. """

import setuptools

with open("README.md") as fh:
    LONG_DESCRIPTION = fh.read()

with open("requirements.txt") as fh:
    REQUIREMENTS = fh.read().split()

setuptools.setup(
    name="ds20kdb",
    version="0.0.6",
    author="Carmelo Pellegrino",
    author_email="carmelo.pellegrino@centrofermi.it",
    description="DarkSide 20K Database User Interface",
    install_requires=REQUIREMENTS,
    license="EUPL 1.2",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://baltig.infn.it/ds20k/dbi-cli",
    packages=setuptools.find_packages(),
    platforms=["Linux"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",
        "Operating System :: POSIX :: Linux",
    ],
)
