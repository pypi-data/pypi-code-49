# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['odoo_backup']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'flask>=1.1.1,<2.0.0',
 'humanize>=1.0.0,<2.0.0',
 'requests>=2.23.0,<3.0.0']

entry_points = \
{'console_scripts': ['odoo_backup = odoo_backup.main:cli']}

setup_kwargs = {
    'name': 'odoo-backup',
    'version': '0.2.2',
    'description': '',
    'long_description': None,
    'author': 'Martin Lehoux',
    'author_email': 'martin@lehoux.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
