# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['global_utilities']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'global-utilities',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Clearvision',
    'author_email': 'melodyamclearvision@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
