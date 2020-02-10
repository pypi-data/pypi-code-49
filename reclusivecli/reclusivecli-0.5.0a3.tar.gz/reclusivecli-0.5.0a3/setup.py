#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as description_file:
    LD = description_file.read()

setuptools.setup(
    name="reclusivecli",
    author="Bruno Gregório",
    author_email="reclusivebox@outlook.com",
    version="0.5.0a3",
    description="A small lib to make good command line interfaces effortlessly.",
    long_description=LD,
    long_description_content_type="text/markdown",
    project_urls={"Source": "https://github.com/reclusivebox/reclusivecli", "Web Page": "https://reclusivebox.github.io/reclusivecli/"},
    packages=setuptools.find_packages(),
    package_dir={'':'src'},
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Interpreters"
    ],
    python_requires=">=3.6"
)
