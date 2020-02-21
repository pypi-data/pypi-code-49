# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jetblack_lvm2']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'jetblack-lvm2',
    'version': '0.1.0',
    'description': 'Python 3 bindings for lvm2',
    'long_description': '# jetblack-lvm2\n\nPython3 bindings for lvm2\n',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/jetblack-lvm2',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
