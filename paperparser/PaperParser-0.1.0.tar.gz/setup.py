# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['paperparser']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.3,<6.0',
 'click>=7.0,<8.0',
 'desert>=2020.1.6,<2021.0.0',
 'marshmallow>=3.3.0,<4.0.0',
 'pybtex>=0.22.2,<0.23.0',
 'pyquery>=1.4.1,<2.0.0',
 'requests>=2.22.0,<3.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=1.5.0,<2.0.0']}

entry_points = \
{'console_scripts': ['paperparser = paperparser.console:main']}

setup_kwargs = {
    'name': 'paperparser',
    'version': '0.1.0',
    'description': 'A tool for parsing academic papers',
    'long_description': '# PaperParser\n\n## Installing Python and Poetry\n\nInstall pyenv:\n\n```bash\nbrew install pyenv\nbrew install pyenv-virtualenv\n```\n\nAdd the following lines to your `~/.bashrc` or `~/.zshrc`:\n\n```bash\nexport PATH="~/.pyenv/bin:$PATH"\neval "$(pyenv init -)"\neval "$(pyenv virtualenv-init -)"\n```\n\nInstall different python versions:\n\n```bash\npyenv install 3.8.1\npyenv install 3.7.6\npyenv local 3.8.1 3.7.6\npython3 --version\npython3.7 --version\n```\n\nInstall poetry:\n\n```bash\ncurl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python\n```\n\nAdd the following lines to your `~/.bashrc` or `~/.zshrc`:\n\n```bash\nsource ~/.poetry/env\n```\n\n## Installing and Opening in VSCode\n\n```bash\npoetry install\npoetry shell\ncode .\n```\n\nThe select the python interpreter with the project name in.\n\n## Updating Dependencies\n\n```bash\npoetry update\n```\n\n## Tests\n\n```\nnox -k "3.8"\n```\n\n## Credits\n\nHeavily inspired by [hypermodern-python](https://github.com/cjolowicz/hypermodern-python) by [cjolowicz](https://github.com/cjolowicz)\n',
    'author': 'Phil Winder',
    'author_email': 'phil@WinderResearch.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/winderresearch/tools/PaperParser',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
