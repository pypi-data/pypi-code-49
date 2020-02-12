# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['udebs',
 'udebs..ipynb_checkpoints',
 'udebs.tests',
 'udebs.tests..ipynb_checkpoints']

package_data = \
{'': ['*'], 'udebs': ['keywords/*']}

setup_kwargs = {
    'name': 'udebs',
    'version': '1.0.0a0',
    'description': '',
    'long_description': None,
    'author': 'Ryan Chartier',
    'author_email': 'redrecrm@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
