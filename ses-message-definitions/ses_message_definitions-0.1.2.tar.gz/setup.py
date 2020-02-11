# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ses_message_definitions']

package_data = \
{'': ['*'], 'ses_message_definitions': ['proto/*']}

setup_kwargs = {
    'name': 'ses-message-definitions',
    'version': '0.1.2',
    'description': 'protobuf message defintions',
    'long_description': None,
    'author': 'Vinu ESB',
    'author_email': 'vinu.vijayakumaran_nair@reutlingen-university.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
