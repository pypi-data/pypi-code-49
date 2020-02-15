# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aerie']

package_data = \
{'': ['*']}

install_requires = \
['asyncpg>=0.18.3,<0.19.0',
 'databases>=0.2.5,<0.3.0',
 'psycopg2-binary>=2.8.4,<3.0.0']

setup_kwargs = {
    'name': 'aerie',
    'version': '0.0.1b0',
    'description': 'A database library for asyncio.',
    'long_description': None,
    'author': 'alex.oleshkevich',
    'author_email': 'alex.oleshkevich@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
