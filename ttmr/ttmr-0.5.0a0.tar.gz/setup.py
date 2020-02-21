# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['ttmr']

package_data = \
{'': ['*'], 'ttmr': ['sql/*']}

install_requires = \
['appdirs>=1.4.3,<2.0.0',
 'arrow>=0.15.5,<0.16.0',
 'colorama>=0.4.3,<0.5.0',
 'docopt-ng>=0.7.2,<0.8.0',
 'pendulum>=2.0.5,<3.0.0',
 'prompt-toolkit>=3.0.3,<4.0.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'sqlalchemy>=1.3.13,<2.0.0',
 'tabulate>=0.8.6,<0.9.0',
 'tomlkit>=0.5.8,<0.6.0']

entry_points = \
{'console_scripts': ['ttmr = ttmr.cli:main']}

setup_kwargs = {
    'name': 'ttmr',
    'version': '0.5.0a0',
    'description': '',
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
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
