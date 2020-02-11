# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flake8_annotations']

package_data = \
{'': ['*']}

install_requires = \
['flake8>=3.7.9,<4.0.0']

extras_require = \
{':python_version < "3.8"': ['typed-ast>=1.4,<2.0']}

entry_points = \
{'flake8.extension': ['ANN = flake8_annotations.checker:TypeHintChecker']}

setup_kwargs = {
    'name': 'flake8-annotations',
    'version': '2.0.0',
    'description': 'Flake8 Type Annotation Checks',
    'long_description': "# flake8-annotations\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flake8-annotations)](https://pypi.org/project/flake8-annotations/)\n[![PyPI](https://img.shields.io/pypi/v/flake8-annotations)](https://pypi.org/project/flake8-annotations/)\n[![Build Status](https://dev.azure.com/python-discord/Python%20Discord/_apis/build/status/python-discord.flake8-annotations?branchName=master)](https://dev.azure.com/python-discord/Python%20Discord/_build/latest?definitionId=16&branchName=master)\n[![Discord](https://img.shields.io/static/v1?label=Python%20Discord&logo=discord&message=%3E30k%20members&color=%237289DA&logoColor=white)](https://discord.gg/2B963hn)\n\n\n`flake8-annotations` is a plugin for [Flake8](http://flake8.pycqa.org/en/latest/) that detects the absence of [PEP 3107-style](https://www.python.org/dev/peps/pep-3107/) function annotations and [PEP 484-style](https://www.python.org/dev/peps/pep-0484/#type-comments) type comments  (see: [Caveats](#Caveats-for-PEP-484-style-Type-Comments)).\n\nWhat this won't do: Check variable annotations (see: [PEP 526](https://www.python.org/dev/peps/pep-0526/)), respect stub files, or replace [mypy](http://mypy-lang.org/).\n\n## Installation\n\nInstall from PyPi with your favorite `pip` invocation:\n\n```bash\n$ pip install flake8-annotations\n```\n\nIt will then be run automatically as part of Flake8.\n\nYou can verify it's being picked up by invoking the following in your shell:\n\n```bash\n$ flake8 --version\n3.7.8 (flake8-annotations: 2.0.0, mccabe: 0.6.1, pycodestyle: 2.5.0, pyflakes: 2.1.1) CPython 3.7.4 on Darwin\n```\n\n## Table of Warnings\n### Function Annotations\n| ID       | Description                                   |\n|----------|-----------------------------------------------|\n| `ANN001` | Missing type annotation for function argument |\n| `ANN002` | Missing type annotation for `*args`           |\n| `ANN003` | Missing type annotation for `**kwargs`        |\n\n### Method Annotations\n| ID       | Description                                        |\n|----------|----------------------------------------------------|\n| `ANN101` | Missing type annotation for `self` in method       |\n| `ANN102` | Missing type annotation for `cls` in classmethod   |\n\n### Return Annotations\n| ID       | Description                                           |\n|----------|-------------------------------------------------------|\n| `ANN201` | Missing return type annotation for public function    |\n| `ANN202` | Missing return type annotation for protected function |\n| `ANN203` | Missing return type annotation for secret function    |\n| `ANN204` | Missing return type annotation for special method     |\n| `ANN205` | Missing return type annotation for staticmethod       |\n| `ANN206` | Missing return type annotation for classmethod        |\n\n### Type Comments\n| ID       | Description                                               |\n|----------|-----------------------------------------------------------|\n| `ANN301` | PEP 484 disallows both type annotations and type comments |\n\n\n## Configuration Options\n### `--suppress-none-returning`: `bool`\nSuppress `ANN200`-level errors for functions that meet one of the following criteria:\n  * Contain no `return` statement, or\n  * Explicit `return` statement(s) all return `None` (explicitly or implicitly).\n\nDefault: `False`\n\n\n## Caveats for PEP 484-style Type Comments\n### Function type comments\nFunction type comments are assumed to contain both argument and return type hints\n\nYes:\n```py\n# type: (int, int) -> bool\n```\n\nNo:\n```py\n# type: (int, int)\n```\n\nPython cannot parse the latter and will raise `SyntaxError: unexpected EOF while parsing`\n\n### Mixing argument type comments and function type comments\nSupport is provided for mixing argument and function type comments, provided that the function type comment use an Ellipsis for the arguments.\n\n```py\ndef foo(\n    arg1,  # type: bool\n    arg2,  # type: bool\n):  # type: (...) -> bool\n    pass\n```\n\nEllipes are ignored by `flake8-annotations` parser.\n\n**Note:** If present, function type comments will override any argument type comments.\n\n### Partial type comments\nPartially type hinted functions are supported\n\nFor example:\n\n```py\ndef foo(arg1, arg2):\n    # type: (bool) -> bool\n    pass\n```\nWill show `arg2` as missing a type hint.\n\n```py\ndef foo(arg1, arg2):\n    # type: (..., bool) -> bool\n    pass\n```\nWill show `arg1` as missing a type hint.\n\n## Contributing\nPlease take some time to read through our [contributing guidelines](CONTRIBUTING.md) before helping us with this project.\n\n### Development Environment\nThis project uses [Poetry](https://python-poetry.org/) to manage dependencies. With your fork cloned to your local machine, you can install the project and its dependencies to create a development environment using:\n\n```bash\n$ poetry install\n```\n\nNote: An editable installation of `flake8-annotations` in the developer environment is required in order for the plugin to be registered for Flake8. By default, Poetry includes an editable install of the project itself when `poetry install` is invoked.\n\nA [pre-commit](https://pre-commit.com) configuration is also provided to create a pre-commit hook so linting errors aren't committed:\n\n```bash\n$ pre-commit install\n```\n\n### Testing & Coverage\nA [pytest](https://docs.pytest.org/en/latest/) suite is provided, with coverage reporting from [pytest-cov](https://github.com/pytest-dev/pytest-cov). A [tox](https://github.com/tox-dev/tox/) configuration is provided to test across all supported versions of Python. Testing will be skipped for Python versions that cannot be found.\n\n```bash\n$ tox\n```\n\nDetails on missing coverage, including in the test suite, is provided in the report to allow the user to generate additional tests for full coverage.\n",
    'author': 'Python Discord',
    'author_email': 'staff@pythondiscord.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pythondiscord.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
