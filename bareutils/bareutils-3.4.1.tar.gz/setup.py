# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bareutils', 'bareutils.compression']

package_data = \
{'': ['*']}

install_requires = \
['baretypes>=3.1.0,<4.0.0']

setup_kwargs = {
    'name': 'bareutils',
    'version': '3.4.1',
    'description': 'Utilities for bareASGI and bareClient',
    'long_description': '# bareutils\n\nUtilities for [bareASGI](https://github.com/rob-blackbourn/bareASGI)\nand [bareClient](https://github.com/rob-blackbourn/bareClient)\n(read the [docs](https://rob-blackbourn.github.io/bareUtils/)).\n',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/bareutils',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
