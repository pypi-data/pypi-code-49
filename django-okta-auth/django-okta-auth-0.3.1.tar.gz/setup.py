# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['okta_oauth2', 'okta_oauth2.tests']

package_data = \
{'': ['*']}

install_requires = \
['Django>=1.11.0',
 'PyJWT>=1.7.1,<2.0.0',
 'python-jose[cryptography]>=3.1.0,<4.0.0',
 'requests>=2.22.0,<3.0.0']

setup_kwargs = {
    'name': 'django-okta-auth',
    'version': '0.3.1',
    'description': 'Django Authentication for Okta OpenID',
    'long_description': None,
    'author': 'Matt Magin',
    'author_email': 'matt.magin@cmv.com.au',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
