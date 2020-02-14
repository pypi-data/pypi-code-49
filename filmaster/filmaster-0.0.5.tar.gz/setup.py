# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['filmaster']

package_data = \
{'': ['*']}

install_requires = \
['discord.py>=1.3.1,<2.0.0', 'isle>=0.6.0,<0.7.0', 'snips-nlu>=0.20.2,<0.21.0']

entry_points = \
{'console_scripts': ['filmaster = filmaster.__main__:run']}

setup_kwargs = {
    'name': 'filmaster',
    'version': '0.0.5',
    'description': 'Discord bot that scours TMDB for film info',
    'long_description': '# Film Master\n\nA Discord bot written with [Snips NLU][]\nthat posts film info via the [TMDB API][].\n\n### Setup\n\nCreate a [Discord app][] for the bot and invite it to your server.\n\nGenerate a [TMDB API][] key for the bot.\n\nInstall `filmaster`:\n\n```sh\n$ pip install filmaster\n```\n\nRun the bot:\n\n```sh\n$ filmaster -d "DISCORD_TOKEN" -t "TMDB_API_KEY"\n```\n\nThe command requires these parameters:\n\n* `DISCORD_TOKEN`: The bot token of the app you created earlier.\n* `TMDB_API_KEY`: The TMDB API key you generated earlier.\n\nYou may also pass the following options:\n\n* `-p PREFIX`: Sets the command prefix of the bot.\n  `PREFIX` must be a single character and defaults to `$`.\n* `-v`: Increases the verbosity of the logs. Can be passed up to 4 times.\n\n### Examples\n\n#### Greetings\n\n![greeting](.examples/greeting.png)\n\n#### Help\n\n![help](.examples/help.png)\n\n#### Film info\n\n![info-1](.examples/info-1.png)\n\n![info-2](.examples/info-2.png)\n\n![director](.examples/director.png)\n\n![actor](.examples/actor.png)\n\n#### Film cast\n\n![cast-1](.examples/cast-1.png)\n\n![cast-2](.examples/cast-2.png)\n\n### Goodbye\n\n![goodbye](.examples/goodbye.png)\n\n### License\n\n> Licensed under the [Academic Free License version 3.0][AFL-3.0]\n\n\n[TMDB API]: https://developers.themoviedb.org/3/\n[Snips NLU]: https://github.com/snipsco/snips-nlu\n[Discord app]: https://discordapp.com/developers/applications\n[AFL-3.0]: https://gitlab.com/ObserverOfTime/filmaster/-/blob/master/LICENSE.md\n',
    'author': 'ObserverOfTime',
    'author_email': 'chronobserver@disroot.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/ObserverOfTime/filmaster',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
