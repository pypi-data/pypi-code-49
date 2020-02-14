# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['botwriter']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.0.1,<2.0.0', 'requests>=2.22.0,<3.0.0']

entry_points = \
{'console_scripts': ['start = botwriter:main']}

setup_kwargs = {
    'name': 'botwriter',
    'version': '0.1.3',
    'description': 'Botwriter provides a simple and comprehensive toolset for saving auth credentials and settings to Infeed as well as fetching data streams for your Botwriter plugins',
    'long_description': None,
    'author': 'Mattis Abrahamsson',
    'author_email': 'mattis.abrahamsson@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
