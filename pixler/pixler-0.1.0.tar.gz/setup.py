# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pixler']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pixler',
    'version': '0.1.0',
    'description': 'Draw a pixel map with braille characters',
    'long_description': None,
    'author': 'Axel',
    'author_email': 'pixler@absalon.is',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
