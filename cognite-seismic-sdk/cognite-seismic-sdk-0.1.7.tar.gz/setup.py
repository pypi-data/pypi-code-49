# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['cognite',
 'cognite.geospatial',
 'cognite.geospatial.internal',
 'cognite.geospatial.internal.api',
 'cognite.geospatial.internal.models',
 'cognite.seismic',
 'cognite.seismic._api',
 'cognite.seismic.data_classes',
 'cognite.seismic.protos']

package_data = \
{'': ['*']}

install_requires = \
['certifi>=2019.11,<2020.0',
 'grpcio-tools>=1.24,<2.0',
 'numpy>=1.17,<2.0',
 'python-dateutil>=2.8,<3.0',
 'six>=1.14,<2.0',
 'tornado>=6.0,<7.0',
 'urllib3>=1.25,<2.0']

setup_kwargs = {
    'name': 'cognite-seismic-sdk',
    'version': '0.1.7',
    'description': '',
    'long_description': None,
    'author': 'cognite',
    'author_email': 'support@cognite.com',
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
