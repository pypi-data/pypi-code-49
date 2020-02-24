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
    'version': '0.2.0',
    'description': '',
    'long_description': '<p align="center">\n  <a href="https://piksel.com/product/piksel-palette/"><img src="https://pikselgroup.com/broadcast/wp-content/uploads/sites/3/2017/09/P-P.png" alt=\'Piksel Palette\'></a>\n</p>\n\n\n# Sequoia Client SDK Async\n\nPython asyncio based SDK for interacting with Piksel Palette services, providing a high level interface to ease the \ndevelopment of different pieces on top of this ecosystem.\n\nAmong other characteristics it provides the following:\n\n* **Authentication** flow integrated and transparent.\n* **Async** requests based on `asyncio` engine providing a high throughput.\n* **Discovery** for Sequoia services, API resources and methods.\n* **Lazy loading** to avoid use and discover not needed elements.\n* **Pagination** automatically handled using continue-based pagination. It\'s completely transparent to client users.\n\n## Requirements\n\n* [Python] 3.6+\n\n## Installation\n\n```console\n$ pip install sequoia-client-sdk-async\n```\n\n## Usage\n\nThe client understand three kind of elements:\n* `Service`: Sequoia service against to the request will be performed.\n* `Resource`: An specific resource of previous service.\n* `Method`: Operation that will be performed (`create`, `retrieve`, `update`, `delete`, `list`).\n\nThe syntax to interact with the client is the following for a resource (`create`, `retrieve`, `update`, `delete`):\n\n```python\nawait client.service.resource.method(params={}, headers={})\n```\n\nAnd the next one for interacting with collections (`list`):\n\n```python\nasync for item in client.service.resource.method(params={}, headers={}):\n    ...  # Do something\n```\n\n\n## Examples\n\nHere is a list of some client usage examples.\n\n### Iterate over a list of metadata offers filtered by availabilityStartAt\n```python\nimport sequoia\n\nasync with sequoia.Client(client_id="foo", client_secret="bar", registry_url="https://foo.bar") as client:\n    async for offer in client.metadata.offers.list(params={"withAvailabilityStartAt": "2000-01-01T00:00:00.000Z"}):\n        ...  # Do fancy things with this offer\n```\n\n### Create a metadata offer\n```python\nimport sequoia\n\nasync with sequoia.Client(client_id="foo", client_secret="bar", registry_url="https://foo.bar") as client:\n    await client.metadata.offers.create(json={"foo": "bar"})\n```\n\n### Retrieve a metadata offer\n```python\nimport sequoia\n\nasync with sequoia.Client(client_id="foo", client_secret="bar", registry_url="https://foo.bar") as client:\n    offer = await client.metadata.offers.retrieve(pk="foo")\n```\n\n### Update a metadata offer\n```python\nimport sequoia\n\nasync with sequoia.Client(client_id="foo", client_secret="bar", registry_url="https://foo.bar") as client:\n    await client.metadata.offers.update(pk="foo", json={"foo": "bar"})\n```\n\n### Delete a metadata offer\n```python\nimport sequoia\n\nasync with sequoia.Client(client_id="foo", client_secret="bar", registry_url="https://foo.bar") as client:\n    await client.metadata.offers.delete(pk="foo")\n```\n\n[Python]: https://www.python.org\n',
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
