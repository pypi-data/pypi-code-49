# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['frankensync', 'frankensync.utils']

package_data = \
{'': ['*']}

install_requires = \
['astor>=0.8,<0.9', 'toolz>=0.10,<0.11']

setup_kwargs = {
    'name': 'frankensync',
    'version': '0.0.0',
    'description': '',
    'long_description': None,
    'author': 'Dylan Wilson',
    'author_email': 'dylanjw@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<3.9',
}


setup(**setup_kwargs)
