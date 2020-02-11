# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['letterboxd_rss']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.7,<5.0', 'feedgen>=0.9.0,<0.10.0', 'requests>=2.21,<3.0']

entry_points = \
{'console_scripts': ['letterboxd-rss = letterboxd_rss.__main__:main']}

setup_kwargs = {
    'name': 'letterboxd-rss',
    'version': '0.2.0',
    'description': 'Generate an RSS feed from your letterboxd.com watchlist',
    'long_description': '# Letterboxd-RSS\n\nConvert your [Letterboxd] Watchlist to an RSS feed.\n\n## Installation\n\nInstall and update using [pip]:\n\n```\npip install letterboxd-rss\n```\n\n## Usage\n\nAfter installing, you may simply call letterboxd-rss from the command line:\n\n```\n$ letterboxd-rss -h\n\nusage: letterboxd-rss [-h] [-o FEED_FILENAME] [-l FEED_LENGTH]\n                      LETTERBOXD_PROFILE\n\npositional arguments:\n  LETTERBOXD_PROFILE    URL of your letterboxd profile\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -o FEED_FILENAME, --output FEED_FILENAME\n                        Destination of the generated RSS feed (defaults to\n                        ./feed.xml)\n  -l FEED_LENGTH, --max-length FEED_LENGTH\n                        Maximum number of watchlist items to keep in the feed\n```\n\n\n[Letterboxd]: https://letterboxd.com\n[pip]: https://pip.pypa.io/en/stable/quickstart/\n',
    'author': 'Jan Willhaus',
    'author_email': 'mail@janwillhaus.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/janw/letterboxd-rss',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
