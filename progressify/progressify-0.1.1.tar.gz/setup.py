# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['progressify']
setup_kwargs = {
    'name': 'progressify',
    'version': '0.1.1',
    'description': 'Progress bar from an iterable, as a context manager, or decorator',
    'long_description': None,
    'author': 'L3viathan',
    'author_email': 'git@l3vi.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
