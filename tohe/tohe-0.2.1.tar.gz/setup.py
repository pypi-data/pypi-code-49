# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tohe', 'tohe.db', 'tohe.log', 'tohe.util']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.3,<0.5.0']

entry_points = \
{'console_scripts': ['tohe = tohe.cli:main']}

setup_kwargs = {
    'name': 'tohe',
    'version': '0.2.1',
    'description': 'tohe - The friendly TODO list helper',
    'long_description': '# tohe\ntohe - the TODO list helper\n\n# Install\n```sh\npip3 install tohe\n```\n\n# Usage\n## General usage information\n### Tags\nTags can be supplied via `-t TAG1 TAG2`.\nOperations that add tags also expect tags in the form `-t TAG1 TAG2`.\nOperations that remove tags work similar, but expect the flag `-r`, like `-r REMOVETAG1 REMOVETAG2`.\n\n## Supported operations:\n* **add**\n```sh\ntohe add [-t TAG [TAG ...]] [CONTENT]\n```\nIf `CONTENT` is not provided, `$EDITOR` will be opened to get content for the entry.\n\n* **list**\n```sh\ntohe list [-t TAG [TAG ...]]\n```\n*Not supported yet*: Tag filtering\n\n* **edit**\n```sh\ntohe edit [-t TAGS [TAGS ...]] [-r RTAGS [RTAGS ...]] ID\n```\n\n* **search**\n```sh\ntohe search [-w] TERM\n```\n`-w|--wildcard` enables the use of `*` and `?` wildcards\n\n* **delete**\n```sh\ntohe delete ID\n```\n\n# Development\n## Setup\n```sh\npoetry install\n```\n\n## Unit tests\n```sh\npoetry run pytest --cov=tohe/ tests/\n# or\npoetry run python -m pytest --cov=tohe/ tests/\n```\n\n### mypy\n```sh\npoetry run mypy tohe/\n# or\npoetry run python -m mypy tohe/\n```\n\n\n## TODO\n- [ ] Add support for currently unsupported options like `-db` and `--loglevel`.\n- [ ] Add Bash and Zsh completion\n- [ ] Add docstrings\n- [ ] Maybe enable tag editing in the editor (i.e. `tags: main,todo,test`)\n- [ ] Build a web server around it for easier reading and editing\n- [ ] Add fzf support for searching\n- [ ] Add ncurses TUI\n',
    'author': 'Lukas Deutz',
    'author_email': 'lukas.deutz@mailfence.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
