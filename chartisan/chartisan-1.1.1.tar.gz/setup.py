# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chartisan']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'chartisan',
    'version': '1.1.1',
    'description': "Chartisan's Python backend",
    'long_description': None,
    'author': 'Erik Campobadal',
    'author_email': 'soc@erik.cat',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
