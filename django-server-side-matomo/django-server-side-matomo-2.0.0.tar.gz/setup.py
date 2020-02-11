# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['server_side_matomo']

package_data = \
{'': ['*']}

install_requires = \
['Django>=3.0.3,<4.0.0',
 'celery[redis]>=4.4.0,<5.0.0',
 'django-ipware>=2.1.0,<3.0.0',
 'piwikapi>=0.3,<0.4']

setup_kwargs = {
    'name': 'django-server-side-matomo',
    'version': '2.0.0',
    'description': 'Send analytics data to Matomo using celery',
    'long_description': None,
    'author': 'David Burke',
    'author_email': 'david@burkesoftware.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
