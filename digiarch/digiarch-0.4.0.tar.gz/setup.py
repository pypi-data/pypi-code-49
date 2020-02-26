# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['digiarch', 'digiarch.identify', 'digiarch.utils']

package_data = \
{'': ['*'], 'digiarch': ['_data/*']}

install_requires = \
['click>=7.0,<8.0',
 'dacite>=1.0,<2.0',
 'pandas>=0.25.1,<0.26.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'pyyaml>=5.2,<6.0',
 'tqdm>=4.36,<5.0',
 'xxhash>=1.4,<2.0']

entry_points = \
{'console_scripts': ['digiarch = digiarch.cli:cli']}

setup_kwargs = {
    'name': 'digiarch',
    'version': '0.4.0',
    'description': 'Tools for the Digital Archive Project at Aarhus Stadsarkiv',
    'long_description': '[![Aarhus Stadsarkiv](https://raw.githubusercontent.com/aarhusstadsarkiv/py-template/master/img/logo.png)](https://stadsarkiv.aarhus.dk/)\n# Digital Archive [![CircleCI](https://circleci.com/gh/aarhusstadsarkiv/digiarch/tree/master.svg?style=shield)](https://circleci.com/gh/aarhusstadsarkiv/digiarch/tree/master) [![codecov](https://codecov.io/gh/aarhusstadsarkiv/digiarch/branch/master/graph/badge.svg)](https://codecov.io/gh/aarhusstadsarkiv/digiarch)\nThis repository contains code pertaining to the Digital Archive Project at Aarhus Stadsarkiv.\n',
    'author': 'Nina Jensen',
    'author_email': 'jnik@aarhus.dk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://stadsarkiv.aarhus.dk/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
