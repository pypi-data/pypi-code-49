# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['twofactorauthcli']

package_data = \
{'': ['*']}

install_requires = \
['pyotp>=2.3.0,<3.0.0', 'pyyaml>=5.3,<6.0', 'tabulate>=0.8.6,<0.9.0']

entry_points = \
{'console_scripts': ['2fa = twofactorauthcli:main']}

setup_kwargs = {
    'name': 'twofactorauthcli',
    'version': '0.1.0',
    'description': '2FA in your computer',
    'long_description': '# 2fa-cli\n\n2FA in your computer\n',
    'author': 'Angel Fernandez',
    'author_email': 'angelfernandezibanez@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/anxodio/2fa-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
