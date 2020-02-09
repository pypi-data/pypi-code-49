# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['synology_drive_api']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.22.0,<3.0.0',
 'selenium>=3.141.0,<4.0.0',
 'simplejson>=3.17.0,<4.0.0']

setup_kwargs = {
    'name': 'synology-drive-api',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'zbjdonald',
    'author_email': 'service@yingchengtz.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
