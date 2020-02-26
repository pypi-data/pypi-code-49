# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kouyou', 'kouyou.google']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=1.7.11,<2.0.0',
 'gspread>=3.2.0,<4.0.0',
 'numpy>=1.18.1,<2.0.0',
 'oauth2client>=4.1.3,<5.0.0',
 'openpyxl>=3.0.3,<4.0.0',
 'pandas>=1.0.1,<2.0.0',
 'python-dotenv>=0.11.0,<0.12.0',
 'unidecode>=1.1.1,<2.0.0']

setup_kwargs = {
    'name': 'kouyou',
    'version': '1.0',
    'description': 'My personal utils project (Kouyou - 効用 - Utility)',
    'long_description': '![Test Kouyou Package](https://github.com/GutoReis/kouyou/workflows/Test%20Kouyou%20Package/badge.svg?branch=test) ![Auto Deploy Kouyou Package on PyPI](https://github.com/GutoReis/kouyou/workflows/Auto%20Deploy%20Kouyou%20Package%20on%20PyPI/badge.svg) [![codecov](https://codecov.io/gh/GutoReis/kouyou/branch/master/graph/badge.svg)](https://codecov.io/gh/GutoReis/kouyou) [![Documentation Status](https://readthedocs.org/projects/kouyou/badge/?version=latest)](https://kouyou.readthedocs.io/en/latest/?badge=latest) [![PyPI version](https://badge.fury.io/py/kouyou.svg)](https://badge.fury.io/py/kouyou) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) \n\n![kouyou logo](https://drive.google.com/uc?export=view&id=1R9cw03Z0zUezPbeBEvVSOoWKqQg58Mvm)\n\n# Kouyou\n**Kouyou** is a japanese word meaning ***utility***, as the word itself implies, is a python package with every ***util*** code made by me, used in personal projects. Feel free to fork, make PRs with sugestion.\n\n# TO-DO\n> * Google Drive utility to update existed google sheet from a pandas.DataFrame\n\n**Kouyou is part of the Zaidan project** (Link to Zaidan incoming)',
    'author': 'Gustavo Reis',
    'author_email': 'guto.reisdelima@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
