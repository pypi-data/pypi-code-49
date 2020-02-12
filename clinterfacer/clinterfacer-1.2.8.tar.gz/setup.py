#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This file is used to install the clinterfacer framework."""

# standard library(ies)
import pathlib as pl
import typing

# 3rd party package(s)
import setuptools

# package module(s)
import clinterfacer as package


def read(path: typing.Union[str, pl.Path], encoding: str = 'utf-8') -> str:
    if isinstance(path, str):
        path = pl.Path(path)
    return path.read_text(encoding) if path.exists() else ''


metadata = {
    'name': package.__name__,
    'version': package.__version__,
    'author': package.__author__,
    'author_email': package.__email__,
    'maintainer': package.__maintainer__,
    'maintainer_email': package.__email__,
    'description': package.__description__,
    'long_description': read('./README.md'),
    'long_description_content_type': 'text/markdown',
    'url': package.__url__,
    'packages': setuptools.find_packages(),
    'include_package_data': True,
    'install_requires': [
        'colorlog==4.0.2',
        'importlib_resources==1.0.2',
        'temppathlib==1.0.3',
        'tqdm==4.41.1',
    ],
    # 'entry_points': {
    #     'console_scripts': [
    #         f'{package.__name__} = {package.__name__}.__main__:main',
    #     ],
    # },
    'classifiers': [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'Environment :: Console',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
    ],
}
if __name__ == '__main__':
    setuptools.setup(**metadata)
