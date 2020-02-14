from setuptools import setup

from io import open

import tomlkit

def _get_version():
    with open('pyproject.toml') as pyproject:
        file_contents = pyproject.read()
    return tomlkit.parse(file_contents)['project']['version']

setup(
   name='hello_python_cli',
   version=_get_version(),
   description='Simple python hello cli program',
   author='Mike Kinney',
   author_email='mike.kinney@gmail.com',
   packages=['hello_module'],
   install_requires=[],
   scripts=['hello'],
)
