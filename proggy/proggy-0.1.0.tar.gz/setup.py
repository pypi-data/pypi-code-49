# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['proggy']
setup_kwargs = {
    'name': 'proggy',
    'version': '0.1.0',
    'description': 'A progress bar generator.',
    'long_description': None,
    'author': 'Tarcísio Eduardo Moreira Crocomo',
    'author_email': 'tarcisioe@pm.me',
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
