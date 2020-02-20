# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nanonispy']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.17,<2.0']

setup_kwargs = {
    'name': 'nanonispy',
    'version': '1.0.7',
    'description': 'Read Nanonis data files',
    'long_description': None,
    'author': 'Yann-Sebastien Tremblay-Johnston',
    'author_email': 'yanns.tremblay@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
