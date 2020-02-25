# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['colins', 'colins.blueprint', 'colins.scrapers']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.8.2,<5.0.0',
 'pendulum>=2.0.5,<3.0.0',
 'requests>=2.23.0,<3.0.0',
 'yarl>=1.4.2,<2.0.0']

setup_kwargs = {
    'name': 'colins',
    'version': '0.0.1b1',
    'description': '',
    'long_description': '# Colins\n\nBlueprint 를 이용한 반자동화 크롤러\n\n\n',
    'author': 'joyongjin',
    'author_email': 'wnrhd114@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/joyongjin/colins',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
