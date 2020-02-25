# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sir_hiss']

package_data = \
{'': ['*']}

install_requires = \
['func_argparse>=1.1.1,<2.0.0', 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['sir_hiss = sir_hiss:_main']}

setup_kwargs = {
    'name': 'sir-hiss',
    'version': '0.0.2',
    'description': 'Run the relevant tools for a repository',
    'long_description': '# Sir Hiss\n\nAutomatically run the relevant tool (pylint, mypy, pytest, ...) for the current repository.\n\nTools are detected by peeking at configuration files (pyproject.toml, .pylintrc, ...).\n\n## Usage\n\nFrom the root of a python project: \n\n* `hiss` will run the tools\n* `hiss --check` prevent the files to be modified by formatters\n* `hiss --fast` will skip slowest tools (mostly tests)\n* `hiss --preview` will print the list of tools found in the repository\n\n\n## Why this (stupid) name\n\nSir Hiss is the name of the snake in "Robin Hood" animated movie.\nHe has a lot of interesting advice to give to the king but he is never listened to ...\nI hope you don\'t treat your linter like that ^^\n\n\n## Supported tools\n\n* black\n* flake\n* isort\n* mypy\n* nosetest\n* pylint\n* pytest\n\nPlease suggest more tools :-)\n\n\n## TODO\n\n- Read requirements.txt\n- Decide if we should try to read tox.ini. Tox also allow to launch several tools in diferrent environments and there is some overlap with hiss.\n- Add installation instructions\n\n\n## To consider\n\n- Display diff on failure\n- Share some options\n',
    'author': 'gwenzek',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://nest.pijul.com/gwenzek/sir_hiss',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
