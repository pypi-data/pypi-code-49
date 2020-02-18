# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mimosa']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=19.3.0,<20.0.0',
 'cerberus>=1.3.2,<2.0.0',
 'cutie>=0.2.2,<0.3.0',
 'firebase-admin>=3.2.1,<4.0.0',
 'halo>=0.0.28,<0.0.29',
 'typer[all]>=0.0.8,<0.0.9']

entry_points = \
{'console_scripts': ['mimosa = mimosa.main:main']}

setup_kwargs = {
    'name': 'mimosa-monomer',
    'version': '0.0.10',
    'description': 'CLI for Stilt 2 database.',
    'long_description': '# mimosa \nDatabase management CLI for **Stilt 2**.\n\n## Installation\nRun `pip install mimosa_monomer-0.0.1-py3-none-any.whl` to install the package\ninto your chosen python environment.\n\nBe sure to update to the current wheel filename.\n\n## Usage\nRun `mimosa` in the terminal. Select the service account key file for the\ndesired Firebase project to connect to. Follow the prompts.\n',
    'author': 'Daniel Hampton',
    'author_email': 'dhampton084@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
