# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tasmidi']

package_data = \
{'': ['*']}

install_requires = \
['mido>=1.2.9,<2.0.0']

entry_points = \
{'console_scripts': ['tasmidi-convert = tasmidi.convert:main',
                     'tasmidi-map = tasmidi.map:main']}

setup_kwargs = {
    'name': 'tasmidi',
    'version': '0.1.1',
    'description': '',
    'long_description': '# tasmidi\n\n## What is this?\n\n`tasmidi` is a collection of tools used to convert a LibTAS input file into a MIDI file. There are two steps to this: producing a mapping file to tell the program what notes correspond to what input, and using that mapping file to create the MIDI.\n\n## Installation\n\n```bash\npip install tasmidi\n```\n\n## How do I get the input file?\n\nAssuming that your LibTAS movie file is called `tas-movie.ltm`:\n\n```bash\ntar xvzf tas-movie.ltm\n```\n\nThis will produce several files, but the only one that we are interested in is called `inputs`.\n\n## Usage\n\nBoth commands in this package have their own `--help` flag for specific usage. A typical workflow looks like:\n\n```bash\ntasmidi-map inputs > mapping.json # Generate a mapping file for the inputs\ntasmidi-convert inputs -m mapping.json # Use that mapping and the input file to create a MIDI\n```\n',
    'author': 'Mark Rawls',
    'author_email': 'markrawls96@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/markrawls/tasmidi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
