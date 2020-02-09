# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='Damian_Skier_92_2',
    version='0.1.2',
    author='SomeCompany PLC',
    author_email='dev@example.com',
    packages=find_packages(),
    include_package_data=True,
    description='Super useful library',
    url='https://github.com',
    install_requires=['names'],
    scripts=['get_names/get_names.py', 'bin/get_names.bat']
)