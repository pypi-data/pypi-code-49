# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['iredis']

package_data = \
{'': ['*'], 'iredis': ['data/*', 'data/commands/*']}

install_requires = \
['Pygments>=2,<3',
 'click>=7.0,<8.0',
 'configobj>=5.0.6,<6.0.0',
 'mistune>=0.8.4,<0.9.0',
 'pendulum>=2.0.5,<3.0.0',
 'prompt_toolkit>=3,<4',
 'redis>=3,<4']

entry_points = \
{'console_scripts': ['iredis = iredis.entry:main']}

setup_kwargs = {
    'name': 'iredis',
    'version': '0.9.0',
    'description': 'Terminal client for Redis with auto-completion and syntax highlighting.',
    'long_description': '# IRedis (Interactive Redis)\n\n<img align="right" width="100" height="100" src="https://raw.githubusercontent.com/laixintao/iredis/master/docs/assets/logo.png" />\n\n[![CircleCI](https://circleci.com/gh/laixintao/iredis.svg?style=svg)](https://circleci.com/gh/laixintao/iredis)\n[![TravisCI](https://travis-ci.org/laixintao/iredis.svg?branch=master)](https://travis-ci.org/laixintao/iredis)\n[![PyPI version](https://badge.fury.io/py/iredis.svg)](https://badge.fury.io/py/iredis)\n![Python version](https://badgen.net/badge/python/3.6%20|%203.7%20|%203.8/)\n[![Chat on telegram](https://badgen.net/badge/icon/join?icon=telegram&label=usergroup)](https://t.me/iredis_users)\n[![Open in Cloud Shell](https://badgen.net/badge/run/GoogleCloudShell/blue?icon=terminal)](https://console.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/laixintao/iredis&cloudshell_print=docs/cloudshell/run-in-docker.txt)\n\n\nIRedis is a terminal client for redis with auto-completion and syntax highlighting. IRedis let you type Redis command smoothly, and display the response in a user-friendly format.\n\nIRedis is an alternative for redis-cli. In most cases IRedis behaves exactly the same with redis-cli. Besides, it is safer to use IRedis on production server then redis-cli. IRedis will prevent accidently running dangerous command, like `KEYS *`(See [here](https://redis.io/topics/latency), the *Latency generated by slow commands* section. )\n\n![](./docs/assets/demo.svg)\n\n## Features\n\n- Advanced code completion. If you run command `KEYS` then run `DEL`, iredis will auto complete your command based on `KEYS` result.\n- Command validation,(eg. try `CLUSTER MEET IP PORT`, iredis will validate IP and PORT for you)\n- Command highlighting, fully based on redis grammar. Any valide command in iredis shell is a valide redis command.\n- Human friendly response display.\n- <kbd>Ctrl</kbd> + <kbd>C</kbd> to clear cureent line, won\'t exit redis-cli. Use <kbd>Ctrl</kbd> + <kbd>D</kbd>  \n- Say "Goodbye!" to you when you exit!\n- <kbd>Ctrl</kbd> + <kbd>R</kbd> to open **reverse-i-search** to search through command history.\n- Auto suggestions. (Like [fish shell](http://fishshell.com/).)\n- Support `--encode=utf-8`, to decode Redis\' bytes responses.\n- Command hint on bottom, include command syntax, supported redis version, and time complexity.\n- Offcial docs build in `HELP` command, try `HELP SET`!\n- For full features, please see: [iredis.io/show](https://www.iredis.io/show/)\n\n## Install\n\n```\npip install iredis\n```\n\n## Usage\n\nOnce you install IRedis, you will know how to use it. Just remember, IRedis\nsupport similar options like redis-cli, like `-h` for redis-server\'s host\nand `-p` for port. \n\n```\n$ iredis --help\n```\n\nIRedis support config files. The options from command line will always be the\nhighest priority. The config files from high priority to low is:\n\n- *Options from command line*\n- `$PWD/.iredisrc`\n- `~/.iredisrc` (this path can be changed with `iredis --iredisrc $YOUR_PATH`)\n- `/etc/iredisrc`\n- default config in iredis package.\n\nYou can copy the self-explained default config here: \n\nhttps://raw.githubusercontent.com/laixintao/iredis/master/iredis/data/iredisrc\n\nAnd then make your own changes.\n\n## Development\n\n### Release Strategy\n\nThe IRedis project was build and released by CircleCI, whenever a tag was pushed to master branch, a new release will be built and uploaded to pypi.org, it\'s very convenient.\n\nThus, we release as often as possible, so users can always enjoy the new features and bugfixes very quickly. Any bugfix or new feature will get at least a patch release, the big feature will get a minor release.\n\n### Setup Environment\n\niredis favors [poetry](https://github.com/sdispater/poetry) as a packagement tool. You can setup a develop envioment on your computer easily.\n\nFirst, install poetry(You can do it in a python\'s virtualenv):\n\n```\npip install poetry\n```\n\nThen run(which euqals `pip install -e .`):\n\n```\npoetry install\n```\n\n**Be careful running testcases, it may flush you db!!!**\n\n### Development Logs\n\nSince this is a commandline tool, so we didn\'t write logs to stdout.\n\nYou can `tail -f ~/.iredis.log` to see logs, the log is pretty clear,\nyou can see what actually happend from log files.\n\n### CI\n\nWe use [pexpect](https://pexpect.readthedocs.io/en/stable/) to test commandline\nbehavior, since there are problems with circleci\'s tty, so we run\npexpect-related tests on travis, and run unittest/black style check/flake8 check\non circleci.\n\nFor local development, you just run `pytest`, if all tests passed locally, it\nshall be passed on CI.\n\n### Command Reference\n\nThere is a full Redis command list in [commands.csv](docs/commands.csv) file, downloaded by:\n\n```\npython scripts/download_redis_commands.py > data/commands.csv\n```\n\n`commands.csv` is here only for test if redis.io was updated, do not package it into release.\n\nCurrent implemented commands: [command_syntax.csv](iredis/data/command_syntax.csv).\n\n## Planned Features\n\nPlease see issue. And you are welcome to submit one.\n\n## Related Projects\n\n- [redis-tui](https://github.com/mylxsw/redis-tui)\n',
    'author': 'laixintao',
    'author_email': 'laixintao1995@163.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/laixintao/iredis',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
