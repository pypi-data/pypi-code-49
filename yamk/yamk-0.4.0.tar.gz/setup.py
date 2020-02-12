# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['yamk']

package_data = \
{'': ['*']}

install_requires = \
['toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['yam = yamk.main:main', 'yamk = yamk.main:main']}

setup_kwargs = {
    'name': 'yamk',
    'version': '0.4.0',
    'description': 'Yet another make',
    'long_description': '<p align="center">\n<a href="https://travis-ci.org/spapanik/yamk"><img alt="Build" src="https://travis-ci.org/spapanik/yamk.svg?branch=master"></a>\n<a href="https://coveralls.io/github/spapanik/yamk"><img alt="Coverage" src="https://coveralls.io/repos/github/spapanik/yamk/badge.svg?branch=master"></a>\n<a href="https://github.com/spapanik/yamk/blob/master/LICENSE.txt"><img alt="License" src="https://img.shields.io/github/license/spapanik/yamk"></a>\n<a href="https://pypi.org/project/yamk"><img alt="PyPI" src="https://img.shields.io/pypi/v/yamk"></a>\n<a href="https://pepy.tech/project/yamk"><img alt="Downloads" src="https://pepy.tech/badge/yamk"></a>\n<a href="https://github.com/psf/black"><img alt="Code style" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>\n</p>\n\n\n# yamk\n\n_yamk_ is yet another make.\n',
    'author': 'Stephanos Kuma',
    'author_email': 'spapanik21@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/spapanik/yamk',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.0,<4.0.0',
}


setup(**setup_kwargs)
