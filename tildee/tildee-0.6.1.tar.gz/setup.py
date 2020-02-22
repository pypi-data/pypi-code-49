# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tildee']

package_data = \
{'': ['*']}

install_requires = \
['cssselect>=1.0,<2.0', 'lxml>=4.3,<5.0', 'requests>=2.22,<3.0']

setup_kwargs = {
    'name': 'tildee',
    'version': '0.6.1',
    'description': 'A client for tildes.net',
    'long_description': 'This is tildee.py, a Python 3 library for interacting with the <https://tildes.net> API. Note that this API is not stable and not actually intended for external use, so this could break at any moment. Main repository and issue tracker is on [Dingenskirchen Systems Git](https://git.15318.de/dingens/tildee.py) (Login using GitLab or -Hub available), there are mirrors provided on [GitLab](https://gitlab.com/deing/tildee) and [GitHub](https://github.com/deingithub/tildee) for discoverability.\n\n[PyPI](https://pypi.org/project/tildee/) — [Source](https://git.15318.de/dingens/tildee.py) — [Docs](https://tildee.readthedocs.io/en/latest/index.html)\n',
    'author': 'deing',
    'author_email': 'admin@15318.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://tildee.readthedocs.io/en/latest/index.html',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
