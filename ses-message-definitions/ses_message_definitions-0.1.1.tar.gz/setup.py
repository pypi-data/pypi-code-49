# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ses_message_definitions', 'ses_message_definitions.proto']

package_data = \
{'': ['*']}

install_requires = \
['protobuf>=3.11.3,<4.0.0']

setup_kwargs = {
    'name': 'ses-message-definitions',
    'version': '0.1.1',
    'description': 'protobuf message defintions',
    'long_description': None,
    'author': 'Vinu ESB',
    'author_email': 'vinu.vijayakumaran_nair@reutlingen-university.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
