# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['phpipam_client']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.21,<3.0']

setup_kwargs = {
    'name': 'phpipam-client',
    'version': '0.4.0',
    'description': 'PHPIPAM Python RESP API Client',
    'long_description': "# phpipam-client\n[![PyPI](https://img.shields.io/pypi/v/phpipam-client.svg)](https://pypi.org/project/phpipam-client/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/phpipam-client.svg)](https://pypi.org/project/phpipam-client/) [![Pyup Status](https://pyup.io/repos/github/adzhurinskij/phpipam-client/shield.svg)](https://pyup.io/repos/github/adzhurinskij/phpipam-client/) [![Travis (.org)](https://img.shields.io/travis/adzhurinskij/phpipam-client.svg)](https://travis-ci.org/adzhurinskij/phpipam-client)\n\nPHPIPAM Python RESP API Client. It supports Python 2.7 and 3.4+.\n\n### Installation\n```\npip install phpipam-client\n```\n\n### Example\nBasic usage:\n```python\nfrom phpipam_client import PhpIpamClient, GET, PATCH\n\nipam = PhpIpamClient(\n    url='https://ipam',\n    app_id='myapp',\n    username='mylogin',\n    password='mypassword',\n    user_agent='myapiclient', # custom user-agent header\n)\n\n# read object\nipam.get('/sections/')\n\nipam.get('/sections/', {\n    'filter_by': 'id',\n    'filter_value': 2,\n})\n\n# create object\nipam.post('/sections/', {\n    'description': 'example',\n})\n\n# update object\nipam.patch('/sections/1/', {\n    'description': 'example',\n})\n\n# delete object\nipam.delete('/sections/1/')\n\n# read object\nipam.query('/sections/', method=GET)\n\n# update object\nipam.query('/sections/1/', method=PATCH, data={\n    'description': 'example',\n})\n```\nUse encryption:\n```python\nipam = PhpIpamClient(\n    url='https://ipam',\n    app_id='myapp',\n    token='mytoken',\n    encryption=True,\n)\n```\n\n### Other API clients\n- https://github.com/adzhurinskij/phpipam-api-pythonclient (only Python 2.7)\n- https://github.com/efenian/phpipamsdk\n- https://github.com/michaelluich/phpIPAM\n",
    'author': 'Alexandr Dzhurinskij',
    'author_email': 'adzhurinskij@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/adzhurinskij/phpipam-client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
}


setup(**setup_kwargs)
