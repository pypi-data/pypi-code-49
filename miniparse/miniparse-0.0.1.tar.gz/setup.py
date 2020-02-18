# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['miniparse']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'miniparse',
    'version': '0.0.1',
    'description': 'A helper library for handwritten parsers.',
    'long_description': 'MiniParse: A Minimal Parser Library\n===================================\n\nA support library for handwritten parsers.\n',
    'author': 'Maximilian Köhl',
    'author_email': 'mkoehl@cs.uni-saarland.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://dgit.cs.uni-saarland.de/koehlma/miniparse',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
