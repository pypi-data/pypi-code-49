# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smarty_py', 'smarty_py.api', 'smarty_py.resources']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.3,<0.5.0', 'names>=0.3.0,<0.4.0', 'requests>=2.22.0,<3.0.0']

setup_kwargs = {
    'name': 'smarty-py',
    'version': '0.1.3',
    'description': 'A CLI for SmartRecruiters solutions consulting.',
    'long_description': None,
    'author': 'Elliott Maguire',
    'author_email': 'e.maguire@smartrecruiters.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
