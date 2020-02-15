# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pixi']

package_data = \
{'': ['*'], 'pixi': ['migrations/*']}

install_requires = \
['appdirs>=1.4,<2.0',
 'click>=7.0,<8.0',
 'pixiv-api>=0.3.0,<0.4.0',
 'tqdm>=4.32,<5.0']

entry_points = \
{'console_scripts': ['pixi = pixi.__main__:run']}

setup_kwargs = {
    'name': 'pixi',
    'version': '1.0.0',
    'description': 'A command line tool to download images from Pixiv.',
    'long_description': '# pixi\n\n[![Build Status](https://travis-ci.org/azuline/pixi.svg?branch=master)](https://travis-ci.org/azuline/pixi)\n[![Coverage Status](https://coveralls.io/repos/github/azuline/pixi/badge.svg?branch=master)](https://coveralls.io/github/azuline/pixi?branch=master)\n[![Pypi](https://img.shields.io/pypi/v/pixi.svg)](https://pypi.python.org/pypi/pixi)\n[![Pyversions](https://img.shields.io/pypi/pyversions/pixi.svg)](https://pypi.python.org/pypi/pixi)\n\nA command line tool to download illustrations from Pixiv.\n\n```\nUsage: pixi [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  artist     Download illustrations of an artist by URL or ID.\n  auth       Log into Pixiv and generate a refresh token.\n  bookmarks  Download illustrations bookmarked by a user.\n  config     Edit the config file.\n  failed     View illustrations that failed to download.\n  illust     Download an illustration by URL or ID.\n  migrate    Upgrade the database to the latest migration.\n  wipe       Wipe the saved history of downloaded illustrations.\n```\n\n## Usage\n\nThis tool can be installed from PyPI as `pixi`.\n\n```sh\n$ pip install --user pixi\n```\n\nAfter installation, create the database and configure pixi with the following\ncommands.\n\n```sh\n$ pixi migrate  # Migrate the database\n$ pixi config  # Configure pixi\n```\n\nRefer to the [configuration section](#Configuration) for details on the various\nconfiguration options.\n\nNow you can begin downloading!\n\nFor example, the following commands download an illustration. pixi accepts both\na URL to the illustration as well as just the illustration ID. The same applies\nto all inputs that accept ID values.\n\n```sh\n$ pixi illustration https://www.pixiv.net/member_illust.php?mode=medium&illust_id=64930973\n```\n\n```sh\n$ pixi illustration 64930973\n```\n\nDownloading all the illustrations of an artist can be done with the following\ncommand.\n\n```sh\n$ pixi artist https://www.pixiv.net/member.php?id=2188232\n```\n\nBookmarks, public and private, can be downloaded with the following command.\n\n```sh\n$ pixi bookmarks\n```\n\nThe public bookmarks of other users can also be downloaded.\n\n```sh\n$ pixi bookmarks --user https://www.pixiv.net/member.php?id=2188232\n```\n\nAnd the following command downloads all bookmarks matching a user-assigned\nbookmark tag.\n\n```sh\n$ pixi bookmarks --tag "has cats"\n```\n\nTo view all the options available to a specific command, run the command with\nthe `--help` flag. For example, `illustration`\'s options can be viewed with the\nfollowing command.\n\n```sh\n$ pixi --help illustration\n```\n\nWhen downloading many images from an artist or a user\'s bookmarks, an image\ncan occasionally fail to download. If an image fails to download after several\nretries, it will be recorded and skipped. Failed images can be viewed with the\nfollowing command.\n\n```sh\n$ pixi failed\n```\n\nIf an image on the failed list is successfully downloaded, it will\nautomatically be removed from the list. To wipe the entire failed list, the\nfollowing command should be run.\n\n```sh\n$ pixi wipe --table=failed\n```\n\npixi also keeps track of which illustrations have been downloaded and will avoid\ndownloading duplicate illustrations. However, if you wish to re-download\nillustrations, pass the `--allow-duplicates` (or `-a`) flag.\n\nBy default, illustration downloads will be tracked if they are downloaded to\nthe default downloads directory and not tracked if they aren\'t. This behavior\ncan be manually set with the `--track/--no-track` (or `-t/-T`) flag.\n\nIf you wish to wipe the database of tracked downloads, run the following\ncommand and confirm the action.\n\n```sh\n$ pixi wipe --table=downloads\n```\n\n## Configuration\n\nThe configuration file is in `ini` format. A demo configuration is included\nbelow. To run pixi, a default download directory must be configured.\n\n```ini\n[pixi]\n; Leave this blank; the script will auto-populate it.\nrefresh_token =\n; The default directory for illustrations to be downloaded to.\ndownload_directory = /home/azuline/images/pixiv\n```\n',
    'author': 'azuline',
    'author_email': 'azuline@riseup.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/azuline/pixi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
