#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

def readme():
    with open('README.rst', encoding='utf-8') as f:
        return f.read()

setup(
     name='starfishX',   # This is the name of your PyPI-package.
     version='0.155496',  # Update the version number for new releases
     author='nattapat attiratanasunthron',
     author_email='tapattan@gmail.com',
     url='https://github.com/tapattan/starfishX',
     packages=['starfishX'],
     zip_safe = False,
     keywords=['starfishx','finance','การลงทุน','หุ้น'],
     description='Get data of stock exchange thailand (SET)',
     long_description=readme(),
     long_description_content_type='text/markdown',
     install_requires=['requests','beautifulsoup4','urllib3','pyqt5','pandas','html5lib','ffn','tqdm','seaborn','scipy','sklearn','squarify'], #
)
