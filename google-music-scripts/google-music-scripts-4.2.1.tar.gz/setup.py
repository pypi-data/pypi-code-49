# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['google_music_scripts']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.0,<2.0',
 'attrs>=18.2,<19.4',
 'audio-metadata>=0.6,<0.7',
 'google-music-proto>=2.5.1,<3.0.0',
 'google-music-utils>=2.1,<3.0',
 'google-music>=3.2,<4.0',
 'loguru>=0.4.0,<0.5.0',
 'natsort>=5.0,<7.0',
 'pendulum>=2.0,<3.0',
 'pprintpp<1.0.0',
 'tbm-utils>=2.0.2,<3.0.0',
 'tomlkit>=0.5,<0.6']

extras_require = \
{'dev': ['flake8>=3.5,<4.0',
         'flake8-builtins>=1.0,<2.0',
         'flake8-comprehensions>=2.0,<=4.0',
         'flake8-import-order>=0.18,<0.19',
         'flake8-import-order-tbm>=1.0,<2.0',
         'nox>=2019,<2020',
         'sphinx>=2.0,<3.0',
         'sphinx-argparse>=0.2,<0.3',
         'sphinx-material<1.0.0'],
 'doc': ['sphinx>=2.0,<3.0',
         'sphinx-argparse>=0.2,<0.3',
         'sphinx-material<1.0.0'],
 'lint': ['flake8>=3.5,<4.0',
          'flake8-builtins>=1.0,<2.0',
          'flake8-comprehensions>=2.0,<=4.0',
          'flake8-import-order>=0.18,<0.19',
          'flake8-import-order-tbm>=1.0,<2.0']}

entry_points = \
{'console_scripts': ['gms = google_music_scripts.cli:run']}

setup_kwargs = {
    'name': 'google-music-scripts',
    'version': '4.2.1',
    'description': 'A CLI utility for interacting with Google Music.',
    'long_description': '# google-music-scripts\n\n[![PyPI](https://img.shields.io/pypi/v/google-music-scripts.svg?label=PyPI)](https://pypi.org/project/google-music-scripts/)\n![](https://img.shields.io/badge/Python-3.6%2B-blue.svg)  \n[![GitHub CI](https://img.shields.io/github/workflow/status/thebigmunch/google-music-scripts/CI?label=GitHub%20CI)](https://github.com/thebigmunch/google-music-scripts/actions?query=workflow%3ACI)  \n[![Docs - Stable](https://img.shields.io/readthedocs/google-music-scripts/stable.svg?label=Docs%20%28Stable%29)](https://google-music-scripts.readthedocs.io/en/stable/)\n[![Docs - Latest](https://img.shields.io/readthedocs/google-music-scripts/latest.svg?label=Docs%20%28Latest%29)](https://google-music-scripts.readthedocs.io/en/latest/)\n\n[google-music-scripts](https://github.com/thebigmunch/google-music-scripts)\nis a CLI utility for interacting with Google Music using my alternative to\ngmusicapi, [google-music](https://github.com/thebigmunch/google-music).\n\n\n## Installation\n\n``pip install -U google-music-scripts``\n\n\n## Usage\n\nFor the release version, see the [stable docs](https://google-music-scripts.readthedocs.io/en/stable/).  \nFor the development version, see the [latest docs](https://google-music-scripts.readthedocs.io/en/latest/).\n\n\n## Appreciation\n\nShowing appreciation is always welcome.\n\n#### Thank\n\n[![Say Thanks](https://img.shields.io/badge/thank-thebigmunch-blue.svg?style=flat-square)](https://saythanks.io/to/thebigmunch)\n\nGet your own thanks inbox at [SayThanks.io](https://saythanks.io/).\n\n#### Contribute\n\n[Contribute](https://github.com/thebigmunch/google-music-scripts/blob/master/.github/CONTRIBUTING.md) by submitting bug reports, feature requests, or code.\n\n#### Help Others/Stay Informed\n\n[Discourse forum](https://forum.thebigmunch.me/)\n\n#### Referrals/Donations\n\n[![Digital Ocean](https://img.shields.io/badge/Digital_Ocean-referral-orange.svg?style=flat-square)](https://bit.ly/DigitalOcean-tbm-referral) [![Namecheap](https://img.shields.io/badge/Namecheap-referral-orange.svg?style=flat-square)](http://bit.ly/Namecheap-tbm-referral) [![PayPal](https://img.shields.io/badge/PayPal-donate-brightgreen.svg?style=flat-square)](https://bit.ly/PayPal-thebigmunch)\n',
    'author': 'thebigmunch',
    'author_email': 'mail@thebigmunch.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/thebigmunch/google-music-scripts',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
