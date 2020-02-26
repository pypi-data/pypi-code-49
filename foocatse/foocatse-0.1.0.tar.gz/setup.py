# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['foocatse']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.0.1,<2.0.0']

setup_kwargs = {
    'name': 'foocatse',
    'version': '0.1.0',
    'description': 'Python package that eases the pain concatenating Pandas categoricals!',
    'long_description': None,
    'author': 'SamEdwardes',
    'author_email': 'edwardes.s@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
