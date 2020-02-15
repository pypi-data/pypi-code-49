# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['json-server']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0', 'click>=7.0,<8.0', 'gera2ld-pyserve>=0.1.1,<0.2.0']

entry_points = \
{'console_scripts': ['json-server = json-server.cli:main']}

setup_kwargs = {
    'name': 'json-server.py',
    'version': '0.1.5',
    'description': 'A simple JSON server',
    'long_description': '# json-server.py\n\n[![PyPI](https://img.shields.io/pypi/v/json-server.py.svg)](https://pypi.org/project/json-server.py/)\n\nFake REST API with zero coding.\n\nThis project is heavily inspired by [json-server](https://github.com/typicode/json-server) in JavaScript.\n\nRequires Python 3.5+.\n\n## Usage\n\n```\nUsage: json-server [OPTIONS] [FILENAME]\n\nOptions:\n  -b, --bind TEXT  the address to bind, default as `:3000`\n  --help           Show this message and exit.\n```\n\n## Examples\n\n```sh\n# Start with default config\n$ json-server\n\n# Listen on port 3000\n$ json-server -b :3000\n\n# Specify a json file\n$ json-server db.json\n```\n',
    'author': 'Gerald',
    'author_email': 'gera2ld@163.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gera2ld/json-server.py',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
