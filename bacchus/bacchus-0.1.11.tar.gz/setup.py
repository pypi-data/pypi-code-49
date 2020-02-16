# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['bacchus']

package_data = \
{'': ['*'], 'bacchus': ['templates/*', 'templates/jackett/Indexers/*']}

install_requires = \
['cleo>=0.7.6,<0.8.0',
 'dns-lexicon>=3.3.17,<4.0.0',
 'docker>=4.1,<5.0',
 'netifaces>=0.10.9,<0.11.0',
 'requests>=2.22.0,<3.0.0']

entry_points = \
{'console_scripts': ['bacchus = bacchus.cli:main']}

setup_kwargs = {
    'name': 'bacchus',
    'version': '0.1.11',
    'description': 'Home Server solution based on docker',
    'long_description': None,
    'author': 'David Francos',
    'author_email': 'opensource@davidfrancos.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
