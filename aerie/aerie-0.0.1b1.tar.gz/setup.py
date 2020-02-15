# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aerie']

package_data = \
{'': ['*']}

install_requires = \
['asyncpg>=0.18.3,<0.19.0',
 'databases>=0.2.5,<0.3.0',
 'psycopg2-binary>=2.8.4,<3.0.0']

setup_kwargs = {
    'name': 'aerie',
    'version': '0.0.1b1',
    'description': 'An object mapper for async python.',
    'long_description': '<p align="center">\n<a href="https://travis-ci.org/alex-oleshkevich/aerie">\n    <img src="https://api.travis-ci.com/alex-oleshkevich/aerie.svg?branch=master" alt="Build Status">\n</a>\n<a href="https://codecov.io/gh/alex-oleshkevich/aerie">\n    <img src="https://codecov.io/gh/alex-oleshkevich/aerie/branch/master/graph/badge.svg" alt="Coverage">\n</a>\n<a href="https://pypi.org/project/aerie/">\n    <img src="https://badge.fury.io/py/aerie.svg" alt="Package version">\n</a>\n</p>\n\n---\n\n# An object mapper for async python.\n\n## Installation\n\n```bash\npip install aerie\n```\n\n## Usage\n\n```python\nfrom aerie import Connection, Store, Schema, fields\n\nconnection = Connection(\'postgresql://user:pass@localhost/db_name\')\nstore = Store(connection)\n\nclass User(Schema):\n    id = fields.IntegerField()\n    name = fields.StringField()\n\nrows = await store.raw(\'select * from users\').to(User)\n\n```\n',
    'author': 'alex.oleshkevich',
    'author_email': 'alex.oleshkevich@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/alex-oleshkevich/aerie',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
