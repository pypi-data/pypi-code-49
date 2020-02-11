# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aioflo', 'aioflo.util']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0']

setup_kwargs = {
    'name': 'aioflo',
    'version': '0.1.5',
    'description': 'A Python3, async-friendly library for Flo by Moen Smart Water Detectors',
    'long_description': '# 💧 aioflo: a Python3, asyncio-friendly library for Notion® Home Monitoring\n\n[![CI](https://github.com/bachya/aioflo/workflows/CI/badge.svg)](https://github.com/bachya/aioflo/actions)\n[![PyPi](https://img.shields.io/pypi/v/aioflo.svg)](https://pypi.python.org/pypi/aioflo)\n[![Version](https://img.shields.io/pypi/pyversions/aioflo.svg)](https://pypi.python.org/pypi/aioflo)\n[![License](https://img.shields.io/pypi/l/aioflo.svg)](https://github.com/bachya/aioflo/blob/master/LICENSE)\n[![Code Coverage](https://codecov.io/gh/bachya/aioflo/branch/master/graph/badge.svg)](https://codecov.io/gh/bachya/aioflo)\n[![Maintainability](https://api.codeclimate.com/v1/badges/1b6949e0c97708925315/maintainability)](https://codeclimate.com/github/bachya/aioflo/maintainability)\n[![Say Thanks](https://img.shields.io/badge/SayThanks-!-1EAEDB.svg)](https://saythanks.io/to/bachya)\n\n`aioflo` is a Python 3, `asyncio`-friendly library for interacting with\n[Flo by Moen Smart Water Detectors](https://www.moen.com/flo).\n\n# Python Versions\n\n`aioflo` is currently supported on:\n\n* Python 3.6\n* Python 3.7\n* Python 3.8\n\n# Installation\n\n```python\npip install aioflo\n```\n\n# Usage\n\n`aioflo` starts within an\n[aiohttp](https://aiohttp.readthedocs.io/en/stable/) `ClientSession`:\n\n```python\nimport asyncio\n\nfrom aiohttp import ClientSession\n\nfrom aioflo import Client\n\n\nasync def main() -> None:\n    """Create the aiohttp session and run the example."""\n    async with ClientSession() as websession:\n        # YOUR CODE HERE\n\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\nCreate an API object, initialize it, then get to it:\n\n```python\nimport asyncio\n\nfrom aiohttp import ClientSession\n\nfrom aioflo import async_get_api\n\n\nasync def main() -> None:\n    """Create the aiohttp session and run the example."""\n    async with ClientSession() as websession:\n        api = await async_get_api(session, "<EMAIL>", "<PASSWORD>")\n\n        # Get user account information:\n        user_info = await api.user.get_info()\n        a_location_id = user_info["locations"][0]["id"]\n\n        # Get location (i.e., device) information:\n        location_info = await api.location.get_info(a_location_id)\n\n        # Get consumption info between a start and end datetime:\n        consumption_info = await api.water.get_consumption_info(\n            a_location_id,\n            datetime(2020, 1, 16, 0, 0),\n            datetime(2020, 1, 16, 23, 59, 59, 999000),\n        )\n\n        # Get various other metrics related to water usage:\n        metrics = await api.water.get_metrics(\n            "<DEVICE_MAC_ADDRESS>",\n            datetime(2020, 1, 16, 0, 0),\n            datetime(2020, 1, 16, 23, 59, 59, 999000),\n        )\n\n        # Set the device in "Away" mode:\n        await set_mode_away(a_location_id)\n\n        # Set the device in "Home" mode:\n        await set_mode_home(a_location_id)\n\n        # Set the device in "Sleep" mode for 120 minutes, then return to "Away" mode:\n        await set_mode_sleep(a_location_id, 120, "away")\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\nSee the module docstrings throughout the library for full info on all parameters, return\ntypes, etc.\n\n# Contributing\n\n1. [Check for open features/bugs](https://github.com/bachya/aioflo/issues)\n  or [initiate a discussion on one](https://github.com/bachya/aioflo/issues/new).\n2. [Fork the repository](https://github.com/bachya/aioflo/fork).\n3. (_optional, but highly recommended_) Create a virtual environment: `python3 -m venv .venv`\n4. (_optional, but highly recommended_) Enter the virtual environment: `source ./venv/bin/activate`\n5. Install the dev environment: `script/setup`\n6. Code your new feature or bug fix.\n7. Write tests that cover your new functionality.\n8. Run tests and ensure 100% code coverage: `script/test`\n9. Update `README.md` with any new documentation.\n10. Add yourself to `AUTHORS.md`.\n11. Submit a pull request!\n',
    'author': 'Aaron Bach',
    'author_email': 'bachya1208@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bachya/aioflo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.0,<4.0.0',
}


setup(**setup_kwargs)
