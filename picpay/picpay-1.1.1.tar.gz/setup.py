# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['picpay']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.22.0,<3.0.0']

setup_kwargs = {
    'name': 'picpay',
    'version': '1.1.1',
    'description': '',
    'long_description': None,
    'author': 'Marcus Pereira',
    'author_email': 'oi@spacedevs.com.br',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MarcusMann/picpay.py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
