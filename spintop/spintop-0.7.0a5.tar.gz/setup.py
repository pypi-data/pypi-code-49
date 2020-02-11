import os
import sys
from glob import glob

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, 'spintop', 'VERSION')) as version_file:
    VERSION = version_file.read().strip()
packages = find_packages()

setup(
    name='spintop',
    version=VERSION,
    description='Spintop, the remote supervisor of SpinHub',
    author='William Laroche',
    author_email='william.laroche@tackv.ca',
    maintainer='William Laroche',
    maintainer_email='william.laroche@tackv.ca',
    packages=packages,
    package_data={
        'spintop': ['VERSION']
    },
    install_requires=[
        'anytree',
        'appdirs',
        'click',
        'dataclasses==0.7',
        'dataclasses-serialization==1.2.3',
        'gitpython',
        'jinja2',
        'majortomo',
        'marshmallow',
        'pkginfo',
        'PyJWT',
        'psutil',
        'pyyaml',
        'python-dateutil',
        'requests',
        'tabulate',
        'tblib',
        'incremental-module-loader',
        'simple-memory-cache',
        'xmltodict'
    ],
    extras_require={
    },
    setup_requires=[
        'wheel>=0.29.0,<1.0',
    ],
    tests_require=[
        'mock>=2.0.0',
        'pytest>=2.9.2',
        'pytest-cov>=2.2.1',
    ],
)