# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['cognite', 'cognite.datastudio']

package_data = \
{'': ['*']}

install_requires = \
['cognite-sdk>=1.3,<2.0',
 'regex>=2019.11,<2020.0',
 'typing_extensions>=3.7,<4.0']

setup_kwargs = {
    'name': 'cognite-datastudio',
    'version': '0.1.14',
    'description': '',
    'long_description': None,
    'author': 'cognite',
    'author_email': 'anders.hafreager@cognite.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
