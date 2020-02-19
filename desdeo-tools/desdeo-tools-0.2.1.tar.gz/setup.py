# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['desdeo_tools',
 'desdeo_tools.interaction',
 'desdeo_tools.scalarization',
 'desdeo_tools.utils']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.17,<2.0', 'pandas>=0.25.3,<0.26.0']

setup_kwargs = {
    'name': 'desdeo-tools',
    'version': '0.2.1',
    'description': 'Generic tools and design language used in the DESDEO framework',
    'long_description': None,
    'author': 'Bhupinder Saini',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
