# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['gopass']
entry_points = \
{'console_scripts': ['gopass = gopass:cli']}

setup_kwargs = {
    'name': 'gopass',
    'version': '0.1.3',
    'description': '',
    'long_description': None,
    'author': 'Nik Cubrilovic',
    'author_email': 'nik@nikcub.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
