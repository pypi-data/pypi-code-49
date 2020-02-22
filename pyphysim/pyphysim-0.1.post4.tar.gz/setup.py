# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyphysim',
 'pyphysim.c_extensions',
 'pyphysim.cell',
 'pyphysim.channel_estimation',
 'pyphysim.channels',
 'pyphysim.comm',
 'pyphysim.extra',
 'pyphysim.extra.MATLAB',
 'pyphysim.ia',
 'pyphysim.mimo',
 'pyphysim.modulators',
 'pyphysim.reference_signals',
 'pyphysim.simulations',
 'pyphysim.subspace',
 'pyphysim.util']

package_data = \
{'': ['*']}

install_requires = \
['configobj', 'h5py', 'matplotlib', 'numpy', 'scipy']

setup_kwargs = {
    'name': 'pyphysim',
    'version': '0.1.post4',
    'description': 'Implementation of a digital communication (physical layer) in python',
    'long_description': '![Testing](https://travis-ci.org/darcamo/pyphysim.svg?branch=master)\n[![Coverage Status](https://coveralls.io/repos/github/darcamo/pyphysim/badge.svg?branch=master)](https://coveralls.io/github/darcamo/pyphysim?branch=master)\n[![Documentation Status](https://readthedocs.org/projects/pyphysim/badge/?version=latest)](http://pyphysim.readthedocs.io/en/latest/?badge=latest)\n\nPyPhysim\n========\n\nSimulation of Digital Communication (physical layer) in Python.\n\nThis includes classes related to digital modulation, AWGN channels, MIMO,\nOFDM, etc.. It also includes classes related to multiuser transmission such\nas block diagonalization, interference alignment, etc.\n\nFurthermore, a framework for implementing Monte Carlo simulations is also\nimplemented (see the pyphysim.simulations package).\n\n\nNote\n----\n\nIt is possible to run the files in the "apps" and "tests" folders without\ninstalling PyPhysim. In that case, you should probably at least run the\nsetup script to compile any C extension with\n\n`python setup.py build_ext`\n',
    'author': 'Darlan Cavalcante Moreira',
    'author_email': 'darcamo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/darcamo/pyphysim',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
