# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['discrete_signals']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=19.3.0,<20.0.0', 'funcy>=1.14,<2.0', 'sortedcontainers>=2.1.0,<3.0.0']

setup_kwargs = {
    'name': 'discrete-signals',
    'version': '0.8.0',
    'description': 'A domain specific language for modeling and manipulating discrete time signals.',
    'long_description': None,
    'author': 'Marcell Vazquez-Chanlatte',
    'author_email': 'mvc@linux.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
