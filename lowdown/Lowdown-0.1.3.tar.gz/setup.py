# :coding: utf-8
# :copyright: Copyright (c) 2014 ftrack

import os
import re

from setuptools import setup, find_packages


ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
SOURCE_PATH = os.path.join(ROOT_PATH, 'source')
README_PATH = os.path.join(ROOT_PATH, 'README.rst')


# Read version from source.
with open(os.path.join(SOURCE_PATH, 'lowdown', '_version.py')) as _version_file:
    VERSION = re.match(
        r'.*__version__ = \'(.*?)\'', _version_file.read(), re.DOTALL
    ).group(1)


# Common common_requirements.
common_requirements = [
    'docutils >= 0.11, < 1',
    'arrow >= 0.4.4, < 1'
]


# Call main setup.
setup(
    name='Lowdown',
    version=VERSION,
    description='Sphinx extension for release notes / changelogs.',
    long_description=open(README_PATH).read(),
    keywords='python, sphinx, changelog, release notes',
    url='https://bitbucket.org/ftrack/lowdown',
    author='ftrack',
    author_email='support@ftrack.com',
    license='Apache License (2.0)',
    packages=find_packages(SOURCE_PATH),
    package_dir={
        '': 'source'
    },
    package_data={
        'lowdown': ['*.css']
    },
    setup_requires=common_requirements + [
        'sphinx >= 1.2.2, < 2',
        'sphinx_rtd_theme >= 0.1.6, < 1'
    ],
    install_requires=common_requirements,
    tests_require=[
    ],
    zip_safe=False
)
