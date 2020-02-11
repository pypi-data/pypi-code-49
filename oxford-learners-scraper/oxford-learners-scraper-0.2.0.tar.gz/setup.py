# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['oxford_learners_scraper']

package_data = \
{'': ['*']}

install_requires = \
['XlsxWriter>=1.2.7,<2.0.0',
 'beautifulsoup4>=4.8.2,<5.0.0',
 'cleo>=0.7.6,<0.8.0',
 'requests>=2.22.0,<3.0.0']

entry_points = \
{'console_scripts': ['ols = oxford_learners_scraper.application:run']}

setup_kwargs = {
    'name': 'oxford-learners-scraper',
    'version': '0.2.0',
    'description': 'Scraper for Oxford Learners Dictionary',
    'long_description': None,
    'author': 'Tadek Teleżyński',
    'author_email': 'tadekte@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
