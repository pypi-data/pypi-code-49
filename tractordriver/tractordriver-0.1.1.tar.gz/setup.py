# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tractordriver']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['APPLICATION-NAME = entry:main']}

setup_kwargs = {
    'name': 'tractordriver',
    'version': '0.1.1',
    'description': 'TractorDriver is a python base end-to-end test framework for Angular and AngularJS applications.',
    'long_description': None,
    'author': 'Pargev Ghazaryan',
    'author_email': 'pargev.ghazarian@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
