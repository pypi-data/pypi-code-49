# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyppeteer']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.3,<2.0.0',
 'pyee>=7.0.1,<8.0.0',
 'tqdm>=4.42.1,<5.0.0',
 'websockets>=8.1,<9.0']

setup_kwargs = {
    'name': 'pyppeteer2',
    'version': '0.2.0',
    'description': 'Headless chrome/chromium automation library (unofficial port of puppeteer)',
    'long_description': None,
    'author': 'pyppeteer',
    'author_email': 'pyppteteer@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
