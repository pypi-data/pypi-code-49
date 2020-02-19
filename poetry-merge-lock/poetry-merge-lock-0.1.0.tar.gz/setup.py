# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['poetry_merge_lock']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'poetry>=1.0.3,<2.0.0', 'tomlkit>=0.5.8,<0.6.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.1.3,<1.2.0']}

entry_points = \
{'console_scripts': ['poetry-merge-lock = poetry_merge_lock.console:main']}

setup_kwargs = {
    'name': 'poetry-merge-lock',
    'version': '0.1.0',
    'description': 'poetry-merge-lock',
    'long_description': '[![Tests](https://github.com/cjolowicz/poetry-merge-lock/workflows/Tests/badge.svg)](https://github.com/cjolowicz/poetry-merge-lock/actions?workflow=Tests)\n[![Codecov](https://codecov.io/gh/cjolowicz/poetry-merge-lock/branch/master/graph/badge.svg)](https://codecov.io/gh/cjolowicz/poetry-merge-lock)\n[![PyPI](https://img.shields.io/pypi/v/poetry-merge-lock.svg)](https://pypi.org/project/poetry-merge-lock/)\n[![Read the Docs](https://readthedocs.org/projects/poetry-merge-lock/badge/)](https://poetry-merge-lock.readthedocs.io/)\n\n# poetry-merge-lock\n',
    'author': 'Claudio Jolowicz',
    'author_email': 'mail@claudiojolowicz.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/cjolowicz/poetry-merge-lock',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
