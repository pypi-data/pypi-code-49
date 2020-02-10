# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['udify',
 'udify.dataset_readers',
 'udify.models',
 'udify.modules',
 'udify.optimizers',
 'udify.predictors']

package_data = \
{'': ['*']}

install_requires = \
['transformers>=2.3.0,<3.0.0', 'unofficial-allennlp-nightly']

setup_kwargs = {
    'name': 'unofficial-udify',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Dan Kondratyuk',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
