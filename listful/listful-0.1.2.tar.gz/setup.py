# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['listful', 'listful._internal']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'listful',
    'version': '0.1.2',
    'description': 'efficient filtering of lists of objects',
    'long_description': '# listful\n\n[![pypi](https://badge.fury.io/py/listful.svg)](https://pypi.org/project/listful)\n[![Python: 3.6+](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://pypi.org/project/listful)\n[![Downloads](https://img.shields.io/pypi/dm/listful.svg)](https://pypistats.org/packages/listful)\n[![Build Status](https://travis-ci.org/d1618033/listful.svg?branch=master)](https://travis-ci.org/d1618033/listful)\n[![Code coverage](https://codecov.io/gh/d1618033/listful/branch/master/graph/badge.svg)](https://codecov.io/gh/d1618033/listful)\n[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://en.wikipedia.org/wiki/MIT_License)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n\n## Description\n\nEfficient filtering of lists of objects\n\n## Installation\n\n    pip install listful\n\n## Usage\n\n\nInitialize with the fields you want to filter by:\n```\n>>> from listful import Listful\n>>> data = Listful(\n...    [{\'x\': 1, \'y\': 10}, {\'x\': 2, \'y\': 20}, {\'x\': 2, \'y\': 30}], \n...    fields=[\'x\', \'y\']\n... )\n```\n\n### Filtering:\n\n* By one field:\n```\n>>> data.filter(x=1).one_or_none()\n{\'x\': 1, \'y\': 10}\n>>> data.filter(y=20).one_or_none()\n{\'x\': 2, \'y\': 20}\n```\n\n* By one field, with more than one result:\n```\n>>> data.filter(x=2).to_list()\n[{\'x\': 2, \'y\': 20}, {\'x\': 2, \'y\': 30}]\n```\n\n* By two fields:\n```\n>>> data.filter(x=2, y=30).one_or_none()\n{\'x\': 2, \'y\': 30}\n```\n\n* Raise exception if more than one found\n``` \n>>> data.filter(x=2).one_or_raise()\nTraceback (most recent call last):\n<...>\nlistful.exceptions.MoreThanOneResultException: Found more than one result for filter {\'x\': 2}: [{\'x\': 2, \'y\': 20}, {\'x\': 2, \'y\': 30}]\n```\n\n* Get all values for a specific field\n\n```\n>>> data.get_all_for_field(\'x\')\n[1, 2, 2]\n```\n\n### Updating indexes:\n\n`Listful` has the same api as `list`, so you can get/set/delete items the same way \nand the indices will be updated automatically\n\n```\n>>> data[0] = {\'x\': 17, \'y\': 17}\n>>> data.filter(x=17).one_or_none()\n{\'x\': 17, \'y\': 17}\n>>> data[0]\n{\'x\': 17, \'y\': 17}\n>>> del data[0]\n>>> data.filter(x=17).one_or_none()\n``` \n\nIf you want to modify an element and update the indices you can do so explicitly:\n```\n>>> data[0][\'x\'] = 1\n>>> data.rebuild_indexes_for_item(data[0])\n>>> data.filter(x=1).one_or_none()\n{\'x\': 1, \'y\': 20}\n``` \n\n\n### Objects:\n\nListful supports also lists of objects:\n\n```\n>>> class Item:\n...     def __init__(self, x, y):\n...         self.x = x\n...         self.y = y\n...\n...     def __repr__(self):\n...         return f"Item(x={self.x}, y={self.y})"\n\n>>> items = Listful(\n...    [Item(x=1, y=10), Item(x=2, y=20), Item(x=2, y=30)], \n...    fields=[\'x\', \'y\']\n... )\n>>> items.filter(x=1).one_or_none()\nItem(x=1, y=10)\n```\n## For developers\n\n### Create venv and install deps\n\n    make init\n\n### Install git precommit hook\n\n    make precommit_install\n\n### Run linters, autoformat, tests etc.\n\n    make pretty lint test\n\n### Bump new version\n\n    make bump_major\n    make bump_minor\n    make bump_patch\n\n## License\n\nMIT\n\n## Change Log\n\nUnreleased\n-----\n\n* ...\n\n0.1.1 - 2020-02-12\n-----\n\n* ...\n\n0.1.0 - 2020-02-12\n-----\n\n* initial\n',
    'author': 'David S',
    'author_email': 'd1618033@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/listful',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
