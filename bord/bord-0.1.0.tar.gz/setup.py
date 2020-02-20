# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['bord']

package_data = \
{'': ['*']}

install_requires = \
['asyncclick>=7.0,<8.0',
 'pyppeteer2==0.2.2',
 'screeninfo>=0.6.1,<0.7.0',
 'starlette>=0.13.1,<0.14.0',
 'urllib3>=1.25,<2.0']

entry_points = \
{'console_scripts': ['bord = bord.cli:main']}

setup_kwargs = {
    'name': 'bord',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Steinn Eldjárn Sigurðarson',
    'author_email': 'steinnes@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
