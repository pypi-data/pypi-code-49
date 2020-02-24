#!/usr/bin/env python3
"""Setup."""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="proclamation",
    version="1.0.0",
    author="Ryan A. Pavlik",
    author_email="ryan.pavlik@collabora.com",
    description="A CHANGES/NEWS file creator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/ryanpavlik/proclamation",
    packages=setuptools.find_packages(),
    install_requires=["jinja2", "click"],
    include_package_data=True,
    entry_points={"console_scripts": ["proclamation=proclamation.main:cli"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
