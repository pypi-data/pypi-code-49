# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['apiwrappers', 'apiwrappers.drivers', 'apiwrappers.middleware']

package_data = \
{'': ['*']}

extras_require = \
{':python_version >= "3.7" and python_version < "3.8"': ['typing-extensions>=3.7.4,<4.0.0'],
 'aiohttp': ['aiohttp>=3.6.2,<4.0.0'],
 'requests': ['requests>=2.22.0,<3.0.0']}

setup_kwargs = {
    'name': 'apiwrappers',
    'version': '0.1.0b1',
    'description': 'apiwrappers is a library for building API clients that work both with regular and async code',
    'long_description': '========\nOverview\n========\n\n.. start-badges\n\n.. image:: https://github.com/unmade/apiwrappers/workflows/lint%20and%20test/badge.svg?branch=master\n    :alt: Build Status\n    :target: https://github.com/unmade/apiwrappers/blob/master/.github/workflows/lint-and-test.yml\n\n.. image:: https://readthedocs.org/projects/apiwrappers/badge/?version=latest\n    :alt: Documentation Status\n    :target: https://apiwrappers.readthedocs.io/en/latest/?badge=latest\n\n.. image:: https://codecov.io/gh/unmade/apiwrappers/branch/master/graph/badge.svg\n    :alt: Coverage Status\n    :target: https://codecov.io/gh/unmade/apiwrappers\n\n.. image:: http://www.mypy-lang.org/static/mypy_badge.svg\n    :alt: Checked with mypy\n    :target: http://mypy-lang.org/\n\n.. image:: https://img.shields.io/pypi/v/apiwrappers.svg\n    :alt: PyPI Package latest release\n    :target: https://pypi.org/project/apiwrappers\n\n.. image:: https://img.shields.io/pypi/pyversions/apiwrappers.svg\n    :alt: Supported versions\n    :target: https://pypi.org/project/apiwrappers\n\n.. image:: https://img.shields.io/badge/License-MIT-purple.svg\n    :alt: MIT License\n    :target: https://github.com/unmade/apiwrappers/blob/master/LICENSE\n\n.. end-badges\n\n----------\n\n*apiwrappers* is a library for building API clients\nthat work both with regular and async code.\n\nFeatures\n========\n\n- **DRY** - support both regular and async code with one implementation\n- **Customizable** - middleware mechanism to customize request/response\n- **Typed** - library is fully typed and it\'s relatively easy\n  to get fully typed wrapper\n- **Unified interface** - work with different python HTTP client libraries\n  in the same way. Currently supported:\n\n    - `requests <https://requests.readthedocs.io/en/master/>`_\n    - `aiohttp <https://docs.aiohttp.org/en/stable/client.html>`_\n\nInstallation\n============\n\n.. code-block:: bash\n\n    pip install apiwrappers[requests,aiohttp]\n\n*Note: extras are optional and mainly needed for the final\nuser of your future API wrapper*\n\nGetting Started\n===============\n\nWith *apiwrappers* you can bootstrap clients for different API\npretty fast and easily.\n\nWriting a Simple API Client\n---------------------------\n\nHere is how a typical API client would look like:\n\n.. code-block:: python\n\n    from dataclasses import dataclass\n    from typing import Awaitable, Generic, List, TypeVar, overload\n\n    from apiwrappers import AsyncDriver, Driver, Method, Request, fetch\n\n    T = TypeVar("T", Driver, AsyncDriver)\n\n\n    @dataclass\n    class Repo:\n        id: int\n        name: str\n\n\n    class Github(Generic[T]):\n        def __init__(self, host: str, driver: T):\n            self.host = host\n            self.driver: T = driver\n\n        @overload\n        def get_repos(\n            self: "Github[Driver]", username: str\n        ) -> List[Repo]:\n            ...\n\n        @overload\n        def get_repos(\n            self: "Github[AsyncDriver]", username: str\n        ) -> Awaitable[List[Repo]]:\n            ...\n\n        def get_repos(self, username: str):\n            path = f"/users/{username}/repos"\n            request = Request(Method.GET, self.host, path)\n            return fetch(self.driver, request, model=List[Repo])\n\nThis is small, but fully typed, API client for one of the\n`api.github.com <https://api.github.com>`_ endpoints to get all user repos\nby username:\n\nHere we defined ``Repo`` dataclass that describes what we want\nto get from response and pass it to the ``fetch`` function.\n``fetch`` will then make a request and will cast response to that type.\n\nUsing the API Client\n--------------------\n\nHere how we can use it:\n\n.. code-block:: python\n\n    >>> from apiwrappers import make_driver\n    >>> driver = make_driver("requests")\n    >>> github = Github("https://api.github.com", driver=driver)\n    >>> github.get_repos("unmade")\n    [Repo(id=47463599, name=\'am-date-picker\'),\n     Repo(id=231653904, name=\'apiwrappers\'),\n     Repo(id=144204778, name=\'conway\'),\n     ...\n    ]\n\nTo use it with asyncio all we need to do is provide a proper driver\nand don\'t forget to ``await`` method call:\n\n*Use IPython or Python 3.8+ with python -m asyncio\nto try this code interactively*\n\n.. code-block:: python\n\n    >>> from apiwrappers import make_driver\n    >>> driver = make_driver("aiohttp")\n    >>> github = Github("https://api.github.com", driver=driver)\n    >>> await github.get_repos("unmade")\n    [Repo(id=47463599, name=\'am-date-picker\'),\n     Repo(id=231653904, name=\'apiwrappers\'),\n     Repo(id=144204778, name=\'conway\'),\n     ...\n    ]\n\nDocumentation\n=============\n\nDocumentation for *apiwrappers* can be found at\n`Read The Docs <https://apiwrappers.readthedocs.io/>`_.\n\nContributing\n============\n\nContributions are welcome, and they are greatly appreciated! Every\nlittle bit helps, and credit will always be given.\n\nSee `contributing guide <CONTRIBUTING.rst>`_ to learn more.\n\nCurrently the code and the issues are hosted on Github.\n\nThe project is licensed under MIT.\n',
    'author': 'Aleksei Maslakov',
    'author_email': 'lesha.maslakov@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
