# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tasmidi']

package_data = \
{'': ['*']}

install_requires = \
['mido>=1.2.9,<2.0.0']

entry_points = \
{'console_scripts': ['tasmidi-convert = tasmidi.convert:main',
                     'tasmidi-map = tasmidi.map:main']}

setup_kwargs = {
    'name': 'tasmidi',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Mark Rawls',
    'author_email': 'markrawls96@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
