# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="longleding-mrc-engine-sdk",
    version="0.1.0",
    author="Shi Ran",
    author_email="ran.shi@longleding.com",
    description="Longleding MRC Engine SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.emhub.top/em/mrc-engine",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: System :: Logging",
    ],
    python_requires='>=3.6',
)
