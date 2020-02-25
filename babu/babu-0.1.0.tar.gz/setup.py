# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['babu', 'babu._internal']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=19.3.0,<20.0.0',
 'click>=7.0,<8.0',
 'lark-parser>=0.8.1,<0.9.0',
 'ruamel.yaml>=0.16.7,<0.17.0',
 'sqlalchemy>=1.3,<2.0']

entry_points = \
{'console_scripts': ['babu = babu._internal.app:cli']}

setup_kwargs = {
    'name': 'babu',
    'version': '0.1.0',
    'description': 'A static site generator for Python',
    'long_description': None,
    'author': 'Leigh Brenecki',
    'author_email': 'leigh@brenecki.id.au',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
