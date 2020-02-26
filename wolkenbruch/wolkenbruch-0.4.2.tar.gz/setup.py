#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import setuptools
import versioneer


with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

with open("requirements.txt") as f:
    REQUIREMENTS = f.read()

PACKAGE_NAMES = setuptools.find_packages()

print(setuptools.find_packages())

setuptools.setup(
    name=PACKAGE_NAMES[0],
    version=versioneer.get_version(),
    author="Christoph Fink",
    author_email="christoph.fink@gmail.com",
    description="Checks the weather forecast for your home town and " +
    "sends an e-mail reminder to pack your rain gear if precipitation " +
    "is forecast.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/christoph.fink/wolkenbruch",
    packages=PACKAGE_NAMES,
    install_requires=REQUIREMENTS,
    cmdclass=versioneer.get_cmdclass(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    license="GPLv3",
    entry_points={
        "console_scripts": [
            "wolkenbruch=wolkenbruch:main"
        ]
    }

)
