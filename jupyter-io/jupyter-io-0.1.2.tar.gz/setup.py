# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jupyter_io']

package_data = \
{'': ['*']}

install_requires = \
['ipython>=7.11,<8.0', 'matplotlib>=3.1,<4.0', 'pandas>=0.25.0,<1.1.0']

setup_kwargs = {
    'name': 'jupyter-io',
    'version': '0.1.2',
    'description': 'Python pacakge of some I/O utilities for Jupyter notebook',
    'long_description': None,
    'author': 'Akio Taniguchi',
    'author_email': 'taniguchi@a.phys.nagoya-u.ac.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/astropenguin/jupyter-io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
