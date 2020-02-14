# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyfony']

package_data = \
{'': ['*'], 'pyfony': ['kernel/*']}

install_requires = \
['console-bundle>=0.2.0,<0.3.0',
 'injecta>=0.6.0,<0.7.0',
 'logger-bundle>=0.1.0,<0.2.0']

setup_kwargs = {
    'name': 'pyfony',
    'version': '0.1.0',
    'description': 'Dependency Injection powered framework',
    'long_description': 'Dependency Injection powered framework\n',
    'author': 'Jiri Koutny',
    'author_email': 'jiri.koutny@datasentics.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DataSentics/pyfony',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<3.8.0',
}


setup(**setup_kwargs)
