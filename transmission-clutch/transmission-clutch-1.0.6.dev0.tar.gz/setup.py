# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clutch']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.23.0,<3.0.0', 'six>=1.14.0,<2.0.0']

setup_kwargs = {
    'name': 'transmission-clutch',
    'version': '1.0.6.dev0',
    'description': 'Transmission RPC for Python',
    'long_description': None,
    'author': 'mhadam',
    'author_email': 'michael@hadam.us',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)
