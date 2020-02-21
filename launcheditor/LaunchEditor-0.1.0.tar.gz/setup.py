# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['LaunchEditor']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'launcheditor',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Thiago F. G. Albuquerque',
    'author_email': 'thiagofga@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)
