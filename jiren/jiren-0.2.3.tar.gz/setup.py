# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jiren']

package_data = \
{'': ['*']}

install_requires = \
['jinja2>=2.11,<3.0', 'nestargs>=0.4.2,<0.5.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.5,<2.0']}

entry_points = \
{'console_scripts': ['jiren = jiren.cli:main']}

setup_kwargs = {
    'name': 'jiren',
    'version': '0.2.3',
    'description': 'jinja2 template renderer',
    'long_description': '# jiren\n\njiren is an application that generates text from a template. The format of the template is based on jinja2.\n\n[![PyPI](https://img.shields.io/pypi/v/jiren.svg)](https://pypi.org/project/jiren/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jiren.svg)](https://pypi.org/project/jiren/)\n[![Build Status](https://travis-ci.com/speg03/jiren.svg?branch=master)](https://travis-ci.com/speg03/jiren)\n[![codecov](https://codecov.io/gh/speg03/jiren/branch/master/graph/badge.svg)](https://codecov.io/gh/speg03/jiren)\n\nRead this in Japanese: [日本語](https://github.com/speg03/jiren/blob/master/README.ja.md)\n\n## Installation\n\n```sh\npip install jiren\n```\n\n## Usage\n\n### Generate text\n\nGenerate text from a template using the `jiren` command. This command can read a template from stdin or files.\n\nAn example of reading a template from stdin:\n\nCommand:\n```sh\necho "hello, {{ name }}" | jiren --var.name=world\n```\nOutputs:\n```\nhello, world\n```\n\nAn example of reading a template from a file:\n\nCommand:\n```sh\ncat <<EOF >template.j2\nhello, {{ name }}\nEOF\n\njiren template.j2 --var.name=world\n```\nOutputs:\n```\nhello, world\n```\n\nIn this example, the template contains a variable called `name`. You can set values for variables in a template using program arguments passed to the `jiren` command. Note that the program arguments must be prefixed with `--var.`.\n\nIf you want to know more about template format, please refer to jinja2 document ( http://jinja.pocoo.org/ ).\n\n\n### Variables in a template\n\nYou can use the help to check the variables defined in a template.\n\nCommand:\n```sh\necho "{{ greeting }}, {{ name }}" | jiren --help\n```\nOutputs:\n```\n... (omitted)\n\nvariables:\n  --var.name VAR.NAME\n  --var.greeting VAR.GREETING\n```\n\n\n### Default values\n\nYou can set default values for variables for which no values was specified. This is based on the jinja2 specification.\n\nCommand:\n```sh\necho "{{ greeting }}, {{ name | default(\'world\') }}" | jiren --var.greeting=hello\n```\nOutputs:\n```\nhello, world\n```\n\n\n### Strict option\n\nWhen using the `--strict` option, you must specify values for all variables.\n\nCommand:\n```sh\necho "{{ greeting }}, {{ name }}" | jiren --strict --var.greeting=hello\n```\nOutputs:\n```\n... (omitted)\n\njiren: error: the following arguments are required: --var.name\n```\n',
    'author': 'Takahiro Yano',
    'author_email': 'speg03@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/speg03/jiren',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
