#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import re

version = ''
with open('pybpodgui_plugin/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

requirements = [
    'pyforms-gui',
    'pyforms_generic_editor',
    'pybpod-gui-api',
    'pge-plugin-terminal',
    'pybpod-gui-plugin-alyx',
    'pybpod-gui-plugin-session-history',
    'pybpod-gui-plugin-stmdiagram',
    'pybpod-gui-plugin-timeline',
    'pybpod-gui-plugin-trial-timeline',
    'pybpod-gui-plugin-waveplayer',
    'pybpod-gui-plugin-rotaryencoder',
    'pybpod-gui-plugin-soundcard',
]

setup(
    name='pybpod-gui-plugin',
    version=version,
    description="""pybpod-gui-plugin is a behavioral experiments control system written in Python 3 for Bpod""",
    author=['Carlos Mão de Ferro', 'Ricardo Ribeiro', 'Luís Teixeira'],
    author_email='cajomferro@gmail.com, ricardojvr@gmail.com, micboucinha@gmail.com',
    license='MIT',
    url='https://github.com/pybpod/pybpod-gui-plugin',

    include_package_data=True,
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples', 'deploy', 'reports']),

    install_requires=requirements,
)
