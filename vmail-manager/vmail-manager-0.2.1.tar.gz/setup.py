# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vmail_manager']

package_data = \
{'': ['*']}

install_requires = \
['argon2_cffi>=19.2.0,<20.0.0',
 'click>=7.0,<8.0',
 'confuse>=1.0.0,<2.0.0',
 'sqlalchemy[pymysql]>=1.3.13,<2.0.0',
 'tabulate>=0.8.6,<0.9.0']

entry_points = \
{'console_scripts': ['vmail-manager = vmail_manager:cli']}

setup_kwargs = {
    'name': 'vmail-manager',
    'version': '0.2.1',
    'description': 'Handy cli interface to manage an vmail-sql-db.',
    'long_description': None,
    'author': 'Dominik Rimpf',
    'author_email': 'dev@d-rimpf.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
