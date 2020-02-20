# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycouchdb']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'pycouchdb',
    'version': '1.14.1',
    'description': 'Modern pure python CouchDB Client.',
    'long_description': '# py-couchdb\n\n[![Build Status](https://travis-ci.org/histrio/py-couchdb.svg?branch=master)](https://travis-ci.org/histrio/py-couchdb)\n![PyPI](https://img.shields.io/pypi/v/pycouchdb)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/pycouchdb)\n[![Coverage Status](https://coveralls.io/repos/github/histrio/py-couchdb/badge.svg?branch=master)](https://coveralls.io/github/histrio/py-couchdb?branch=master)\n\n\n\nModern pure python [CouchDB](https://couchdb.apache.org/) Client.\n\nCurrently there are several libraries in python to connect to couchdb. **Why one more?**\nIt\'s very simple.\n\nAll seems not be maintained, all libraries used standard Python libraries for http requests, and are not compatible with python3.\n\n\n\n## Advantages of py-couchdb\n\n- Use [requests](http://docs.python-requests.org/en/latest/) for http requests (much faster than the standard library)\n- Python2 and Python3 compatible with same codebase (with one exception, python view server that uses 2to3)\n- Also compatible with pypy.\n\n\nExample:\n\n```python\n>>> import pycouchdb\n>>> server = pycouchdb.Server("http://admin:admin@localhost:5984/")\n>>> server.info()[\'version\']\n\'1.2.1\'\n```\n\n\n## Installation\n\nTo install py-couchdb, simply:\n\n```bash\npip install pycouchdb\n```\n\n## Documentation\n\nDocumentation is available at http://pycouchdb.readthedocs.org.\n\n\n## Test\n\nTo test py-couchdb, simply run:\n\n``` bash\n    nosetests --cover-package=pycouchdb --with-doctest\n```\n',
    'author': 'Andrey Antukh',
    'author_email': 'niwi@niwi.be',
    'maintainer': 'Rinat Sabitov',
    'maintainer_email': 'rinat.sabitov@gmail.com',
    'url': 'https://github.com/histrio/py-couchdb',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*',
}


setup(**setup_kwargs)
