# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['json_server']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0', 'click>=7.0,<8.0', 'gera2ld-pyserve>=0.0.7,<0.0.8']

entry_points = \
{'console_scripts': ['json_server = json_server.cli:main']}

setup_kwargs = {
    'name': 'json-server.py',
    'version': '0.1.3',
    'description': 'A simple JSON server',
    'long_description': None,
    'author': 'Gerald',
    'author_email': 'gera2ld@163.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
