# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rocket_args']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rocket-args',
    'version': '0.1.0',
    'description': 'Make your arg parsing even more declarative!',
    'long_description': '<p align="center">\n    <img src="https://i.imgur.com/vjEOvJj.png" alt="logo">\n    <b>Make your arg parsing even more declarative!</b><br>\n</p>\n\n<p align="center">\n    <a href="https://travis-ci.com/Xaaq/Rocket-args">\n        <img src="https://travis-ci.com/Xaaq/Rocket-args.svg?branch=master" alt="badge">\n    </a>\n    <a href="https://pypi.org/project/rocket-args/">\n        <img src="https://img.shields.io/badge/pypi-0.1.0-informational" alt="badge">\n    </a>\n    <a href="https://github.com/Xaaq/Rocket-args/blob/master/LICENSE">\n        <img src="https://img.shields.io/badge/license-MIT-informational" alt="badge">\n    </a>\n</p>\n\n---\n\n**Source code**:\n<a href="https://github.com/Xaaq/Rocket-args">\n    https://github.com/Xaaq/Rocket-args\n</a>\n\n**Documentation**:\n<a href="https://xaaq.github.io/Rocket-args">\n    https://xaaq.github.io/Rocket-args\n</a>\n\n---\n\n## Overview\n\nSo you wanted a tool that handles parsing arguments? You\'ve come to right place!\n\nKey features:\n\n* fully declarative,\n* less boilerplate code required,\n* type hints,\n* IDE auto-completion - no more strange `Namespace` objects.\n\n## Installation\n\nYou will need Python 3.6+\n\nIn order to install it:\n```\npip install rocket-args\n```\n\n## Examples\n\n### Simple CLI args\n\nCreate `main.py` with following content:\n```python\nfrom rocket_args import RocketBase\n\nclass MyArgs(RocketBase):\n    my_int: int\n    my_float: float\n    my_str: str\n\nargs = MyArgs.parse_args()\nprint(args)\n```\n\nCall it with arguments:\n```\n$ python main.py --my-int 1234 --my-float 12.34 --my-string abcd\nMyArgs(my_int=1234, my_float=12.34, my_str=abcd)\n```\n\n### Auto-generated help\n\n```\n$ python main.py --help\nusage: main.py [-h] [--my-int MY_INT] [--my-float MY_FLOAT] [--my-str MY_STR]\n\noptional arguments:\n  -h, --help           show this help message and exit\n  --my-int MY_INT\n  --my-float MY_FLOAT\n  --my-str MY_STR\n```\n',
    'author': 'Amadeusz Hercog',
    'author_email': 'xaaq333@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Xaaq/Rocket-args',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
