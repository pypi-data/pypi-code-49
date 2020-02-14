# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['danger_py_jscpd']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'danger-py-jscpd',
    'version': '0.1.0',
    'description': 'danger-python plugin for detecting copy/paste',
    'long_description': None,
    'author': 'Mateusz Szklarek',
    'author_email': 'mateusz.szklarek@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
