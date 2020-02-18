# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fst_lookup']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fst-lookup',
    'version': '2020.2.17',
    'description': 'Lookup Foma FSTs',
    'long_description': None,
    'author': 'Eddie Antonio Santos',
    'author_email': 'easantos@ualberta.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/eddieantonio/fst-lookup',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
