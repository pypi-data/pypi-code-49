# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['basicldap3']

package_data = \
{'': ['*']}

install_requires = \
['ldap3>=2.6.1,<3.0.0']

setup_kwargs = {
    'name': 'basicldap3',
    'version': '0.1.1',
    'description': 'Provides basic authentication using the ldap3 library',
    'long_description': '# Basic LDAP3\n\nBasic LDAP is a small package that uses the ldap3 library. It can be used to authenticate a user against an LDAP server and can check whether the users is in a specific group. In addition it is possible to get user attributes if the authentication is successful.\n\n## Basic example\n\n### Import basicldap and define the server\n```python\nfrom basicldap import Ldap\n\nLDAP_HOST = \'ldap.server.com\'\nLDAP_BASE_DN = \'DC=example,DC=com\'\n\nconn = Ldap(LDAP_HOST, LDAP_BASE_DN)\n\n# Using SSL\nssl = {"port": 636, "use_ssl": True}\nconn = Ldap(LDAP_HOST, LDAP_BASE_DN, ldap3_args=ssl)\n```\n### Authenticate the user\n```python\nconn.authenticate(user_name, password)\n```\n\n### Get user attributes (requires successful authentication)\n```python\n# To get all attributes\nconn.get_attributes()\n\n# To get specific attributes\nconn.get_attributes([\'mail\', \'cn])\n```',
    'author': 'Ramon Brandt',
    'author_email': 'devramon22@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
