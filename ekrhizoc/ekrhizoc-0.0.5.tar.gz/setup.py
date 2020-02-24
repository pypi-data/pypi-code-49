# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ekrhizoc',
 'ekrhizoc.bot',
 'ekrhizoc.bot.crawlers',
 'ekrhizoc.bot.helpers',
 'ekrhizoc.cli',
 'ekrhizoc.cli.commands']

package_data = \
{'': ['*']}

install_requires = \
['aiodns>=2.0.0,<3.0.0',
 'aiohttp>=3.6.2,<4.0.0',
 'asyncio>=3.4.3,<4.0.0',
 'beautifulsoup4==4.8.1',
 'brotlipy>=0.7.0,<0.8.0',
 'matplotlib>=3.1.3,<4.0.0',
 'networkx>=2.4,<3.0',
 'poetry>=1.0.3,<2.0.0',
 'pyyaml>=5.3,<6.0',
 'reppy>=0.4.14,<0.5.0',
 'tomlkit>=0.5.8,<0.6.0',
 'urlcanon>=0.3.1,<0.4.0']

entry_points = \
{'console_scripts': ['ekrhizoc = ekrhizoc.cli.__main__:main']}

setup_kwargs = {
    'name': 'ekrhizoc',
    'version': '0.0.5',
    'description': 'A simple python web crawler',
    'long_description': None,
    'author': 'Nicholas Elia',
    'author_email': 'me@nichelia.com',
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
