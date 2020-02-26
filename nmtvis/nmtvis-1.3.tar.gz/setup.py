
from setuptools import setup, find_packages
import sys
 
with open("readme.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="nmtvis",
    version="1.3",
    author="Player Eric",
    author_email="digimonyan@gmail.com",
    description="A visualization toolkit for NMT(Neural Machine Translation) system.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/player-eric/NMT-Visualizer",
    packages=['nmtvis'],
    install_requires=[
        "numpy"
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
    ],
)
