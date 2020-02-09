# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['seatingchart']
setup_kwargs = {
    'name': 'seatingchart',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Ryan Opel',
    'author_email': 'ryan.a.opell@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
