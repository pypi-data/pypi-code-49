# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_utils']

package_data = \
{'': ['*']}

install_requires = \
['fastapi', 'pydantic>=1.0,<2.0', 'sqlalchemy>=1.3.12,<2.0.0']

setup_kwargs = {
    'name': 'fastapi-utils',
    'version': '0.1.1',
    'description': 'Reusable utilities for FastAPI',
    'long_description': '<p align="center">\n    <em>Reusable utilities for FastAPI</em>\n</p>\n<p align="center">\n<img src="https://img.shields.io/github/last-commit/dmontagu/fastapi-utils.svg">\n<a href="https://github.com/dmontagu/fastapi-utils" target="_blank">\n    <img src="https://github.com/dmontagu/fastapi-utils/workflows/build/badge.svg" alt="Build">\n</a>\n<a href="https://codecov.io/gh/dmontagu/fastapi-utils" target="_blank">\n    <img src="https://codecov.io/gh/dmontagu/fastapi-utils/branch/master/graph/badge.svg" alt="Coverage">\n</a>\n<a href="https://app.netlify.com/sites/trusting-archimedes-72b369/deploys">\n    <img src="https://img.shields.io/netlify/28b2a077-65b1-4d6c-9dba-13aaf6059877" alt="Netlify status">\n</a>\n<br />\n<a href="https://pypi.org/project/fastapi-utils" target="_blank">\n    <img src="https://badge.fury.io/py/fastapi-utils.svg" alt="Package version">\n</a>\n    <img src="https://img.shields.io/pypi/pyversions/fastapi-utils.svg">\n    <img src="https://img.shields.io/github/license/dmontagu/fastapi-utils.svg">\n</p>\n\n---\n\n**Documentation**: <a href="https://fastapi-utils.davidmontague.xyz" target="_blank">https://fastapi-utils.davidmontague.xyz</a>\n\n**Source Code**: <a href="https://github.com/dmontagu/fastapi-utils" target="_blank">https://github.com/dmontagu/fastapi-utils</a>\n\n---\n\n<a href="https://fastapi.tiangolo.com">FastAPI</a> is a modern, fast web framework for building APIs with Python 3.6+.\n\nBut if you\'re here, you probably already knew that!\n\n---\n\n## Features\n\nThis package includes a number of utilities to help reduce boilerplate and reuse common functionality across projects:\n\n* **Class Based Views**: Stop repeating the same dependencies over and over in the signature of related endpoints.\n* **Response-Model Inferring Router**: Let FastAPI infer the `response_model` to use based on your return type annotation. \n* **Repeated Tasks**: Easily trigger periodic tasks on server startup\n* **Timing Middleware**: Log basic timing information for every request\n* **SQLAlchemy Sessions**: The `FastAPISessionMaker` class provides an easily-customized SQLAlchemy Session dependency \n* **OpenAPI Spec Simplification**: Simplify your OpenAPI Operation IDs for cleaner output from OpenAPI Generator\n\n---\n\nIt also adds a variety of more basic utilities that are useful across a wide variety of projects:\n\n* **APIModel**: A reusable `pydantic.BaseModel`-derived base class with useful defaults\n* **APISettings**: A subclass of `pydantic.BaseSettings` that makes it easy to configure FastAPI through environment variables \n* **String-Valued Enums**: The `StrEnum` and `CamelStrEnum` classes make string-valued enums easier to maintain\n* **CamelCase Conversions**: Convenience functions for converting strings from `snake_case` to `camelCase` or `PascalCase` and back\n* **GUID Type**: The provided GUID type makes it easy to use UUIDs as the primary keys for your database tables\n\nSee the [docs](https://fastapi-utils.davidmontague.xyz/) for more details and examples. \n\n## Requirements\n\nThis package is intended for use with any recent version of FastAPI (depending on `pydantic>=1.0`), and Python 3.6+.\n\n## Installation\n\n```bash\npip install fastapi-utils\n```\n\n## License\n\nThis project is licensed under the terms of the MIT license.\n',
    'author': 'David Montague',
    'author_email': 'davwmont@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://fastapi-utils.davidmontague.xyz',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
