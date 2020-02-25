# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mormo', 'mormo.schema']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=0.4.0,<0.5.0',
 'click>=7.0,<8.0',
 'fakeredis>=1.1.0,<2.0.0',
 'fastapi>=0.47.1,<0.48.0',
 'frozendict>=1.2,<2.0',
 'hypothesis-jsonschema>=0.10.2,<0.11.0',
 'jinja2>=2.10.3,<3.0.0',
 'pydantic>=1.4,<2.0',
 'python-dotenv>=0.10.5,<0.11.0',
 'pyyaml>=5.3,<6.0',
 'redis>=3.3.11,<4.0.0',
 'requests>=2.22.0,<3.0.0',
 'uvicorn>=0.11.2,<0.12.0']

entry_points = \
{'console_scripts': ['mormo = mormo:cli.cli']}

setup_kwargs = {
    'name': 'mormo',
    'version': '0.7.43',
    'description': 'Automated API Testing Framework for OpenAPI Schema.',
    'long_description': None,
    'author': 'Joey Stevens',
    'author_email': 'joey.stevens00@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
