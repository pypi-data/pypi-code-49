# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['test-pypi-poetry']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'test-pypi-poetry',
    'version': '0.2.2',
    'description': 'Testing PyPi & Poetry',
    'long_description': 'for public viewing',
    'author': 'Christopher Farrenden',
    'author_email': 'cfarrend@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://cfarrend.com',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
