# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['basicsql']

package_data = \
{'': ['*']}

install_requires = \
['cx_Oracle>=7.3.0,<8.0.0',
 'dpath>=2.0.1,<3.0.0',
 'numpy>=1.18.1,<2.0.0',
 'pandas>=1.0.1,<2.0.0',
 'psycopg2>=2.8.4,<3.0.0',
 'sqlalchemy>=1.3.13,<2.0.0']

setup_kwargs = {
    'name': 'basicsql',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Basic SQL',
    'author': 'Ramon Brandt',
    'author_email': 'devramon22@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
