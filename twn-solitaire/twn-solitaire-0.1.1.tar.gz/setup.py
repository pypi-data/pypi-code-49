# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['twn_solitaire']

package_data = \
{'': ['*'], 'twn_solitaire': ['assets/Jellee-Roman/*']}

install_requires = \
['pygame>=1.9.6,<2.0.0', 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['twn_solitaire = twn_solitaire.run:main']}

setup_kwargs = {
    'name': 'twn-solitaire',
    'version': '0.1.1',
    'description': 'Generic version of 2048 Solitaire. Simple, fun and satisfying game.',
    'long_description': "<pre>\n  ___  _ __     _____       _ _ _        _\n |__ \\| '_ \\   / ____|     | (_) |      (_)\n    ) |_| |_| | (___   ___ | |_| |_ __ _ _ _ __ ___\n   / /         \\___ \\ / _ \\| | | __/ _` | | '__/ _ \\\n  / /_         ____) | (_) | | | || (_| | | | |  __/\n |____|       |_____/ \\___/|_|_|\\__\\__,_|_|_|  \\___|\n\n</pre>\n\n[![Build Status](https://travis-ci.com/geckon/2-n_solitaire.svg?branch=master)](https://travis-ci.com/geckon/2-n_solitaire)\n[![Codacy Badge](https://api.codacy.com/project/badge/Grade/37d712df43e44d6487bb35e015c27c47)](https://app.codacy.com/app/geckon/2-n_solitaire?utm_source=github.com&utm_medium=referral&utm_content=geckon/2-n_solitaire&utm_campaign=Badge_Grade_Dashboard)\n[![Total alerts](https://img.shields.io/lgtm/alerts/g/geckon/2-n_solitaire.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/geckon/2-n_solitaire/alerts/)\n[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/geckon/2-n_solitaire.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/geckon/2-n_solitaire/context:python)\n[![Updates](https://pyup.io/repos/github/geckon/2-n_solitaire/shield.svg)](https://pyup.io/repos/github/geckon/2-n_solitaire/)\n\n2<sup>n</sup> Solitaire (or TWN Solitaire) is a simple game inspired by\n2048 Solitaire (but more generic) which is inspired by 2048 (but instead of\ntiles in a grid you collect cards here). I find the game fun and\nsatisfying and thus I decided to try and implement it using Pygame. Here we are.\n\nThe goal of the game is to stack an endless row of cards into limited-size\ncolumns. Each time you stack two cards of the same value one on the other,\nthe two cards are replaced by one of double the value and your score grows.\nCards with the maximum value (configurable, see below) will disappear.\nThe game ends once all the columns are full and so no more cards can be played.\n\n### Controls\n\n![Screenshot](https://github.com/geckon/2-n_solitaire/blob/master/docs/screenshot.png)\n\nThis is what the game looks like. At the top you can see your current score,\nbelow that is the main board where the cards are stacked. In the bottom part you\ncan see two next cards that will come to the game. You can use `1`, `2`, `3` and\n`4` keys to place the next upcoming card to the respective column.\n\nThat's it. Simple, eh?\n\n### Configuration\n\nThere are some configurable options - see\nthe [default config file](.2-n_solitaire.conf). All options should be described\nthere including default values which will be used if not specified otherwise.\nThe game will search for the configuration file in the following locations\n(in this order):\n\n-   current working directory\n\n-   home directory\n\n-   directory specified by TWN_SOLITAIRE_CONF_DIR environment\n    variable\n\n### Current state\n\nThe game works but doesn't do anything fancy or look fancy yet.\n\n### Future plans\n\n-   High score recording\n-   Special cards?\n-   Limited swapping *next cards*?\n-   Limited discarding *next cards*?\n-   Saving game state on exit?\n-   Better *graphics*?\n-   Mouse support?\n\nSee/add issues if interested in anything particular.\n",
    'author': 'Tomáš Heger',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/geckon/2-n_solitaire',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
