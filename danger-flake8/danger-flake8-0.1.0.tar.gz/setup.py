# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['danger_flake8']

package_data = \
{'': ['*']}

install_requires = \
['flake8>=3.7.9,<4.0.0']

setup_kwargs = {
    'name': 'danger-flake8',
    'version': '0.1.0',
    'description': 'Danger plugin to display flake8 lint result',
    'long_description': None,
    'author': 'Maciej Gomolka',
    'author_email': 'maciej.gomolka@elpassion.pl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
