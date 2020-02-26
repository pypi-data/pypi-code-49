# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pickle_secure']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=2.3.0,<3.0.0']

setup_kwargs = {
    'name': 'pickle-secure',
    'version': '0.9.9',
    'description': 'Easily create encrypted pickle files',
    'long_description': '<p align="center">\n<a href="https://travis-ci.org/spapanik/pickle-secure"><img alt="Build" src="https://travis-ci.org/spapanik/pickle-secure.svg?branch=master"></a>\n<a href="https://coveralls.io/github/spapanik/pickle-secure"><img alt="Coverage" src="https://coveralls.io/repos/github/spapanik/pickle-secure/badge.svg?branch=master"></a>\n<a href="https://github.com/spapanik/pickle-secure/blob/master/LICENSE.txt"><img alt="License" src="https://img.shields.io/github/license/spapanik/pickle-secure"></a>\n<a href="https://pypi.org/project/pickle-secure"><img alt="PyPI" src="https://img.shields.io/pypi/v/pickle-secure"></a>\n<a href="https://pepy.tech/project/pickle-secure"><img alt="Downloads" src="https://pepy.tech/badge/pickle-secure"></a>\n<a href="https://github.com/psf/black"><img alt="Code style" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>\n</p>\n\n# pickle-secure\n\n_pickle-secure_ is a wrapper around pickle that creates encrypted pickles\n',
    'author': 'Stephanos Kuma',
    'author_email': 'spapanik21@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/spapanik/pickle-secure',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.0,<4.0.0',
}


setup(**setup_kwargs)
