# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gcgc',
 'gcgc.data',
 'gcgc.tests',
 'gcgc.tests.fixtures',
 'gcgc.tests.tokenizer',
 'gcgc.tokenizer']

package_data = \
{'': ['*'],
 'gcgc.data': ['splice/*'],
 'gcgc.tests.fixtures': ['PF12057/*',
                         'ecoli/*',
                         'globin_alignment/*',
                         'p53_human/*']}

install_requires = \
['click>=7.0,<8.0', 'pydantic>=1.1,<2.0', 'typing-extensions>=3.7,<4.0']

extras_require = \
{'sentencepiece': ['sentencepiece>=0.1,<0.2', 'biopython>=1.76,<2.0']}

entry_points = \
{'console_scripts': ['gcgc = gcgc.cli:cli']}

setup_kwargs = {
    'name': 'gcgc',
    'version': '0.12.1.dev3',
    'description': 'GCGC is a preprocessing library for biological sequence model development.',
    'long_description': '# GCGC\n\n> GCGC is a tool for feature processing on Biological Sequences.\n\n[![](https://github.com/tshauck/gcgc/workflows/Run%20Tests%20and%20Lint/badge.svg)](https://github.com/tshauck/gcgc/actions?query=workflow%3A%22Run+Tests+and+Lint%22)\n[![](https://img.shields.io/pypi/v/gcgc.svg)](https://pypi.python.org/pypi/gcgc)\n[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2329966.svg)](https://doi.org/10.5281/zenodo.2329966)\n[![code style black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n## Installation\n\nGCGC is primarily intended to be used as part of a larger workflow inside\nPython, but it can also be used as a docker container.\n\nTo install via pip:\n\n```sh\n$ pip install gcgc\n```\n\nAnd to pull the docker image:\n\n```sh\n$ docker pull docker.io/thauck/gcgc\n```\n\n## Documentation\n\nThe GCGC documentation is at [gcgc.trenthauck.com](http://gcgc.trenthauck.com),\nplease see it for an example.\n\n## Citing GCGC\n\nIf you use GCGC in your research, cite it with the following:\n\n```\n@misc{trent_hauck_2018_2329966,\n  author       = {Trent Hauck},\n  title        = {GCGC},\n  month        = dec,\n  year         = 2018,\n  doi          = {10.5281/zenodo.2329966},\n  url          = {https://doi.org/10.5281/zenodo.2329966}\n}\n```\n',
    'author': 'Trent Hauck',
    'author_email': 'trent@trenthauck.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://gcgc.trenthauck.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
