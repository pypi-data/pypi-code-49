# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['edgar3']

package_data = \
{'': ['*']}

install_requires = \
['backoff>=1.10.0,<2.0.0', 'httpx>=0.11.0,<0.12.0', 'pandas>=0.25.3,<0.26.0']

setup_kwargs = {
    'name': 'edgar3',
    'version': '1.1.7',
    'description': 'Simple 13F Edgar Extractor',
    'long_description': None,
    'author': 'Ken Farr',
    'author_email': 'ken@farr.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
