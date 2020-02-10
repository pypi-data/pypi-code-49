#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

version = ''
with open('pybpodgui_api/__init__.py', 'r') as fd: 
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)
if not version:
    raise RuntimeError('Cannot find version information')

requirements = [
    'pybpod-api',
    'safe-and-collaborative-architecture',
    'pandas'
]

setup(
    name='pybpod-gui-api',
    version=version,
    description="""pybpod-gui-api is an API for the PyBpodGUI""",
    author=['Ricardo Ribeiro', 'Carlos Mão de Ferro', 'Luís Teixeira'],
    author_email='ricardojvr@gmail.com, micboucinha@gmail.com',
    license='MIT',
    url='https://github.com/pybpod/pybpod-gui-api/',

    include_package_data=True,
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples', 'deploy', 'reports']),
    install_requires=requirements,
)
