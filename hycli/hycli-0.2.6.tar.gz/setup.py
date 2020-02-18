# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hycli', 'hycli.commands']

package_data = \
{'': ['*'], 'hycli': ['commons/*', 'convert/*', 'services/*']}

install_requires = \
['XlsxWriter>=1.2.7,<2.0.0',
 'click-log>=0.3.2,<0.4.0',
 'click>=7.0,<8.0',
 'filetype>=1.0.5,<2.0.0',
 'halo>=0.0.28,<0.0.29',
 'requests>=2.22.0,<3.0.0',
 'toml>=0.10.0,<0.11.0',
 'xmltodict>=0.12.0,<0.13.0']

entry_points = \
{'console_scripts': ['hycli = hycli.cli:main']}

setup_kwargs = {
    'name': 'hycli',
    'version': '0.2.6',
    'description': 'Interface package to convert invoice to xml by requesting different Hypatos services.',
    'long_description': None,
    'author': 'Dylan Bartels',
    'author_email': 'dylan.bartels@hypatos.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
