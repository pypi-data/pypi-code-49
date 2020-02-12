# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mag']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'magit',
    'version': '0.1.0',
    'description': 'Multi repo Git manager',
    'long_description': None,
    'author': 'Pavel Brodsky',
    'author_email': 'pavel.brodsky@forter.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)
