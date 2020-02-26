# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages
from vise.__init__ import __version__
module_dir = os.path.dirname(os.path.abspath(__file__))
reqs_raw = open(os.path.join(module_dir, "requirements.txt")).read()
reqs_list = [r.replace("==", "~=") for r in reqs_raw.split("\n")]

with open("README.md", "r") as fh:
    long_description = fh.read()

version = __version__

setup(
    name='vise',
    version=version,
    author="Yu Kumagai",
    author_email="yuuukuma@gmail.com",
    url='https://github.com/oba-group/vise',
    packages=find_packages(),
    license='MIT license',
    description="Package for constructing the computational materials database ",
    long_description=long_description,
    long_description_content_type="text/markdown",

    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
    install_requires=reqs_list,
    ext_modules={},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'vise = fireworks.cli.main:vise',
        ]
    }
)
