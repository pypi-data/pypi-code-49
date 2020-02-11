"""Distribution setup."""

import os

from setuptools import setup, find_packages

import versioneer

ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(ROOT, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name='simpy-agents',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="An extension of SimPy for working with distinct agents.",
    long_description=long_description,
    author='Jake Nunemaker',
    author_email='jake.d.nunemaker@gmail.com',
    credits='Ontje Lünsdorf, Stefan Scherfke',
    license="MIT",
    url="https://github.com/JakeNunemaker/simpy-agents",
    install_requires=[],
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)
