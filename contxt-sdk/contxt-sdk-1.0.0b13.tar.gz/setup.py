# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['contxt',
 'contxt.auth',
 'contxt.cli',
 'contxt.models',
 'contxt.services',
 'contxt.utils']

package_data = \
{'': ['*']}

install_requires = \
['auth0-python>=3.9,<4.0',
 'pyjwt>=1.7,<2.0',
 'python-dateutil>=2.8,<3.0',
 'pytz>=2019.2,<2020.0',
 'requests>=2.22,<3.0',
 'tabulate>=0.8.3,<0.9.0',
 'tqdm>=4.36,<5.0']

extras_require = \
{':python_version < "3.7"': ['dataclasses>=0.6.0,<0.7.0'],
 'server': ['python-jose-cryptodome>=1.3,<2.0']}

entry_points = \
{'console_scripts': ['contxt = contxt.__main__:main']}

setup_kwargs = {
    'name': 'contxt-sdk',
    'version': '1.0.0b13',
    'description': 'Contxt SDK from </ndustrial.io>',
    'long_description': '# Contxt Python SDK\n[![build status](https://github.com/ndustrialio/contxt-sdk-python/workflows/build/badge.svg)](https://github.com/ndustrialio/contxt-sdk-python/actions)\n[![pypi version](https://img.shields.io/pypi/v/contxt-sdk.svg)](https://pypi.org/project/contxt-sdk/)\n\n## Dependencies\nThis project **requires** Python 3.6+.\n\n## Installation \nTo install, just use pip:\n```console\n$ pip install contxt-sdk\n```\n\nThis also installs a CLI. To see all supported commands, run the following:\n```console\n$ contxt -h\n```\n\n## Documentation\n* [CLI](docs/cli.md)\n* [Worker](docs/worker.md)\n\n## Contributing\nPlease refer to [CONTRIBUTING.md](CONTRIBUTING.md).',
    'author': 'ndustrial.io',
    'author_email': 'dev@ndustrial.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ndustrialio/contxt-sdk-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
