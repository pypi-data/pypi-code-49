"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# Read the API version from disk
with open(path.join(here, 'vtg', 'VERSION')) as fp:
    __version__ = fp.read()


# Setup the package
setup(
    name='VANTAGE6-pyClient',
    version=__version__,
    description='Utilities for federated learning',
    long_description=long_description,
    url='https://github.com/iknl/VANTAGE6-pyClient',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3',
    install_requires=[
        "cryptography",
        "requests",
        "pyjwt"
    ]
)

