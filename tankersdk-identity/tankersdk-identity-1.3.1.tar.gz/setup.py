# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tankersdk_identity', 'tankersdk_identity.crypto', 'tankersdk_identity.test']

package_data = \
{'': ['*']}

install_requires = \
['PyNacl>=1.3.0,<2.0.0']

setup_kwargs = {
    'name': 'tankersdk-identity',
    'version': '1.3.1',
    'description': 'Tanker identity library',
    'long_description': None,
    'author': 'Tanker team',
    'author_email': 'tech@tanker.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/TankerHQ/identity-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
