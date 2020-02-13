# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coeusfactory', 'coeusfactory.connectors', 'coeusfactory.repositories']

package_data = \
{'': ['*']}

install_requires = \
['pypubsub>=4.0.3,<5.0.0', 'rainbow-bridge-logger>=0.6.0,<0.7.0']

setup_kwargs = {
    'name': 'coeusfactory',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'amendoza',
    'author_email': 'amendoza@stratpoint.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
