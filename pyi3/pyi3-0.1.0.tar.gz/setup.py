# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyi3', 'pyi3.meta']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyi3',
    'version': '0.1.0',
    'description': 'A type-hinted python module to communicate with i3.',
    'long_description': None,
    'author': 'Tarcísio Eduardo Moreira Crocomo',
    'author_email': 'tarcisioe@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
