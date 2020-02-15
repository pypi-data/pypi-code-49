# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['image_pattern', 'image_pattern.contrib', 'image_pattern.elements']

package_data = \
{'': ['*']}

install_requires = \
['pillow>=7.0,<8.0', 'pydantic>=1.4,<2.0']

setup_kwargs = {
    'name': 'image-pattern',
    'version': '0.0.8',
    'description': '',
    'long_description': None,
    'author': 'acrius',
    'author_email': 'acrius@mail.ru',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
