# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['codeblocks']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['codeblocks = codeblocks:main']}

setup_kwargs = {
    'name': 'codeblocks',
    'version': '0.1.0',
    'description': 'Extract and process code blocks from markdown files.',
    'long_description': None,
    'author': 'Alexey Shamrin',
    'author_email': 'shamrin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
