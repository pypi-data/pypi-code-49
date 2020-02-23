# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['holo']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'holo',
    'version': '0.1.0',
    'description': 'Holo is a library provides overload like cpp',
    'long_description': None,
    'author': 'lvzhi',
    'author_email': '279094354@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Na0ture/holo',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
