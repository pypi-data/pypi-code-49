# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['escarpolette',
 'escarpolette.admin',
 'escarpolette.migrations',
 'escarpolette.models',
 'escarpolette.routers',
 'escarpolette.rules',
 'escarpolette.schemas']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'fastapi>=0.47.1,<0.48.0',
 'importlib_metadata>=1.5.0,<2.0.0',
 'pydantic>=1.3,<2.0',
 'pyjwt>=1.7.1,<2.0.0',
 'sqlalchemy>=1.2,<2.0',
 'uvicorn>=0.11.2,<0.12.0',
 'xdg>=4.0,<5.0',
 'youtube-dl']

entry_points = \
{'console_scripts': ['escarpolette = escarpolette:__main__']}

setup_kwargs = {
    'name': 'escarpolette',
    'version': '0.7.1',
    'description': 'Manage your musical playlist with your friends without starting a war.',
    'long_description': "# Escarpolette\n\nThis project provides a server and clients to manage your music playlist when you are hosting a party.\n\nIt supports many sites thanks to the awesome project [youtube-dl](https://rg3.github.io/youtube-dl/).\n\n## Features\n\nServer:\n* add items (and play them!)\n* get playlist's items\n* runs on Android! (see [instructions](#Android))\n\nWeb client:\n* there is currently no web client :(\n\n## Dependencies\n\n* Python 3.7\n* the player [mpv](https://mpv.io)\n\nThey should be available for most of the plateforms.\n\n\n## Installation\n\n```Shell\npip install escarpolette\n```\n\n### Android\n\nYou will need [Termux](https://termux.com/).\nThen inside Termux you can install it with:\n\n```Shell\n# dependencies\npkg install python python-dev clang mpv\n# escarpolette\npip install escarpolette\n```\n\nNote that while the project can run without wake-lock, acquiring it improve the performance (with a battery trade off).\n\n## Usage\n\n```Shell\nescarpolette [--config config.cfg] [--host host] [--port port] [--help]\n```\n\nThe default configuration should be good for all the usages.\n\n## Dev\n\nYou will need [Poetry](https://poetry.eustace.io/) to manage the dependencies.\n\nClone the repo and then type `poetry install`.\nYou can run the app with `poetry run python -m escarpolette`.\n\n## Todo\n\n* server\n    * votes\n    * bonjour / mDNS\n    * prevent adding youtube / soundcloud playlists\n    * restrictions by users\n    * configuration of those restrictions by an admin\n* web client\n    * show playing status\n    * votes\n    * configure restrictions:\n        * max video added per user\n        * max video length\n    * admin access:\n        * configure restrictions\n        * no restrictions for him\n        * force video order\n\nMaybe one day?\n* android client\n* iOS client\n",
    'author': 'Alexandre Morignot',
    'author_email': 'erdnaxeli@cervoi.se',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/erdnaxeli/escarpolette',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
