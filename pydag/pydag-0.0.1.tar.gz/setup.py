# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pydag']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pydag',
    'version': '0.0.1',
    'description': 'Python Directed Acyclic Graph',
    'long_description': None,
    'author': 'kelvins',
    'author_email': 'kelvinpfw@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
