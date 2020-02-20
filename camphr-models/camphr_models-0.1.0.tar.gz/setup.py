# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['camphr_models']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.2.1,<0.3.0']

entry_points = \
{'console_scripts': ['camphr_models = camphr_models:main']}

setup_kwargs = {
    'name': 'camphr-models',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Yohei Tamura',
    'author_email': 'tamuhey@gmail.com',
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
