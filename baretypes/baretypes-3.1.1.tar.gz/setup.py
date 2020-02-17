# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['baretypes']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'baretypes',
    'version': '3.1.1',
    'description': 'Types for bareASGI and bareClient',
    'long_description': '# bareTypes\n\nTypes for [bareASGI](https://github.com/rob-blackbourn/bareASGI)\nand [bareClient](https://github.com/rob-blackbourn/bareClient)\n(read the [docs](https://rob-blackbourn.github.io/bareTypes/)).\n',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/bareTypes',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
