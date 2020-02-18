# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yousearch']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2', 'youtube_transcript_api>=0.3.0,<0.4.0']

entry_points = \
{'console_scripts': ['yousearch = yousearch:app']}

setup_kwargs = {
    'name': 'yousearch',
    'version': '0.1.6',
    'description': 'Interactive CLI to fetch and browse transcripts of YouTube videos',
    'long_description': None,
    'author': 'Konstantin',
    'author_email': 'buecheko@protonmail.ch',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/buecheko/YouSearch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
