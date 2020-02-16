# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blue_chip', 'blue_chip.config', 'blue_chip.tasks']

package_data = \
{'': ['*']}

install_requires = \
['black==19.10b0', 'invoke', 'isort', 'prospector[with_pyroma]>=1.2.0,<2.0.0']

entry_points = \
{'console_scripts': ['bc = blue_chip.__main__:program.run',
                     'bcp = blue_chip.__main__:program.run']}

setup_kwargs = {
    'name': 'blue-chip',
    'version': '0.0.6',
    'description': 'One click Python code quality package',
    'long_description': '[![PyPI version](https://badge.fury.io/py/blue-chip.svg)](https://badge.fury.io/py/blue-chip)\n[![Build Status](https://travis-ci.com/Kilo59/blue-chip.svg?branch=master)](https://travis-ci.com/Kilo59/blue-chip)\n[![Coverage Status](https://coveralls.io/repos/github/Kilo59/blue-chip/badge.svg?branch=master)](https://coveralls.io/github/Kilo59/blue-chip?branch=master)\n[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Kilo59/blue-chip.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Kilo59/blue-chip/context:python)\n[![Total alerts](https://img.shields.io/lgtm/alerts/g/Kilo59/blue-chip.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Kilo59/blue-chip/alerts/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n\n# blue-chip\nOne click Python code quality package\n\n`blue-chip` uses [`black`](https://github.com/ambv/black), [`isort`](https://github.com/timothycrosley/isort), [`invoke`](http://www.pyinvoke.org/) and [`prospector`](https://prospector.readthedocs.io/en/master/) configured to work well together out of the box.\n\n-----------------------\n## Install\n\nThe recommended installation method is to use [`pipx`](https://github.com/pipxproject/pipx)\n```\npipx install blue-chip\n```\nOr use `pip`\n```\npip install blue-chip --user\n```\n\n## Command-line use\n\nList the possible `blue-chip` commands with `bc --list`\n```\n$bc --list\n\nSubcommands:\n\n  fmt    Format python source code.\n  lint   Run static analysis on python source code.\n  sort   Sort module imports.\n```\n\n----------------------\n\n## Enterprise use\nEnterprise teams may find it useful to fork and redistribute this package with their own custom defined standards.\n\n\nIn many cases this is a simple as changing the package name and values in [`blue_chip/constants.py`](https://github.com/Kilo59/blue-chip/blob/master/blue_chip/constants.py).\n\nFor fine grain control of the static analysis tools, edit the `prospector` profiles in [`blue_chip/lint_config`](https://github.com/Kilo59/blue-chip/blob/master/blue_chip/lint_config).\n',
    'author': 'Gabriel Gore',
    'author_email': 'gabriel59kg@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Kilo59/blue-chip',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
