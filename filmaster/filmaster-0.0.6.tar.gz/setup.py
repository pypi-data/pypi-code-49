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
    'version': '0.0.6',
    'description': 'Discord bot that scours TMDB for film info',
    'long_description': '# Film Master\n\nA Discord bot written with [Snips NLU][]\nthat posts film info via the [TMDB API][].\n\n### Setup\n\nCreate a [Discord app][] for the bot and invite it to your server.\n\nGenerate a [TMDB API][] key for the bot.\n\nInstall the package and run the bot:\n\n```sh\n$ pip install filmaster\n$ filmaster -d "DISCORD_TOKEN" -t "TMDB_API_KEY"\n```\n\nOr, you can use the Docker image:\n\n```sh\n$ docker pull registry.gitlab.com/observeroftime/filmaster:latest\n$ docker run filmaster -d "DISCORD_TOKEN" -t "TMDB_API_KEY"\n```\n\nIn both cases, the bot command requires these parameters:\n\n* `DISCORD_TOKEN`: The bot token of the app you created earlier.\n* `TMDB_API_KEY`: The TMDB API key you generated earlier.\n\nYou may also pass the following options:\n\n* `-p PREFIX`: Sets the command prefix of the bot. (defaults to `$`)\n* `-v`: Increases the verbosity of the logs. Can be passed up to 4 times.\n\n### Examples\n\n#### Greetings\n\n![greeting](https://gitlab.com/ObserverOfTime/filmaster/-/raw/master/.examples/greeting.png)\n\n#### Help\n\n![help](https://gitlab.com/ObserverOfTime/filmaster/-/raw/master/.examples/help.png)\n\n#### Film info\n\n![info-1](https://gitlab.com/ObserverOfTime/filmaster/-/raw/master/.examples/info-1.png)\n\n![info-2](https://gitlab.com/ObserverOfTime/filmaster/-/raw/master/.examples/info-2.png)\n\n![director](https://gitlab.com/ObserverOfTime/filmaster/-/raw/master/.examples/director.png)\n\n![actor](https://gitlab.com/ObserverOfTime/filmaster/-/raw/master/.examples/actor.png)\n\n#### Film cast\n\n![cast-1](https://gitlab.com/ObserverOfTime/filmaster/-/raw/master/.examples/cast-1.png)\n\n![cast-2](https://gitlab.com/ObserverOfTime/filmaster/-/raw/master/.examples/cast-2.png)\n\n### Goodbye\n\n![goodbye](https://gitlab.com/ObserverOfTime/filmaster/-/raw/master/.examples/goodbye.png)\n\n### License\n\n> Licensed under the [Academic Free License version 3.0][AFL-3.0]\n\n\n[TMDB API]: https://developers.themoviedb.org/3/\n[Snips NLU]: https://github.com/snipsco/snips-nlu\n[Discord app]: https://discordapp.com/developers/applications\n[AFL-3.0]: https://gitlab.com/ObserverOfTime/filmaster/-/blob/master/LICENSE.md\n',
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
