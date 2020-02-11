# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiowwlln', 'aiowwlln.helpers']

package_data = \
{'': ['*']}

install_requires = \
['aiocache>=0.11.1,<0.12.0',
 'aiohttp>=3.6.2,<4.0.0',
 'msgpack>=0.6.2,<0.7.0',
 'ujson>=1.35,<2.0']

setup_kwargs = {
    'name': 'aiowwlln',
    'version': '2.0.5',
    'description': 'A simple Python API for the WWLLN',
    'long_description': '# ⚡️ aiowwlln: A simple Python3 wrapper for WWLLN\n\n[![CI](https://github.com/bachya/aiowwlln/workflows/CI/badge.svg)](https://github.com/bachya/aiowwlln/actions)\n[![PyPi](https://img.shields.io/pypi/v/aiowwlln.svg)](https://pypi.python.org/pypi/aiowwlln)\n[![Version](https://img.shields.io/pypi/pyversions/aiowwlln.svg)](https://pypi.python.org/pypi/aiowwlln)\n[![License](https://img.shields.io/pypi/l/aiowwlln.svg)](https://github.com/bachya/aiowwlln/blob/master/LICENSE)\n[![codecov](https://codecov.io/gh/bachya/aiowwlln/branch/dev/graph/badge.svg)](https://codecov.io/gh/bachya/aiowwlln)\n[![Maintainability](https://api.codeclimate.com/v1/badges/e78f0ba106cbe14bfcea/maintainability)](https://codeclimate.com/github/bachya/aiowwlln/maintainability)\n[![Say Thanks](https://img.shields.io/badge/SayThanks-!-1EAEDB.svg)](https://saythanks.io/to/bachya)\n\n`aiowwlln` is a simple, `asyncio`-driven Python library for retrieving information on\nlightning strikes from\n[the World Wide Lightning Location Network (WWLLNN)](http://wwlln.net/).\n\n**NOTE:** This library is built on an unofficial API; therefore, it may stop working at\nany time.\n\n# Installation\n\n```python\npip install aiowwlln\n```\n\n# Python Versions\n\n`aiowwlln` is currently supported on:\n\n* Python 3.6\n* Python 3.7\n* Python 3.8\n\n# Usage\n\n`aiowwlln` starts within an\n[aiohttp](https://aiohttp.readthedocs.io/en/stable/) `ClientSession`:\n\n```python\nimport asyncio\n\nfrom aiohttp import ClientSession\n\nfrom aiowwlln import Client\n\n\nasync def main() -> None:\n    """Create the aiohttp session and run the example."""\n    async with ClientSession() as websession:\n        # YOUR CODE HERE\n\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\nCreate a client, initialize it, then get to it:\n\n```python\nimport asyncio\nfrom datetime import datetime\n\nfrom aiohttp import ClientSession\n\nfrom aiowwlln import Client\n\n\nasync def main() -> None:\n    """Create the aiohttp session and run the example."""\n    async with ClientSession() as websession:\n        client = aiowwlln.Client(websession)\n\n        # Create a client and get all strike data – by default, data is cached for\n        # 60 seconds (be a responsible data citizen!):\n        client = Client(websession)\n        await client.dump()\n\n        # If you want to increase the cache to 24 hours, go for it:\n        client = Client(websession, cache_seconds=60*60*24)\n        await client.dump()\n\n        # Get strike data within a 50 km radius around a set of coordinates (note that\n        # the cache still applies):\n        await client.within_radius(\n            56.1621538, 92.2333561, 50, unit="metric"\n        )\n\n        # Get strike data within a 10 mile radius around a set of coordinates (note that\n        # the cache still applies):\n        await client.within_radius(\n            56.1621538, 92.2333561, 10, unit="imperial"\n        )\n\n        # Get strike data within a 50 km radius around a set of coordinates _and_\n        # within the last 10 minutes:\n        await client.within_radius(\n            56.1621538, 92.2333561, 50, unit="metric", window=timedelta(minutes=10)\n        )\n\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\n# Contributing\n\n1. [Check for open features/bugs](https://github.com/bachya/aiowwlln/issues)\n  or [initiate a discussion on one](https://github.com/bachya/aiowwlln/issues/new).\n2. [Fork the repository](https://github.com/bachya/aiowwlln/fork).\n3. (_optional, but highly recommended_) Create a virtual environment: `python3 -m venv .venv`\n4. (_optional, but highly recommended_) Enter the virtual environment: `source ./venv/bin/activate`\n5. Install the dev environment: `script/setup`\n6. Code your new feature or bug fix.\n7. Write tests that cover your new functionality.\n8. Run tests and ensure 100% code coverage: `script/test`\n9. Update `README.md` with any new documentation.\n10. Add yourself to `AUTHORS.md`.\n11. Submit a pull request!\n\n',
    'author': 'Aaron Bach',
    'author_email': 'bachya1208@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bachya/aiowwlln',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
