# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['beercraft']

package_data = \
{'': ['*']}

install_requires = \
['pytest-cov>=2.8.1,<3.0.0']

setup_kwargs = {
    'name': 'beercraft',
    'version': '0.1.1a0',
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
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
