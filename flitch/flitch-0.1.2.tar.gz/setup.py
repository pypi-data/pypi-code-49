# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flitch']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'flitch',
    'version': '0.1.2',
    'description': 'A simple text file splitting utility',
    'long_description': '<p align="center">\n    <img width=60% src="https://github.com/aorumbayev/flitch/blob/master/misc/logo-min.png?raw=true" border="0" />\n</p>\n\n<p align="center">\n <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-blue.svg"></a>\n</p>\n\n<p align="center">\n  Flitch is a collection of simple utilities for splitting text files\n</p>\n\n## Table of contents\n\n- [Prerequisites](#prerequisites)\n- [Installation](#installation)\n- [Examples](#examples)\n- [Testing](#contributing)\n\n## Prerequisites\n\nThe following set of technologies is required to be installed:\n\n- [Python 3.6](https://www.python.org/downloads/release/python-360/) and higher\n- [Poetry](https://python-poetry.org) a python dependency manager\n\n## Installation\n\n```bash\npoetry install\n```\n\n## Examples\n\nThe following section demonstrates usage of various file splitting functions available.\n\n### Splitting text file into `n` parts\n\nExample below demonstrated a sample invocation of parts splitter.\n\n```python\nimport flitch\n\nflitch.split_into_parts("{input_file}", "{output_folder}", 10)\n```\n\nFor more details refer to [Documentation]()\n\n### Testing\n\nThe following assumes that all dependencies are installed and virtual environment is activated via `poetry`.\n\n```bash\npytest\n```\n',
    'author': 'Altynbek Orumbayev',
    'author_email': 'aorumbayev@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/python-poetry/poetry',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
