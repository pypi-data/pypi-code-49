# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pgmask']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.0.1,<2.0.0',
 'psycopg2-binary>=2.8.4,<3.0.0',
 'sqlalchemy>=1.3.13,<2.0.0']

setup_kwargs = {
    'name': 'pgmask',
    'version': '0.1.1',
    'description': 'A abstraction to handle of postgres database',
    'long_description': '# Pgmask\n\nA postgres python abstraction\n',
    'author': 'marcusmello',
    'author_email': 'mandealista@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/vintem/pgmask',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
