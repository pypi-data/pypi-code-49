# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ehealthkd']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ehealthkd',
    'version': '0.1.0',
    'description': 'Evaluation scripts and tools for eHealth-KD',
    'long_description': None,
    'author': 'eHealth-KD',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
