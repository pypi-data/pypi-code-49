# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['heybrochecklog',
 'heybrochecklog.markup',
 'heybrochecklog.resources',
 'heybrochecklog.score',
 'heybrochecklog.score.modules']

package_data = \
{'': ['*'], 'heybrochecklog.resources': ['eac/*', 'eac95/*']}

install_requires = \
['chardet>=3.0.4,<4.0.0']

entry_points = \
{'console_scripts': ['heybrochecklog = heybrochecklog.__main__:runner']}

setup_kwargs = {
    'name': 'heybrochecklog',
    'version': '1.3.2',
    'description': 'A python tool for evaluating and working with EAC/XLD rip logs.',
    'long_description': "# hey-bro-check-log\n\n[![Build Status](https://travis-ci.org/ligh7s/hey-bro-check-log.svg?branch=master)](https://travis-ci.org/ligh7s/hey-bro-check-log)\n\nA python tool which analyzes and verifies good ripping practices and potential inaccuracies\nin CD ripping logs.\n\n## Support\n\n- Supports checking EAC and XLD logs.\n- Matches deductions on Redacted (minus stupid aggregate ones)\n- Supports combined EAC logs\n- Detects other irregularities and special occurrences in the rip\n  - Data tracks\n  - Irregular AR results\n  - Hidden tracks and extraction\n- Foreign language support (temperamental, as it's based on the most recent translation files).\n\n## Running CLI\n\n```\nusage: heybrochecklog [-h] [-t] [-m] [-s] log\n\nTool to analyze, translate, and score a CD Rip Log.\n\npositional arguments:\n  log               log file to check.\n\noptional arguments:\n  -h, --help        show this help message and exit\n  -t, --translate   translate a foreign log to English\n  -m, --markup      print the marked up version of the log after analyzing\n  -s, --score-only  Only print the score of the log.\n```\n",
    'author': 'lights',
    'author_email': 'lights@tutanota.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ligh7s/hey-bro-check-log',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
