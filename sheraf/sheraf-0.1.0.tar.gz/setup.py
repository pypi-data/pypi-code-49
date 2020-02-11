# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sheraf',
 'sheraf.attributes',
 'sheraf.batches',
 'sheraf.models',
 'sheraf.queryset',
 'sheraf.tools',
 'sheraf.types']

package_data = \
{'': ['*']}

install_requires = \
['orderedset', 'zodb>=5', 'zodburi']

extras_require = \
{'all': ['zeo', 'psycopg2', 'psycopg2cffi', 'relstorage', 'colored', 'tqdm'],
 'doc': ['recommonmark', 'sphinx', 'sphinx-rtd-theme'],
 'relstorage_pg': ['psycopg2', 'psycopg2cffi', 'relstorage'],
 'zeo': ['zeo']}

setup_kwargs = {
    'name': 'sheraf',
    'version': '0.1.0',
    'description': 'Versatile ZODB abstraction layer',
    'long_description': None,
    'author': 'Yaal team',
    'author_email': 'contact@yaal.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.5',
}


setup(**setup_kwargs)
