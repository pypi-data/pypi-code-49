# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['cmdlib']
setup_kwargs = {
    'name': 'cmdlib',
    'version': '0.3.0',
    'description': '',
    'long_description': None,
    'author': 'Xavier Martinez-Hidalgo',
    'author_email': 'xavier@martinezhidalgo.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
