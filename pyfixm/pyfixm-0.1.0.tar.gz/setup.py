# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyfixm']

package_data = \
{'': ['*']}

install_requires = \
['six>=1.14.0,<2.0.0']

setup_kwargs = {
    'name': 'pyfixm',
    'version': '0.1.0',
    'description': 'Parses FIXM data into Python datastructures',
    'long_description': None,
    'author': 'ignormies',
    'author_email': 'bryce.beagle@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
