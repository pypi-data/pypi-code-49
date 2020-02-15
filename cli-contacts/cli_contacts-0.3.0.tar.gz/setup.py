# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cli_contacts']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'peewee>=3.13.1,<4.0.0', 'pydrive>=1.3.1,<2.0.0']

entry_points = \
{'console_scripts': ['black-book = cli_contacts.cli_contacts:cli_contacts']}

setup_kwargs = {
    'name': 'cli-contacts',
    'version': '0.3.0',
    'description': 'A small CLI for managing contact information',
    'long_description': None,
    'author': 'Dan\xc3\xadel \xc3\x96rn \xc3\x81rnason',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
