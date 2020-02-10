from setuptools import setup, find_packages
import io
import re
import os
import sys
from os import path

with io.open('./dims_client/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="dims_client",
    version=version,
    author='Jonathas',
    author_email='jhsalves@gmail.com',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://uiot.org/",
    description="Raspberry Pi Client Registration",
    install_requires=['requests', 'uuid',"geocoder","argparse"],
    classifiers=[
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering'
    ],
    keywords=(
        'Universal Internet of Things '
        'Raspberry Client'
    )
)
