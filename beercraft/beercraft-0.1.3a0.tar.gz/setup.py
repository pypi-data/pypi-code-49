# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['beercraft']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'beercraft',
    'version': '0.1.3a0',
    'description': 'A pub/sub library.',
    'long_description': None,
    'author': 'Mark Gemmill',
    'author_email': 'gitlab@markgemmill.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
