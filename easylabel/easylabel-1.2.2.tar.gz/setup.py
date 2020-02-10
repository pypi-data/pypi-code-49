# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['easylabel']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'easylabel',
    'version': '1.2.2',
    'description': 'Interface for simple NER labeling',
    'long_description': None,
    'author': 'proprefenetre',
    'author_email': 'proprefenetre@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
