# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['awscli_plugin_yubikeytotp']

package_data = \
{'': ['*']}

install_requires = \
['botocore>=1.14.14,<2.0.0']

setup_kwargs = {
    'name': 'awscli-plugin-yubikeytotp',
    'version': '0.1.0.dev1',
    'description': '',
    'long_description': None,
    'author': 'Thomas Liebetraut',
    'author_email': 'thomas@tommie-lie.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
