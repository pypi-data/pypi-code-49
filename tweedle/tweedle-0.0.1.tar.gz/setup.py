# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tweedle', 'tweedle.cmd', 'tweedle.util']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'munch>=2.5.0,<3.0.0', 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['tweedle = tweedle.entry:main']}

setup_kwargs = {
    'name': 'tweedle',
    'version': '0.0.1',
    'description': 'A CLI tool for manage appconfigs and archive data',
    'long_description': '# <p align="center"> Tweedle </p>\n[![Build Status](https://travis-ci.org/StrayDragon/dragon.svg?branch=master)](https://travis-ci.org/StrayDragon/dragon)\n<!--TODO:Add more icons-->\n\n- Configs manager and controller\n<!-- - Commands manager and controller -->\n---\n\n# **WARNING**:\n:warning: Now, **DON\'T USE** this tool in important workspace directories, because:\n- This project is still in the **development**, and some usages may change in the future.\n- It has some **destructive** and **unrecoverable** operations.\n\n# Install (Dev)\n- For Developer:\n1. At first, you need to install [poetry](https://poetry.eustace.io/)\n2. You can fork or just clone my repo to modify something:\n\n```bash\ngit clone https://github.com/StrayDragon/tweedle.git # master repo\n\ncd Tweedle\npoetry install\npoetry shell\n\n# use it directly and editable\npip install --editable .\n# or unit test\npytest\n```\n\n- For User:\n *Coming soon*\n\n# Usages:\nTODO\n',
    'author': 'straydragon',
    'author_email': 'straydragonl@foxmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/StrayDragon/dragon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
