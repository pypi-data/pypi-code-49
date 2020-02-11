# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyiqvia']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.6.2,<4.0.0']

setup_kwargs = {
    'name': 'pyiqvia',
    'version': '0.2.5',
    'description': 'A clean, async-focused Python3 API for IQVIA data',
    'long_description': '# 🌻 pyiqvia: A clean, async-focused Python3 API for IQVIA™\n\n[![CI](https://github.com/bachya/pyiqvia/workflows/CI/badge.svg)](https://github.com/bachya/pyiqvia/actions)\n[![PyPi](https://img.shields.io/pypi/v/pyiqvia.svg)](https://pypi.python.org/pypi/pyiqvia)\n[![Version](https://img.shields.io/pypi/pyversions/pyiqvia.svg)](https://pypi.python.org/pypi/pyiqvia)\n[![License](https://img.shields.io/pypi/l/pyiqvia.svg)](https://github.com/bachya/pyiqvia/blob/master/LICENSE)\n[![Code Coverage](https://codecov.io/gh/bachya/pyiqvia/branch/dev/graph/badge.svg)](https://codecov.io/gh/bachya/pyiqvia)\n[![Maintainability](https://api.codeclimate.com/v1/badges/3bf37f9cabf73b5d991e/maintainability)](https://codeclimate.com/github/bachya/pyiqvia/maintainability)\n[![Say Thanks](https://img.shields.io/badge/SayThanks-!-1EAEDB.svg)](https://saythanks.io/to/bachya)\n\n`pyiqvia` is an async-focused Python3 library for allergen, asthma, and disease\ndata from the [IQVIA™](https://www.iqvia.com) family of websites (such as \nhttps://pollen.com, https://flustar.com, and more).\n\n# Python Versions\n\n`pyiqvia` is currently supported on:\n\n* Python 3.6\n* Python 3.7\n* Python 3.8\n\n# Installation\n\n```python\npip install pyiqvia\n```\n\n# Usage\n\n`pyiqvia` starts within an\n[aiohttp](https://aiohttp.readthedocs.io/en/stable/) `ClientSession`:\n\n```python\nimport asyncio\n\nfrom aiohttp import ClientSession\n\nfrom pyiqvia import Client\n\n\nasync def main() -> None:\n    """Create the aiohttp session and run the example."""\n    async with ClientSession() as websession:\n      # YOUR CODE HERE\n\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\nCreate a client and get to it:\n\n```python\nimport asyncio\n\nfrom aiohttp import ClientSession\n\nfrom pyiqvia import Client\n\n\nasync def main() -> None:\n    """Create the aiohttp session and run the example."""\n    async with ClientSession() as websession:\n      client = Client(80012, websession)\n\n      # ZIP codes starting with 0 need to be provided as strings:\n      client = Client(\'00544\', websession)\n\n      # Get current allergen information:\n      await client.allergens.current()\n\n      # Get more information on the current allergen outlook:\n      await client.allergens.outlook()\n\n      # Get extended forecast allergen information:\n      await client.allergens.extended()\n\n      # Get historic allergen information:\n      await client.allergens.historic()\n\n      # Get current asthma information:\n      await client.asthma.current()\n\n      # Get extended forecast asthma information:\n      await client.asthma.extended()\n\n      # Get historic asthma information:\n      await client.asthma.historic()\n\n      # Get current cold and flu information:\n      await client.disease.current()\n\n      # Get extended forecast cold and flu information:\n      await client.disease.extended()\n\n      # Get historic cold and flu information:\n      await client.disease.historic()\n\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\n# Contributing\n\n1. [Check for open features/bugs](https://github.com/bachya/pyiqvia/issues)\n  or [initiate a discussion on one](https://github.com/bachya/pyiqvia/issues/new).\n2. [Fork the repository](https://github.com/bachya/pyiqvia/fork).\n3. (_optional, but highly recommended_) Create a virtual environment: `python3 -m venv .venv`\n4. (_optional, but highly recommended_) Enter the virtual environment: `source ./venv/bin/activate`\n5. Install the dev environment: `script/setup`\n6. Code your new feature or bug fix.\n7. Write tests that cover your new functionality.\n8. Run tests and ensure 100% code coverage: `script/test`\n9. Update `README.md` with any new documentation.\n10. Add yourself to `AUTHORS.md`.\n11. Submit a pull request!\n',
    'author': 'Aaron Bach',
    'author_email': 'bachya1208@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bachya/pyiqvia',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.0,<4.0.0',
}


setup(**setup_kwargs)
