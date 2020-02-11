# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyopenuv']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0']

setup_kwargs = {
    'name': 'pyopenuv',
    'version': '1.0.13',
    'description': 'A simple Python API data from openuv.io',
    'long_description': '# ☀️  pyopenuv: A simple Python API for data from openuv.io\n\n[![CI](https://github.com/bachya/pyopenuv/workflows/CI/badge.svg)](https://github.com/bachya/pyopenuv/actions)\n[![PyPi](https://img.shields.io/pypi/v/pyopenuv.svg)](https://pypi.python.org/pypi/pyopenuv)\n[![Version](https://img.shields.io/pypi/pyversions/pyopenuv.svg)](https://pypi.python.org/pypi/pyopenuv)\n[![License](https://img.shields.io/pypi/l/pyopenuv.svg)](https://github.com/bachya/pyopenuv/blob/master/LICENSE)\n[![Code Coverage](https://codecov.io/gh/bachya/pyopenuv/branch/master/graph/badge.svg)](https://codecov.io/gh/bachya/pyopenuv)\n[![Maintainability](https://api.codeclimate.com/v1/badges/a03c9e96f19a3dc37f98/maintainability)](https://codeclimate.com/github/bachya/pyopenuv/maintainability)\n[![Say Thanks](https://img.shields.io/badge/SayThanks-!-1EAEDB.svg)](https://saythanks.io/to/bachya)\n\n`pyopenuv` is a simple Python library for retrieving UV-related information from\n[openuv.io](https://openuv.io/).\n\n# Installation\n\n```python\npip install pyopenuv\n```\n\n# Python Versions\n\n`pyopenuv` is currently supported on:\n\n* Python 3.6\n* Python 3.7\n* Python 3.8\n\n# API Key\n\nYou can get an API key from\n[the OpenUV console](https://www.openuv.io/console).\n\n# Usage\n\n`pyopenuv` starts within an\n[aiohttp](https://aiohttp.readthedocs.io/en/stable/) `ClientSession`:\n\n```python\nimport asyncio\n\nfrom aiohttp import ClientSession\n\nfrom pyopenuv import Client\n\n\nasync def main() -> None:\n    """Create the aiohttp session and run the example."""\n    async with ClientSession() as websession:\n      # YOUR CODE HERE\n\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\nCreate a client, initialize it, then get to it:\n\n```python\nimport asyncio\n\nfrom aiohttp import ClientSession\n\nfrom pyopenuv import Client\n\n\nasync def main() -> None:\n    """Create the aiohttp session and run the example."""\n    async with ClientSession() as websession:\n      client = pyopenuv.Client(\n        "<OPENUV.IO API KEY>",\n        "<LATITUDE>",\n        "<LONGITUDE>",\n        websession,\n        altitude="<ALTITUDE>")\n\n      # Get current UV index information:\n      await client.uv_index()\n\n      # Get forecasted UV information:\n      await client.uv_forecast()\n\n      # Get information on the window of time during which SPF protection\n      # should be used:\n      await client.uv_protection_window()\n\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\n# Contributing\n\n1. [Check for open features/bugs](https://github.com/bachya/pyopenuv/issues)\n  or [initiate a discussion on one](https://github.com/bachya/pyopenuv/issues/new).\n2. [Fork the repository](https://github.com/bachya/pyopenuv/fork).\n3. (_optional, but highly recommended_) Create a virtual environment: `python3 -m venv .venv`\n4. (_optional, but highly recommended_) Enter the virtual environment: `source ./venv/bin/activate`\n5. Install the dev environment: `script/setup`\n6. Code your new feature or bug fix.\n7. Write tests that cover your new functionality.\n8. Run tests and ensure 100% code coverage: `script/test`\n9. Update `README.md` with any new documentation.\n10. Add yourself to `AUTHORS.md`.\n11. Submit a pull request!\n',
    'author': 'Aaron Bach',
    'author_email': 'bachya1208@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bachya/pyopenuv',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.0,<4.0.0',
}


setup(**setup_kwargs)
