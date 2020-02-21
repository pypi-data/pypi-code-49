# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pymail_aliyun']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.8.1,<5.0.0',
 'imapclient>=2.1.0,<3.0.0',
 'optionaldict>=0.1.1,<0.2.0',
 'requests>=2.22.0,<3.0.0',
 'selenium>=3.141.0,<4.0.0',
 'simplejson>=3.17.0,<4.0.0',
 'tqdm>=4.41.1,<5.0.0']

setup_kwargs = {
    'name': 'pymail-aliyun',
    'version': '0.1.12',
    'description': 'mail-aliyun wrapper',
    'long_description': None,
    'author': 'zbjdonald',
    'author_email': 'service@yingchengtz.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
