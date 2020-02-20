import setuptools
import os
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pandoc-acronyms',
    # the PACKAGE_VERSION variable is defined in the CI runner:
    version=os.environ.get('PACKAGE_VERSION') or '0.0.1.dev0',
    author="Mirko Boehm",
    author_email="mirko@kde.org",
    description="A Python filter to manage acronyms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/mirkoboehm/pandoc-acronyms",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Development Status :: 4 - Beta',
    ],
    entry_points='''
        [console_scripts]
        pandoc-acronyms=filter.pandocacronyms:filter
    ''',
    python_requires='>=3.6',
)
