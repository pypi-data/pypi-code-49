# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sequoia']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.11.1,<0.12.0', 'isodate>=0.6.0,<0.7.0']

setup_kwargs = {
    'name': 'sequoia-client-sdk-async',
    'version': '0.1.0',
    'description': '',
    'long_description': '<p align="center">\n  <a href="https://piksel.com/product/piksel-palette/"><img src="https://pikselgroup.com/broadcast/wp-content/uploads/sites/3/2017/09/P-P.png" alt=\'Piksel Palette\'></a>\n</p>\n\n\n# Sequoia Client SDK Async\n\nPython asyncio based SDK for interacting with Piksel Palette services, providing a high level interface to ease the \ndevelopment of different pieces on top of this ecosystem.\n\nAmong other characteristics it provides the following:\n\n* **Authentication** flow integrated and transparent.\n* **Async** requests based on `asyncio` engine providing a high throughput.\n* **Discovery** for Sequoia services, API resources and methods.\n* **Lazy loading** to avoid use and discover not needed elements.\n* **Pagination** automatically handled using continue-based pagination. It\'s completely transparent to client users.\n\n## Requirements\n\n* [Python] 3.6+\n\n## Installation\n\n```console\n$ pip install sequoia-client-sdk-async\n```\n\n## Example\n\n```python\n```\n\n[Python]: https://www.python.org\n',
    'author': 'José Antonio Perdiguero López',
    'author_email': 'perdy@perdy.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pikselpalette/sequoia-python-client-sdk-async',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
