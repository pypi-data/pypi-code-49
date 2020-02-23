# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['manjaro_torrent_find']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2', 'lxml>=4.5.0,<5.0.0', 'requests>=2.23.0,<3.0.0']

entry_points = \
{'console_scripts': ['mtf = manjaro_torrent_find.mtf:goBabe']}

setup_kwargs = {
    'name': 'manjaro-torrent-find',
    'version': '0.1.2',
    'description': 'Searches the OSDN Manjaro project for torrent files and downloads them.',
    'long_description': "Manjaro Torrent Find\n====================\n\nReads the RSS feed from osdn.net/projects/manjaro/storage/!rss and parses out the\n.torrent, .sig, .sha1 and .sha256 files. It then attempts to download them to the\ncurrent directory.\n\nInstallation\n------------\n\nAvailable from pypi, so `pip3 install manjaro-torrent-find --user` should suffice.\nYou'll then have a new command at `$HOME/.local/bin/mtf` so add that dir to your path.\n\nUsage\n-----\n\nOnce the local python scripts directory is on your path, just execute `mtf`.\n",
    'author': 'Chris Allison',
    'author_email': 'chris.charles.allison+mtf@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': '',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
