# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['berny']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.15,<2.0']

extras_require = \
{'cov': ['coverage>=4.5,<5.0'],
 'doc': ['sphinx>=1.7,<2.0', 'toml>=0.10.0,<0.11.0'],
 'test': ['pytest>=3.6,<4.0']}

entry_points = \
{'console_scripts': ['berny = berny.cli:main']}

setup_kwargs = {
    'name': 'pyberny',
    'version': '0.5.0',
    'description': 'Molecular/crystal structure optimizer',
    'long_description': "# Berny\n\n[![build](https://img.shields.io/travis/jhrmnn/pyberny/master.svg)](https://travis-ci.org/jhrmnn/pyberny)\n[![coverage](https://img.shields.io/codecov/c/github/jhrmnn/pyberny.svg)](https://codecov.io/gh/jhrmnn/pyberny)\n![python](https://img.shields.io/pypi/pyversions/pyberny.svg)\n[![pypi](https://img.shields.io/pypi/v/pyberny.svg)](https://pypi.org/project/pyberny/)\n[![commits since](https://img.shields.io/github/commits-since/jhrmnn/pyberny/latest.svg)](https://github.com/jhrmnn/pyberny/releases)\n[![last commit](https://img.shields.io/github/last-commit/jhrmnn/pyberny.svg)](https://github.com/jhrmnn/pyberny/commits/master)\n[![license](https://img.shields.io/github/license/jhrmnn/pyberny.svg)](https://github.com/jhrmnn/pyberny/blob/master/LICENSE)\n\nBerny is an optimizer of molecular geometries with respect to the total energy, using nuclear gradient information.\n\nIn each step, it takes energy and Cartesian gradients as an input, and returns a new equilibrium structure estimate.\n\nThe package implements a single optimization algorithm, which is an amalgam of several techniques, comprising the quasi-Newton method, redundant internal coordinates, an iterative Hessian approximation, a trust region scheme, and linear search. The algorithm is described in more detailed in the [documentation](https://jhrmnn.github.io/pyberny/algorithm.html).\n\nSeveral desirable features are missing at the moment but planned, some of them being actively worked on (help is always welcome): [crystal geometries](https://github.com/jhrmnn/pyberny/issues/5),\xa0[coordinate constraints](https://github.com/jhrmnn/pyberny/issues/14), [coordinate weighting](https://github.com/jhrmnn/pyberny/issues/32), [transition state search](https://github.com/jhrmnn/pyberny/issues/4).\n\n## Installing\n\nInstall and update using [Pip](https://pip.pypa.io/en/stable/quickstart/):\n\n```\npip install -U pyberny\n```\n\n## Example\n\n```python\nfrom berny import Berny, geomlib\n\noptimizer = Berny(geomlib.readfile('geom.xyz'))\nfor geom in optimizer:\n    # get energy and gradients for geom\n    optimizer.send((energy, gradients))\n```\n\n## Links\n\n- Documentation: <https://jhrmnn.github.io/pyberny>\n",
    'author': 'Jan Hermann',
    'author_email': 'dev@jan.hermann.name',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jhrmnn/pyberny',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
}


setup(**setup_kwargs)
