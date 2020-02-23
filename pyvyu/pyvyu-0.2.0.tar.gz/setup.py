# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyvyu']

package_data = \
{'': ['*']}

install_requires = \
['Click>=7.0',
 'appdirs>=1.4.3',
 'atomicwrites>=1.3.0',
 'attrs>=19.1.0',
 'black>=19.3b0',
 'certifi>=2019.3.9',
 'chardet>=3.0.4',
 'codecov>=2.0.15',
 'coverage>=4.5.3',
 'coveralls>=1.7.0',
 'docopt>=0.6.2',
 'idna>=2.8',
 'more-itertools>=7.0.0',
 'numpy>=1.16.3',
 'pandas>=0.24.2',
 'pluggy>=0.9.0',
 'py>=1.8.0',
 'pytest-cov>=2.6.1',
 'pytest>=4.4.1',
 'python-dateutil>=2.8.0',
 'pytz>=2019.1',
 'requests>=2.21.0',
 'six>=1.12.0',
 'toml>=0.10.0',
 'urllib3>=1.24.2']

setup_kwargs = {
    'name': 'pyvyu',
    'version': '0.2.0',
    'description': 'Python API for Datavyu',
    'long_description': None,
    'author': 'Shohan Hasan',
    'author_email': 'shohan.hasan@databrary.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
