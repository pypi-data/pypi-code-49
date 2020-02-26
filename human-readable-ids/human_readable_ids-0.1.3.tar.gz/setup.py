# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['human_readable_ids']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'human-readable-ids',
    'version': '0.1.3',
    'description': 'Generates a human readable ID using a format of: Adjective Noun ID',
    'long_description': "# Human Readable ID\n> Python library to generate a random human readable ID in the format of `<adjective> <noun> <number 1-100>`.\n\n\n## Common Usage\nThis can be used any time you need a unique value that should be legible by humans (unlike a UUID).  \nCurrently this library only contains a single method: `get_new_id()`\n\n```python\nIn [1]: import human_readable_ids                                                                                                                                                                                                       \n\nIn [2]: human_readable_ids.get_new_id()                                                                                                                                                                                                 \nOut[2]: 'Short-term Painting 30'\n\n```\n",
    'author': 'Jonny Carlyon',
    'author_email': 'jonathoncarlyon@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/JonnyFb421/human-readable-ids',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
