# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['danger_python', 'danger_python.generator']

package_data = \
{'': ['*'], 'danger_python.generator': ['templates/*']}

install_requires = \
['click-default-group>=1.2.2,<2.0.0', 'click>=7.0,<8.0', 'pydantic>=1.4,<2.0']

entry_points = \
{'console_scripts': ['danger-python = danger_python.cli:cli']}

setup_kwargs = {
    'name': 'danger-python',
    'version': '0.1.0',
    'description': 'Write your Dangerfiles in Python.',
    'long_description': None,
    'author': 'Orta Therox',
    'author_email': 'danger@orta.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
