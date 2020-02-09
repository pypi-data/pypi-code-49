# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['migo']
install_requires = \
['aiofiles>=0.4.0,<0.5.0', 'asyncpg>=0.20.1,<0.21.0']

entry_points = \
{'console_scripts': ['migo = migo:main']}

setup_kwargs = {
    'name': 'migo',
    'version': '0.0.2',
    'description': 'Simple async migrations for postgres.',
    'long_description': None,
    'author': 'Sandeep Jadoonanan',
    'author_email': 'jsanweb@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
