#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

try:
    with open('./README.rst') as readme_file:
        readme = readme_file.read()
except:
    readme = "refer to https://github.com/ihgazni2/efdir/"
else:
    pass

requirements = [
    'lxml',
    'xdict',
    'nvhtml',
    'docutils',
    'elist',
    'edict',
    'pandas',
    'ltdict',
    'dlist',
    'efuntool'
]

setup_requirements = [
    'lxml',
    'elist',
    'xdict',
    'nvhtml',
    'docutils',
    'edict',
    'pandas',
    'ltdict',
    'dlist',
    'efuntool'
]


setup(
    name='efdir',
    version='0.0.21',
    description="handle dirs, mktree from .rst or .json",
    long_description=readme,
    author="dli",
    author_email='286264978@qq.com',
    url='https://github.com/ihgazni2/efdir',
    packages=find_packages(),
    package_data={
                  'documentation': ['docs/*']
                 },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    keywords='mktree,dir-toolset',
     entry_points = {
         'console_scripts': [
             'efdir=efdir.bin:main',
             'efdir_repl_suffix=efdir.BIN.repl_suffix:main',
             'efdir_csv2cols=efdir.BIN.csv2cols:main',
             'efdir_csv2dtb=efdir.BIN.csv2dtb:main',
             'efdir_csv2jsd=efdir.BIN.csv2jsd:main',
          ]
    },
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    setup_requires=setup_requirements,
    py_modules=['efdir'],
)
