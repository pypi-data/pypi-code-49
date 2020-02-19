# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['riberry_web',
 'riberry_web.lib.gql',
 'riberry_web.lib.gql.graphene_sqla',
 'riberry_web.lib.gql.graphene_sqla.loaders',
 'riberry_web.middleware',
 'riberry_web.riberry']

package_data = \
{'': ['*'], 'riberry_web': ['webapp/*']}

install_requires = \
['fastapi[all]>=0.45.0,<0.46.0', 'riberry>=0.10.21,<0.11.0']

setup_kwargs = {
    'name': 'riberry-web',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'Shady Rafehi',
    'author_email': 'shadyrafehi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
