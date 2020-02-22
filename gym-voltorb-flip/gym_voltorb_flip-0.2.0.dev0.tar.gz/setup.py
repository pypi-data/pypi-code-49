# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gym_voltorb_flip', 'gym_voltorb_flip.envs']

package_data = \
{'': ['*']}

install_requires = \
['gym>=0.16.0,<0.17.0', 'voltorb-flip>=0.2.0.dev0,<0.3.0']

setup_kwargs = {
    'name': 'gym-voltorb-flip',
    'version': '0.2.0.dev0',
    'description': 'A VoltorbFlip environment',
    'long_description': None,
    'author': 'Antonio Feregrino',
    'author_email': 'antonio.feregrino@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
