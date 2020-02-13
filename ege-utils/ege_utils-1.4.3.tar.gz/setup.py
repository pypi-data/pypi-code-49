# -*- coding: utf-8 -*-
from setuptools import setup
# from distutils.core import setup

setup(
    name='ege_utils',
    description='Utils classes for EGE project',
    long_description='Utils classes for EGE project',
    license='MIT',
    author='Kelson da Costa Medeiros',
    author_email='kelsoncm@gmail.com',
    packages=['ege_utils', 'ege_utils/templates'],
    include_package_data=True,
    version='1.4.3',
    download_url='https://github.com/CoticEaDIFRN/ege_utils/releases/tag/1.4.3',
    url='https://github.com/CoticEaDIFRN/ege_utils',
    keywords=['EGE', 'JWT', 'Django', 'Auth', 'SSO', 'client', ],
    install_requires=['PyJWT==1.7.1', 'django==3.0.1', 'djangorestframework==3.11.0',
                      'ege_theme', 'sc4py==0.1.1', 'sc4net==0.1.2'],
    classifiers=[]
)
