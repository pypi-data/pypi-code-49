# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['localizedstringkit']

package_data = \
{'': ['*']}

install_requires = \
['deserialize>=1.5.0,<2.0.0', 'dotstrings==0.13.0']

entry_points = \
{'console_scripts': ['localizedstringkit = '
                     'localizedstringkit:command_line.run']}

setup_kwargs = {
    'name': 'localizedstringkit',
    'version': '0.1.0',
    'description': 'Generate .strings files directly from your code',
    'long_description': '',
    'author': 'Dale Myers',
    'author_email': 'dalemy@microsoft.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/microsoft/LocalizedStringKit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
