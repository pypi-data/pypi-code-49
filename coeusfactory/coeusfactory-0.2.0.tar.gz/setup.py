# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coeusfactory', 'coeusfactory.connectors', 'coeusfactory.repositories']

package_data = \
{'': ['*']}

install_requires = \
['pypubsub>=4.0.3,<5.0.0', 'rainbow-bridge-logger>=0.6.0,<0.7.0']

setup_kwargs = {
    'name': 'coeusfactory',
    'version': '0.2.0',
    'description': 'A Database Connector interface that follows a factory model pattern.',
    'long_description': '# Coeus Factory - Database Connector Factory\n\n[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/coeusfactory)](https://pypi.python.org/pypi/coeusfactory/)\n[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)\n![Coverage](./assets/coverage.svg)\n[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](mailto:atmalmer23@gmail.com)\n[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)\n\n[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)\n[![ForTheBadge powered-by-electricity](http://ForTheBadge.com/images/badges/powered-by-electricity.svg)](http://ForTheBadge.com)\n\nA Database Connector interface that follows a factory model pattern.\n\n## Installation\n\n```bash\n# if using poetry\npoetry add coeusfactory\n```\n\nThen add necessary database interfaces as necessary. Below are the libraries that works with Coeus Factory.\n\n| Database | Python Library |\n|----------|----------------|\n| MongoDB  | `pymongo`      |\n| DynamoDB | `boto3`        |\n',
    'author': 'Almer Mendoza',
    'author_email': 'atmalmer23@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
