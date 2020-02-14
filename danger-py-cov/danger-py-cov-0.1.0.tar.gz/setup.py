# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['danger_py_cov']

package_data = \
{'': ['*'], 'danger_py_cov': ['templates/*']}

install_requires = \
['jinja2>=2.11.1,<3.0.0', 'pycobertura>=0.10.5,<0.11.0']

setup_kwargs = {
    'name': 'danger-py-cov',
    'version': '0.1.0',
    'description': 'danger-python plugin for displaying code coverage changes',
    'long_description': None,
    'author': 'Jakub Turek',
    'author_email': 'jkbturek@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
