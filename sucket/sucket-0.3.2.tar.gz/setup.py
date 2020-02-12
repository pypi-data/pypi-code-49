# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sucket']

package_data = \
{'': ['*']}

install_requires = \
['aiobotocore>=0.11.1,<0.12.0',
 'click>=7.0,<8.0',
 'typing_extensions>=3.7.4,<4.0.0']

entry_points = \
{'console_scripts': ['sucket = sucket:sucket']}

setup_kwargs = {
    'name': 'sucket',
    'version': '0.3.2',
    'description': 'A tool to get all files from an S3 bucket',
    'long_description': '# Sucket\n\nA tool to download all objects from an S3 bucket. Supports filtering keys by a prefix.\n\n## Help\n\n```\n-> % sucket --help\nUsage: sucket [OPTIONS] BUCKET_NAME [PREFIX]\n\n  Download all files from a S3 bucket\n\n  Everything from the bucket BUCKET_NAME is downloaded, with an optional key\n  filter, specified with PREFIX\n\n  By default the "folder" mode is used, which will keep the bucket "folder\n  structure" when downloading.\n\n  The "flat" mode will download all objects into the current folder by\n  adding the folder structure into the key name.\n\n  The "keys-only" will completely disregard the folders and put all files in\n  the current folder.\n\nOptions:\n  -m, --mode [folder|flat|keys-only]\n                                  The structure to download the objects in.\n  -y, --yes                       Don\'t prompt for continuing\n  -q, --quiet                     Don\'t print out any info, assumes --yes\n  -s, --semaphores INTEGER        Max number of asynchronous requests to make.\n                                  Default: 1000\n  --help                          Show this message and exit.\n```\n\n## Examples\n\n![folder](.github/examples/folder.png)\n![flat](.github/examples/flat.png)\n![keys-only](.github/examples/keys-only.png)\n\n## Notes\n\nThis has only been tested on a fairly limited set of data, but has worked well\nfor ~3500 small files. Need to tweak and experiment with larger files.\n\n# Special thanks\n\nThis is heavily based on a script that [@steinnes](https://github.com/steinnes) wrote some time ago and has\nbeen very useful to me for a long time, the name was entirely his idea.\n',
    'author': 'Axel',
    'author_email': 'sucket@absalon.is',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ikornaselur/sucket',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
