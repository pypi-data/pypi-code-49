# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['redash_toolbelt']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.22.0,<3.0.0']

setup_kwargs = {
    'name': 'redash-toolbelt',
    'version': '0.1.1',
    'description': 'Redash API client and tools to manage your instance.',
    'long_description': None,
    'author': 'Redash Maintainers',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
