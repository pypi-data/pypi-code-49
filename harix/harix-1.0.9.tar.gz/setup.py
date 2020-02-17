#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from shutil import rmtree

import pip
import pkg_resources
import logging

from setuptools import find_packages, setup, Command

# here = os.path.abspath(os.path.dirname(__file__))
#
# about = {}
# with open(os.path.join(here, 'harix', '__version__.py'), 'r') as f:
#     exec(f.read().encode('utf-8'), about)
#
# readme=""
# with open('README.md', 'r') as f:
#     readme = f.read().encode('utf-8')
#
# readme = readme.decode().strip()
#
#
# def _parse_requirements(file_path):
#
#     requirements = []
#     fileins = open(file_path)
#
#     line = fileins.readline()
#
#     while line:
#         text = line.strip()
#         if text == '':
#             line = fileins.readline()
#             continue
#         requirements.append(text)
#         line = fileins.readline()
#
#     fileins.close()
#     return requirements
#
#
# # # parse_requirements() returns generator of pip.req.InstallRequirement objects
# try:
#     install_reqs = _parse_requirements("requirements.txt")
# except Exception as err:
#     logging.warning('Fail load requirements file')
#     print(err)
#     sys.exit(-1)
#
#
# class UploadCommand(Command):
#     description = 'Build and publish the package.'
#     user_options = []
#
#     @staticmethod
#     def status(s):
#         """Prints things in bold."""
#         print('\033[1m{0}\033[0m'.format(s))
#
#     def initialize_options(self):
#         pass
#
#     def finalize_options(self):
#         pass
#
#     def run(self):
#         try:
#             self.status('Removing previous builds…')
#             rmtree(os.path.join(here, 'dist'))
#         except OSError:
#             pass
#
#         self.status('Building Source and Wheel (universal) distribution…')
#         os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))
#
#         self.status('Uploading the package to PyPI via Twine…')
#         os.system('twine upload dist/*')
#
#         self.status('Pushing git tags…')
#         os.system('git tag v{0}'.format(about['__version__']))
#         os.system('git push --tags')
#
#         sys.exit()


setup(
    name='harix',
    version='1.0.9',
    description='CloudMinds robot develop kit.',
    long_description='Harix Skill Robot SDK',
    long_description_content_type='text/markdown',
    author='CloudMinds',
    author_email='harix@cloudminds.com',
    python_requires='>=3.5.1',
    url='https://www.cloudminds.com',
    keywords="robot development kit CloudMinds HARIX",
    packages=find_packages(),
    install_requires=["googleapis-common-protos==1.6.0", "grpcio==1.24.3", "grpcio-tools==1.24.3"],
    include_package_data=True,
    package_data={},
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py upload support.
    # cmdclass={
    #     'upload': UploadCommand,
    # },
)
