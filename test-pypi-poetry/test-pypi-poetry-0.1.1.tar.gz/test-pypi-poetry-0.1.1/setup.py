# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['test-pypi-poetry']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'test-pypi-poetry',
    'version': '0.1.1',
    'description': 'Testing PyPi & Poetry',
    'long_description': '# test-pypi-poetry\n\n```\ncurl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python\n```',
    'author': 'Christopher Farrenden',
    'author_email': 'cfarrend@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
