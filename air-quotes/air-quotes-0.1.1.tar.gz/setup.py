# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['air_quotes']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'air-quotes',
    'version': '0.1.1',
    'description': 'Mock any proposal, reasonable or otherwise',
    'long_description': None,
    'author': 'JB',
    'author_email': 'jb.tellez@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
