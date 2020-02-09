# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rtpi', 'rtpi.providers']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.11.1,<0.12.0']

setup_kwargs = {
    'name': 'rtpi',
    'version': '0.1.3',
    'description': '',
    'long_description': None,
    'author': 'Marco Rougeth',
    'author_email': 'marco@rougeth.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
