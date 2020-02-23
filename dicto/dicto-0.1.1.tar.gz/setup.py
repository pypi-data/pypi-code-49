# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dicto']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=5.3,<6.0', 'xmltodict>=0.12.0,<0.13.0']

setup_kwargs = {
    'name': 'dicto',
    'version': '0.1.1',
    'description': '',
    'long_description': '# dicto',
    'author': 'Cristian Garcia',
    'author_email': 'cgarcia.e88@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://cgarciae.github.io/dicto',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
