# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ptera']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ptera',
    'version': '0.1.0',
    'description': 'Call graph addressing library.',
    'long_description': None,
    'author': 'Olivier Breuleux',
    'author_email': 'breuleux@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
