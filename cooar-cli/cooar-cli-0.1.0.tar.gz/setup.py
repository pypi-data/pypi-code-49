# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['cooar_cli']
install_requires = \
['MechanicalSoup>=0.12.0,<0.13.0',
 'arrow>=0.15.5,<0.16.0',
 'click>=7.0,<8.0',
 'colorama>=0.4.3,<0.5.0',
 'jinja2>=2.11.1,<3.0.0']

entry_points = \
{'console_scripts': ['cooar = cooar_cli:cli']}

setup_kwargs = {
    'name': 'cooar-cli',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Christopher Schmitt',
    'author_email': 'cooar@chris.yt',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chrisWhyTea/cooar-cli',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
