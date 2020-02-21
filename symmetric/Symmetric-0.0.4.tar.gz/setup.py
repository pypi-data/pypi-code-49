# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['symmetric']

package_data = \
{'': ['*']}

install_requires = \
['flask>=1.1.1,<2.0.0']

setup_kwargs = {
    'name': 'symmetric',
    'version': '0.0.4',
    'description': 'A simple wrapper over Flask to speed up basic API deployments.',
    'long_description': None,
    'author': 'Daniel Leal',
    'author_email': 'dlleal@uc.cl',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
