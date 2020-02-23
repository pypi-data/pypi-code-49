#!/usr/bin/env python

from setuptools import setup

# Version info -- read without importing
_locals = {}
with open("tyrian_sphinx_theme/_version.py") as fp:
    exec(fp.read(), None, _locals)
version = _locals["__version__"]

setup(
    name="tyrian-sphinx-theme",
    version=version,
    license = "BSD-2-Clause",
    description="A Tyrian based Sphinx theme for Gentoo",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author="Max Magorsch",
    author_email="max@magorsch.de",
    url="https://github.com/mmagorsc/tyrian_sphinx_theme",
    packages=["tyrian_sphinx_theme"],
    package_data={'tyrian_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/*.css',
        'static/*.css_t'
    ]},
    include_package_data=True,
    entry_points={"sphinx.html_themes": ["tyrian_sphinx_theme = tyrian_sphinx_theme"]},
    classifiers=[
        "Framework :: Sphinx",
        "Framework :: Sphinx :: Theme",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
)
