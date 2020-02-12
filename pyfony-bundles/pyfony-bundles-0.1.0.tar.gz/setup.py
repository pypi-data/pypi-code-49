# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyfonybundles']

package_data = \
{'': ['*']}

install_requires = \
['injecta>=0.5.0,<0.6.0', 'python-box>=3.4.0,<3.5.0', 'tomlkit>=0.5.0,<0.6.0']

setup_kwargs = {
    'name': 'pyfony-bundles',
    'version': '0.1.0',
    'description': 'Pyfony Framworkd bundles base package',
    'long_description': 'Pyfony Framework bundles base package',
    'author': 'Jiri Koutny',
    'author_email': 'jiri.koutny@datasentics.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DataSentics/pyfony-bundles',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.3,<3.8.0',
}


setup(**setup_kwargs)
