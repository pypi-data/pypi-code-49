# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pymatched']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pymatched',
    'version': '0.1.0',
    'description': 'A library which provides functional pattern matching.',
    'long_description': None,
    'author': 'Seonghyeon Kim',
    'author_email': 'k.seonghyeon@mymusictaste.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
