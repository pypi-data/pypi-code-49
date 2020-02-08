# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['repacolors', 'repacolors.palette']

package_data = \
{'': ['*'], 'repacolors': ['command/*']}

install_requires = \
['click>=7.0,<8.0']

entry_points = \
{'console_scripts': ['repacolor = repacolors.command.repacolor:color']}

setup_kwargs = {
    'name': 'repacolors',
    'version': '0.4.0',
    'description': 'Small library for color conversion, manipulation, etc.',
    'long_description': '# repacolors\n\nSmall library for color conversion, manipulation, etc.\n\n[![Build Status](https://travis-ci.com/dyuri/repacolors.svg?branch=master)](https://travis-ci.com/dyuri/repacolors)\n\n## Install\n\n```\n$ pip install repacolors\n```\n\n## `repacolor` command\n\n### `display`\n\nDisplay color in terminal (TODO conversion, manipulation, ...)\n\nExample:\n```\n$ repacolor display red\n$ repacolor display "#ffaad5"\n```\n\n### `pick`\n\nExecutes color picker (`xcolor`) and displays the picked color.\n\n```\n$ repacolor pick\n```\n',
    'author': 'Gyuri Horak',
    'author_email': 'dyuri@horak.hu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dyuri/repacolors',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
