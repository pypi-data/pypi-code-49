# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kkt', 'kkt.builders', 'kkt.builders.kernels', 'kkt.commands', 'kkt.utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'gitpython>=3.0,<4.0',
 'kaggle>=1.5,<2.0',
 'lockfile>=0.12.2,<0.13.0',
 'poetry==1.0.0',
 'tomlkit>=0.5.8,<0.6.0']

entry_points = \
{'console_scripts': ['kkt = kkt.cli:main']}

setup_kwargs = {
    'name': 'kkt',
    'version': '0.2.0',
    'description': 'A tool for kaggle kernel',
    'long_description': None,
    'author': 'Masahiro Wada',
    'author_email': 'argon.argon.argon@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
