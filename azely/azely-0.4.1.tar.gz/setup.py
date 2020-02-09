# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['azely']

package_data = \
{'': ['*']}

install_requires = \
['astropy>=4.0,<5.0',
 'docopt>=0.6.2,<0.7.0',
 'geopy>=1.21.0,<2.0.0',
 'matplotlib>=3.1.3,<4.0.0',
 'numpy>=1.18.1,<2.0.0',
 'pandas>=0.25.0,<1.1.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'pytz>=2019.3,<2020.0',
 'requests>=2.21.0,<3.0.0',
 'timezonefinder>=4.2.0,<5.0.0',
 'toml>=0.10.0,<0.11.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses>=0.7,<0.8']}

setup_kwargs = {
    'name': 'azely',
    'version': '0.4.1',
    'description': "Python package for calculation and plotting of astronomical object's azimuth/elevation",
    'long_description': None,
    'author': 'Akio Taniguchi',
    'author_email': 'taniguchi@a.phys.nagoya-u.ac.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
