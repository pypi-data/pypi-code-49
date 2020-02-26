# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lowder']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'lowder',
    'version': '0.6.0',
    'description': 'CLI Loader',
    'long_description': None,
    'author': 'John Aldrich Bernardo',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
