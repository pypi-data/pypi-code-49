
from setuptools import setup, find_packages
import sys
 
setup(
    name="nmtvis",
    version="1.0",
    author="Player Eric",
    author_email="digimonyan@gmail.com",
    description="A visualization toolkit for attention-based NMT(Neural Machine Translation) system.",
    license="MIT",
    url="https://github.com/player-eric/NMT-Attention-Visualization",
    packages=['nmtvis'],
    install_requires=[
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
