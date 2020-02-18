# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['past_mtl_monitors']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=19.3.0,<20.0.0', 'intervaltree>=3.0.2,<4.0.0']

setup_kwargs = {
    'name': 'past-mtl-monitors',
    'version': '0.1.0',
    'description': 'A library for creating past metric temporal logic monitors.',
    'long_description': "Past MTL Monitors\n=================\nA library for creating past metric temporal logic monitors.\n\n[![Build Status](https://cloud.drone.io/api/badges/mvcisback/past-mtl-monitors/status.svg)](https://cloud.drone.io/mvcisback/past-mtl-monitors)\n[![Documentation Status](https://readthedocs.org/projects/past-mtl-monitors/badge/?version=latest)](https://past-mtl-monitors.readthedocs.io/en/latest/?badge=latest)\n[![codecov](https://codecov.io/gh/mvcisback/past-mtl-monitors/branch/master/graph/badge.svg)](https://codecov.io/gh/mvcisback/past-mtl-monitors)\n[![PyPI version](https://badge.fury.io/py/past-mtl-monitors.svg)](https://badge.fury.io/py/past-mtl-monitors)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n\n\n<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-generate-toc again -->\n**Table of Contents**\n\n- [Past MTL Monitors](#past-mtl-monitors)\n- [Installation](#installation)\n- [Usage](#usage)\n\n<!-- markdown-toc end -->\n\n\n# Installation\n\nIf you just need to use `past-mtl-monitors`, you can just run:\n\n`$ pip install past-mtl-monitors`\n\nFor developers, note that this project uses the\n[poetry](https://poetry.eustace.io/) python package/dependency\nmanagement tool. Please familarize yourself with it and then\nrun:\n\n`$ poetry install`\n\n# Usage\n\nThe primary entry point to the `past-mtl-monitors` package is the\n`atom` function. This exposes a monitor factory which can be combined\nwith other monitor factories to create complex property monitors.\n\nUnder the hood, these monitor factories are just wrappers around\npython coroutines that expect a `(time, val)` pair, where time is a\n`float` and `val` is a mapping from strings to robustness values\n(`float`).\n\n**Note** `past-mtl-monitors` only implements a quantitative semantics\nwhere a value greater than 0 implies sat and a value less than 0\nimplies unsat.\n\nThus if one would like to use Boolean semantics, use `1` for `True` and\n`-1` for `False`.\n\n```python\nfrom past_mtl_monitors import atom\n\nx, y, z = atom('x'), atom('y'), atom('z')\n\n# Monitor that historically, x has been equal to y.\nmonitor = (x == y).hist().monitor()\n\n#                    time         values\nassert monitor.send((0    , {'x': 1, 'y': 1}))  ==  1   # sat\nassert monitor.send((1.1  , {'x': 1, 'y': -1})) == -1   # unsat\nassert monitor.send((1.5  , {'x': 1, 'y': 1}))  == -1   # unsat\n\nmonitor2 = x.once().monitor()  # Monitor's x's maximum value.\nassert monitor2.send((0 , {'x': -10, 'y': 1})) == -10\nassert monitor2.send((0 , {'x': 100, 'y': 2})) == 100\nassert monitor2.send((0 , {'x': -100, 'y': -1})) == 100\n\n# Monitor that x & y have been true since the last\n# time that z held for 3 time units.\nmonitor3 = (x & y).since(z.hist(0, 3)).monitor()\n```\n",
    'author': 'Marcell Vazquez-Chanlatte',
    'author_email': 'mvc@linux.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mvcisback/past-mtl-monitors',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
