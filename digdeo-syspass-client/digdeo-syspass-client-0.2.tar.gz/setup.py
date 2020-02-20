#!/usr/bin/env python

# This will try to import setuptools. If not here, it fails with a message
import os

try:
    from setuptools import setup
except ImportError:
    raise ImportError(
        "This module could not be installed, probably because"
        " setuptools is not installed on this computer."
        "\nInstall ez_setup ([sudo] pip install ez_setup) and try again."
    )

pre_version = "0.2"
if os.environ.get('CI_COMMIT_TAG'):
    version = os.environ['CI_COMMIT_TAG']
else:
    if os.environ.get('CI_JOB_ID'):
        version = os.environ['CI_JOB_ID']
    else:
        version = pre_version

with open('README.md') as f:
    long_description = f.read()

setup(
    name='digdeo-syspass-client',
    version=version,
    description='DigDeo Syspass Client',
    author='DigDeo',
    author_email='jerome.ornech@digdeo.fr',
    packages=['syspassclient'],
    include_package_data=True,
    url='https://git.digdeo.fr/digdeo-system/FLOSS/digdeo-syspass-client/',
    license='GNU GENERAL PUBLIC LICENSE Version 3',
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown; charset=UTF-8',
    keywords="DigDeo Syspass Client",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5"
    ],
    tests_require=['green']
)
