# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chatserver']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['chatserver = chatserver:chatserver.main',
                     'run = chatserver:chatserver.main']}

setup_kwargs = {
    'name': 'chatserver',
    'version': '0.1.1',
    'description': 'A chatserver written in python',
    'long_description': None,
    'author': 'Luke Spademan',
    'author_email': 'info@lukespademan.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8.0,<4.0.0',
}


setup(**setup_kwargs)
