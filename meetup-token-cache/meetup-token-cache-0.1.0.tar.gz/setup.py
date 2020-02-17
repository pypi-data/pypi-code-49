# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['meetup', 'meetup.token_cache']

package_data = \
{'': ['*']}

install_requires = \
['redis>=3.3,<4.0', 'requests>=2.22,<3.0']

setup_kwargs = {
    'name': 'meetup-token-cache',
    'version': '0.1.0',
    'description': 'Easily obtain and cache OAuth 2.0 token from the Meetup API. Obtained tokens are stored both in memory and in Redis.',
    'long_description': None,
    'author': 'Jan-Benedikt Jagusch',
    'author_email': 'jan.jagusch@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/janjagusch/meetup-token-cache',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
