# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bareasgi_session']

package_data = \
{'': ['*']}

install_requires = \
['bareasgi>=3.5,<4.0', 'baretypes>=3.1.1,<4.0.0', 'bareutils>=3.4.0,<4.0.0']

setup_kwargs = {
    'name': 'bareasgi-session',
    'version': '3.0.0rc1',
    'description': 'Session support for bareASGI',
    'long_description': '# bareASGI-session\n\nSession support for bareASGI\n',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/bareASGI-session',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
