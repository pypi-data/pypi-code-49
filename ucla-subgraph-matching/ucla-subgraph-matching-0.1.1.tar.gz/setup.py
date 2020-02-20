# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['uclasm', 'uclasm.counting', 'uclasm.filters', 'uclasm.utils']

package_data = \
{'': ['*']}

install_requires = \
['networkx>=2.4,<3.0',
 'numpy>=1.18.1,<2.0.0',
 'pandas>=1.0.1,<2.0.0',
 'scipy>=1.4.1,<2.0.0']

setup_kwargs = {
    'name': 'ucla-subgraph-matching',
    'version': '0.1.1',
    'description': '',
    'long_description': '',
    'author': 'Jacob Moorman',
    'author_email': 'jacob@moorman.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jdmoorman/uclasm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
