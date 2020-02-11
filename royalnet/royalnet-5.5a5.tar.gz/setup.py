# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['royalnet',
 'royalnet.alchemy',
 'royalnet.backpack',
 'royalnet.backpack.commands',
 'royalnet.backpack.events',
 'royalnet.backpack.stars',
 'royalnet.backpack.tables',
 'royalnet.backpack.utils',
 'royalnet.bard',
 'royalnet.bard.discord',
 'royalnet.commands',
 'royalnet.constellation',
 'royalnet.constellation.api',
 'royalnet.herald',
 'royalnet.serf',
 'royalnet.serf.discord',
 'royalnet.serf.matrix',
 'royalnet.serf.telegram',
 'royalnet.utils']

package_data = \
{'': ['*']}

install_requires = \
['dateparser>=0.7.2,<0.8.0', 'toml>=0.10.0,<0.11.0']

extras_require = \
{'alchemy_easy': ['sqlalchemy>=1.3.10,<2.0.0',
                  'psycopg2_binary>=2.8.4,<3.0.0',
                  'bcrypt>=3.1.7,<4.0.0'],
 'alchemy_hard': ['sqlalchemy>=1.3.10,<2.0.0',
                  'psycopg2>=2.8.4,<3.0.0',
                  'bcrypt>=3.1.7,<4.0.0'],
 'bard': ['ffmpeg_python>=0.2.0,<0.3.0', 'youtube_dl', 'eyed3>=0.9,<0.10'],
 'coloredlogs': ['coloredlogs>=10.0,<11.0'],
 'constellation': ['starlette>=0.12.13,<0.13.0',
                   'uvicorn>=0.10.7,<0.11.0',
                   'python-multipart>=0.0.5,<0.0.6'],
 'discord': ['discord.py>=1.3.1,<2.0.0', 'pynacl>=1.3.0,<2.0.0'],
 'herald': ['websockets>=8.1,<9.0'],
 'matrix': ['matrix-nio>=0.6,<0.7'],
 'sentry': ['sentry_sdk>=0.13.2,<0.14.0'],
 'telegram': ['python_telegram_bot>=12.2.0,<13.0.0']}

setup_kwargs = {
    'name': 'royalnet',
    'version': '5.5a5',
    'description': 'A multipurpose bot and web framework',
    'long_description': '# `royalnet` [![PyPI](https://img.shields.io/pypi/v/royalnet.svg)](https://pypi.org/project/royalnet/)\n\nA multipurpose bot framework and webserver\n\n## About\n\n`royalnet` is a Python framework that allows you to create interconnected modular chat bots accessible through multiple interfaces (such as Telegram or Discord), and also modular websites that can be connected with the bots.\n\n### Supported bot platforms ("serfs")\n\n- [Telegram](https://core.telegram.org/bots)\n- [Discord](https://discordapp.com/developers/docs/)\n- [Matrix](https://matrix.org/) (no E2E support yet)\n\n## Installing\n\nTo install `royalnet`, run:\n```\npip install royalnet\n```\n\nTo install a specific module, run:\n```\npip install royalnet[MODULENAME]\n```\n\nTo install all `royalnet` modules, run:\n```\npip install royalnet[telegram,discord,matrix,alchemy_easy,bard,constellation,sentry,herald,coloredlogs]\n```\n\n## Documentation\n\n`royalnet`\'s documentation is available [here](https://gh.steffo.eu/royalnet).\n\n## Developing `royalnet`\n\nTo develop `royalnet`, you need to have [Poetry](https://poetry.eustace.io/) installed on your PC.\n\nAfter you\'ve installed Poetry, clone the git repo with the command:\n\n```\ngit clone https://github.com/Steffo99/royalnet\n```\n\nThen enter the new directory:\n\n```\ncd royalnet\n```\n\nAnd finally install all dependencies and the package:\n\n```\npoetry install -E telegram -E discord -E matrix -E alchemy_easy -E bard -E constellation -E sentry -E herald -E coloredlogs\n```',
    'author': 'Stefano Pigozzi',
    'author_email': 'ste.pigozzi@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Steffo99/royalnet',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
