# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['felixlib']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.1,<0.5.0',
 'flask>=1.1,<2.0',
 'numpy>=1.17,<2.0',
 'psutil>=5.6,<6.0',
 'pysimplegui>=4.14,<5.0',
 'pywebview>=3.1,<4.0',
 'pywin32>=225,<226',
 'pywinauto>=0.6.8,<0.7.0',
 'send2trash>=1.5,<2.0',
 'wtforms>=2.2,<3.0',
 'xlwings>=0.16.0,<0.17.0']

setup_kwargs = {
    'name': 'felixlib',
    'version': '0.0.8',
    'description': 'felixlib',
    'long_description': 'felixlib\n',
    'author': 'spectereye',
    'author_email': 'spectereye@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
