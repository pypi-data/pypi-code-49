# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sbot']

package_data = \
{'': ['*']}

install_requires = \
['j5>=0.9.0,<0.10.0']

extras_require = \
{'vision': ['zoloto>=0.5.2,<0.6']}

setup_kwargs = {
    'name': 'sbot',
    'version': '0.8.0',
    'description': 'SourceBots API',
    'long_description': "# sbot\n\n[![CircleCI](https://circleci.com/gh/sourcebots/sbot.svg?style=svg)](https://circleci.com/gh/sourcebots/sbot)\n[![PyPI version](https://badge.fury.io/py/sbot.svg)](https://badge.fury.io/py/sbot)\n[![Documentation Status](https://readthedocs.org/projects/pip/badge/?version=stable)](http://pip.pypa.io/en/stable/?badge=stable)\n[![MIT license](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat)](https://opensource.org/licenses/MIT)\n![Bees](https://img.shields.io/badge/bees-110%25-yellow.svg)\n\n`sbot` - SourceBots Robot API - Powered by j5\n\nThis is the API for SourceBots, based on the [j5](https://github.com/j5api/j5)\nlibrary for writing Robotics APIs. It will first be deployed at Smallpeice 2019.\n\nMuch like it's predecessor, [robot-api](https://github.com/sourcebots/robot-api), `sbot` supports\nmultiple backends, although should be more reliable as there is no `UNIX-AF` socket layer.\n\n## Installation\n\nInstall: `pip install sbot`\n\nInstall with vision support: `pip install sbot[vision]`\n\n## Usage\n\n```python\n\nfrom sbot import Robot\n\nr = Robot()\n\n```\n\nOr alternatively:\n\n```python\n\nfrom sbot import Robot\n\nr = Robot(wait_start=False)\n\n# Setup in here\n\nr.wait_start()\n\n```\n",
    'author': 'SourceBots',
    'author_email': 'hello@sourcebots.co.uk',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://sourcebots.co.uk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
