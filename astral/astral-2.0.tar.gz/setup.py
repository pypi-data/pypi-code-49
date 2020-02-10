# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['astral', 'doc', 'test']

package_data = \
{'': ['*'], 'doc': ['static/*']}

install_requires = \
['pytz']

extras_require = \
{':python_version == "3.6"': ['dataclasses']}

setup_kwargs = {
    'name': 'astral',
    'version': '2.0',
    'description': 'Calculations for the position of the sun and moon.',
    'long_description': None,
    'author': 'Simon Kennedy',
    'author_email': 'sffjunkie+code@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sffjunkie/astral',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
