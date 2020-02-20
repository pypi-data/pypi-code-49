# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oauth_token_cache']

package_data = \
{'': ['*']}

install_requires = \
['redis>=3.3,<4.0', 'requests>=2.22,<3.0']

setup_kwargs = {
    'name': 'oauth-token-cache',
    'version': '0.2.0',
    'description': 'Easily obtain and cache OAuth 2.0 JWT tokens from Auth0.',
    'long_description': None,
    'author': 'Nikolai Gulatz',
    'author_email': 'nikolai.gulatz@posteo.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/NikolaiGulatz/oauth-token-cache',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
