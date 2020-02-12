# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pixler']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pixler',
    'version': '0.1.2',
    'description': 'Draw a pixel map with braille characters',
    'long_description': '# Pixler\n\nA library to draw pixles with unicode braille characters\n\n## Example\n\n![example](https://raw.githubusercontent.com/ikornaselur/pixler/master/.github/example.png)\n',
    'author': 'Axel',
    'author_email': 'pixler@absalon.is',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ikornaselur/pixler',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
