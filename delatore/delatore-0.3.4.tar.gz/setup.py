# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['delatore',
 'delatore.configuration',
 'delatore.outputs',
 'delatore.outputs.telegram',
 'delatore.sources']

package_data = \
{'': ['*'], 'delatore.configuration': ['resources/*']}

install_requires = \
['aiodns>=2.0.0,<3.0.0',
 'aiogram>=2.5.3,<3.0.0',
 'aiohttp-socks>=0.3.4,<0.4.0',
 'aiohttp>=3.6.2,<4.0.0',
 'apubsub>=0.2.1,<0.3.0',
 'influxdb>=5.2.3,<6.0.0',
 'ocomone>=0.4.3,<0.5.0',
 'pyyaml-typed>=0.1.0,<0.2.0']

setup_kwargs = {
    'name': 'delatore',
    'version': '0.3.4',
    'description': 'Telegram bot for CSM jobs notifications',
    'long_description': '# Delatore\n[![Build Status](https://travis-ci.org/opentelekomcloud-infra/delatore.svg?branch=master)](https://travis-ci.org/opentelekomcloud-infra/delatore)\n[![codecov](https://codecov.io/gh/opentelekomcloud-infra/delatore/branch/master/graph/badge.svg)](https://codecov.io/gh/opentelekomcloud-infra/delatore)\n[![PyPI version](https://img.shields.io/pypi/v/delatore.svg)](https://pypi.org/project/delatore/)\n![GitHub](https://img.shields.io/github/license/opentelekomcloud-infra/delatore)\n\nMonitor and report status of customer service monitoring scenarios\n\n## Bot commands\n\nTelegram bot accepts following commands:\n\n### `/status`\nBot reply to the message with last status(-es) retrieved from given source\n\nStatus has following syntax:\n\n`/status <source> [detailed_source] [history_depth]`\n\nIf some argument contains spaces, it should be surrounded by quotes, either `\'...\'` or `"..."`\n\n#### AWX Source\n\nStatus command for AWX source has following syntax:\n\n`/status awx [template_name] [history_depth]`\n\nExamples:\n - `/status awx` — return last job status for all _scenarios_\n - `/status awx \'Buld test host\'` — return last job status for AWX template which called \'Buld test host\'\n - `/status awx \'Scenario 1.5\' 3` — return status of last 3 jobs for AWX template which called  `Scenario 1.5`\n',
    'author': 'OTC customer service monitoring team',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/opentelekomcloud-infra/delatore',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
