# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyflunearyou', 'pyflunearyou.helpers']

package_data = \
{'': ['*']}

install_requires = \
['aiocache>=0.11.1,<0.12.0',
 'aiohttp>=3.6.2,<4.0.0',
 'msgpack>=0.6.2,<0.7.0',
 'ujson>=1.35,<2.0']

setup_kwargs = {
    'name': 'pyflunearyou',
    'version': '1.0.7',
    'description': 'A clean, well-tested Python3 API for Flu Near You',
    'long_description': '# 🤒 pyflunearyou: A Python3 API for Flu Near You\n\n[![CI](https://github.com/bachya/pyflunearyou/workflows/CI/badge.svg)](https://github.com/bachya/pyflunearyou/actions)\n[![PyPi](https://img.shields.io/pypi/v/pyflunearyou.svg)](https://pypi.python.org/pypi/pyflunearyou)\n[![Version](https://img.shields.io/pypi/pyversions/pyflunearyou.svg)](https://pypi.python.org/pypi/pyflunearyou)\n[![License](https://img.shields.io/pypi/l/pyflunearyou.svg)](https://github.com/bachya/pyflunearyou/blob/master/LICENSE)\n[![Code Coverage](https://codecov.io/gh/bachya/pyflunearyou/branch/dev/graph/badge.svg)](https://codecov.io/gh/bachya/pyflunearyou)\n[![Maintainability](https://api.codeclimate.com/v1/badges/dee8556060c7d0e7f2d1/maintainability)](https://codeclimate.com/github/bachya/pyflunearyou/maintainability)\n[![Say Thanks](https://img.shields.io/badge/SayThanks-!-1EAEDB.svg)](https://saythanks.io/to/bachya)\n\n`pyflunearyou` is a simple Python library for retrieving UV-related information\nfrom [Flu Near You](https://flunearyou.org/#!/).\n\n# Installation\n\n```python\npip install pyflunearyou\n```\n\n# Python Versions\n\n`pyflunearyou` is currently supported on:\n\n* Python 3.6\n* Python 3.7\n* Python 3.8\n\n# Usage\n\n`pyflunearyou` starts within an\n[aiohttp](https://aiohttp.readthedocs.io/en/stable/) `ClientSession`:\n\n```python\nimport asyncio\n\nfrom aiohttp import ClientSession\n\n\nasync def main() -> None:\n    """Create the aiohttp session and run the example."""\n    async with ClientSession() as websession:\n      # YOUR CODE HERE\n\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\nCreate a client and get to work:\n\n```python\nimport asyncio\n\nfrom aiohttp import ClientSession\n\nfrom pyflunearyou import Client\n\n\nasync def main() -> None:\n    """Create the aiohttp session and run the example."""\n    async with ClientSession() as websession:\n      client = Client(websession)\n\n      # Get user data for a specific latitude/longitude:\n      await client.user_reports.status_by_coordinates(<LATITUDE>, <LONGITUDE>)\n\n      # Get user data for a specific ZIP code:\n      await client.user_reports.status_by_zip("<ZIP_CODE>")\n\n      # Get CDC data for a specific latitude/longitude:\n      await client.cdc_reports.status_by_coordinates(<LATITUDE>, <LONGITUDE>)\n\n      # Get CDC data for a specific state:\n      await client.cdc_reports.status_by_state(\'<USA_CANADA_STATE_NAME>\')\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\n# Contributing\n\n1. [Check for open features/bugs](https://github.com/bachya/pyflunearyou/issues)\n  or [initiate a discussion on one](https://github.com/bachya/pyflunearyou/issues/new).\n2. [Fork the repository](https://github.com/bachya/pyflunearyou/fork).\n3. (_optional, but highly recommended_) Create a virtual environment: `python3 -m venv .venv`\n4. (_optional, but highly recommended_) Enter the virtual environment: `source ./venv/bin/activate`\n5. Install the dev environment: `script/setup`\n6. Code your new feature or bug fix.\n7. Write tests that cover your new functionality.\n8. Run tests and ensure 100% code coverage: `script/test`\n9. Update `README.md` with any new documentation.\n10. Add yourself to `AUTHORS.md`.\n11. Submit a pull request!\n',
    'author': 'Aaron Bach',
    'author_email': 'bachya1208@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bachya/pyflunearyou',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
