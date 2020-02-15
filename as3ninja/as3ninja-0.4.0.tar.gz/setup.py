# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['as3ninja']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'fastapi>=0.48.0,<1',
 'hvac>=0.9.6,<0.10.0',
 'jinja2>=2.10.3,<3.0.0',
 'jsonschema>=3.2.0,<4.0.0',
 'loguru>=0.3.2,<0.4.0',
 'pydantic>=1.2,<2.0',
 'pyyaml>=5.1,<6.0',
 'six>=1.14.0,<2.0.0',
 'uvicorn>=0.10.8,<0.11.0']

entry_points = \
{'console_scripts': ['as3ninja = as3ninja.cli:cli']}

setup_kwargs = {
    'name': 'as3ninja',
    'version': '0.4.0',
    'description': 'AS3 Ninja is a templating and validation engine for your AS3 declarations providing a CLI and Swagger REST API',
    'long_description': "![AS3 Ninja](https://raw.githubusercontent.com/simonkowallik/as3ninja/master/docs/_static/logo.png)\n\n_AS3 Ninja is a templating and validation engine for your AS3 declarations. No matter if you prefer a CLI or Swagger REST API, AS3 Ninja has you covered!_\n\n[![Travis CI Build\nStatus](https://img.shields.io/travis/com/simonkowallik/as3ninja/master?style=flat-square)](https://travis-ci.com/simonkowallik/as3ninja)[![Documentation\nStatus](https://img.shields.io/readthedocs/as3ninja/latest?style=flat-square)](https://as3ninja.readthedocs.io/en/latest/?badge=latest)[![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/simonkowallik/as3ninja?style=flat-square)](https://codeclimate.com/github/simonkowallik/as3ninja)[![Test\nCoverage](https://img.shields.io/codecov/c/github/simonkowallik/as3ninja?style=flat-square)](https://codecov.io/gh/simonkowallik/as3ninja)\n\n- Free software: ISC license\n- Documentation: <https://as3ninja.readthedocs.io>\n- Works with Python 3.7 and up\n\n## What is AS3 Ninja and what can it do for you?\n\nAS3 Ninja is a templating engine as well as a validator for\n[AS3](https://github.com/F5Networks/f5-appsvcs-extension/) declarations.\nIt offers a CLI for local usage, as well as a OpenAPI/Swagger based REST\nAPI.\n\nAS3 Ninja empowers you to create AS3 declarations in a DevOps way by\nembracing the ideas of GitOps and CI/CD.\n\nIt separates Configuration from Code (Templates) as far as YOU wish.\n\nAS3 Ninja let's you decide to scale between declarative and imperative\nparadigms to fit your needs.\n\nWhat AS3 Ninja doesn't do:\n\n- It does not provide you with a UI to create configurations\n- It does not deploy AS3 configurations\n\n## Features\n\n- Validate your AS3 Declarations against the AS3 Schema (via API, eg. for CI/CD)\n- Create AS3 Declarations from templates using the full power of Jinja2 (CLI and API)\n  - reads your JSON or YAML configurations to generate AS3 Declarations\n  - carefully crafted Jinja2 `as3ninja.filters` and `as3ninja.functions` further enhance the templating capabilities\n- Use Git(hub) to pull template configurations and declaration templates\n- HashiCorp Vault integration to retrieve secrets\n- AS3 Ninja provides a simple CLI..\n- ..and a REST API including a Swagger/OpenAPI interface at `/docs` and `/redoc` (openapi.json @ `/openapi.json`)\n\n## AS3 Ninja Interface\n\nSome impressions from AS3 Ninja's interfaces:\n\n### the Command Line\n\n![CLI](https://as3ninja.readthedocs.io/en/latest/_images/_cli.svg)\n\n### the API UI\n\nReDoc and Swagger UI:\n\n![ReDoc](https://raw.githubusercontent.com/simonkowallik/as3ninja/master/docs/_static/_api.gif)\n\nSwagger UI demo:\n\n![Swagger UI](https://raw.githubusercontent.com/simonkowallik/as3ninja/master/docs/_static/_api_demo.gif)\n\n## Disclaimer and Security Note\n\nAS3 Ninja is not a commercial product and [is not covered by any form of support, there is no contract nor SLA!](./docs/support.rst). Please read, understand and adhere to the license before use.\n\nAS3 Ninja's focus is flexibility in templating and features, it is not hardened to run in un-trusted environments.\n\n- It comes with a large set of dependencies, all of them might introduce security issues\n- Jinja2 is not using a Sandboxed Environment and the `readfile` filter allows arbitrary file includes.\n- The API is unauthenticated\n\n> **_WARNING:_**  Only use AS3 Ninja in a trusted environment with restricted access and trusted input.\n\n## Where to start?\n\n[Read the Docs](https://as3ninja.readthedocs.io/) and then [Try it\nout](https://as3ninja.readthedocs.io/en/latest/usage.html)\\! :-)\n",
    'author': 'Simon Kowallik',
    'author_email': 'github@simonkowallik.com',
    'maintainer': 'Simon Kowallik',
    'maintainer_email': 'github@simonkowallik.com',
    'url': 'https://github.com/simonkowallik/as3ninja',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
