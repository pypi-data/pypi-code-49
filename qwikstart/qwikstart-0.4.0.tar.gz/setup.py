# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qwikstart',
 'qwikstart.cli',
 'qwikstart.operations',
 'qwikstart.parser',
 'qwikstart.repository',
 'qwikstart.utils']

package_data = \
{'': ['*'], 'qwikstart.cli': ['templates/*']}

install_requires = \
['binaryornot>=0.4.4,<0.5.0',
 'click>=7.0,<8.0',
 'colorlog>=4.0.2,<5.0.0',
 'gitpython>=3.0.5,<4.0.0',
 'jinja2>=2.10,<3.0',
 'prompt-toolkit>=3.0.3,<4.0.0',
 'pyyaml>=5.1,<6.0',
 'rope>=0.14.0,<0.15.0',
 'termcolor>=1.1.0,<2.0.0',
 'typing-extensions>=3.7,<4.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses>=0.7,<0.8'],
 'docs': ['sphinx<2', 'sphinx-autobuild', 'sphinxcontrib-napoleon']}

entry_points = \
{'console_scripts': ['qwikstart = qwikstart.cli.main:main']}

setup_kwargs = {
    'name': 'qwikstart',
    'version': '0.4.0',
    'description': 'Code generator for automating configuration, setup, and yak shaving.',
    'long_description': 'qwikstart: Code injector for fun and profit\n===========================================\n\n.. default-role:: literal\n\n.. image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg\n   :target: https://github.com/tonysyu/qwikstart/blob/master/LICENSE\n\n.. image:: https://travis-ci.com/tonysyu/qwikstart.svg?branch=master\n   :target: https://travis-ci.com/tonysyu/qwikstart\n\n.. image:: https://codecov.io/gh/tonysyu/qwikstart/branch/master/graph/badge.svg\n   :target: https://codecov.io/gh/tonysyu/qwikstart\n\n.. image:: https://readthedocs.org/projects/qwikstart/badge/\n   :target: https://qwikstart.readthedocs.io\n\n\n- **Documentation:** https://qwikstart.readthedocs.io\n- **Source:** https://github.com/tonysyu/qwikstart\n\nInstall\n=======\n\nThe recommended way of installing `qwikstart` is to use pipx_::\n\n    pipx install qwikstart\n\nIf you happen to be setting up pipx_ for the first time, the\n`pipx installation instructions`_ suggest running `pipx ensurepath` to update\nthe user path. Note, if you use `~/.profile` instead of `~/.bash_profile`,\nthis will add `~/.bash_profile`, which will take precendence over `~/.profile`.\nEither move the code from `~/.bash_profile` to `~/.profile` or\n`link your profiles <https://superuser.com/a/789465>`_.\n\n.. _pipx: https://pypi.org/project/pipx/\n.. _pipx installation instructions:\n    https://pipxproject.github.io/pipx/installation/\n\nBasic Usage\n===========\n\nAfter installing `qwikstart`, you can run a simple hello-world example using the following::\n\n    qwikstart run --repo https://github.com/tonysyu/qwikstart examples/hello_world.yml\n\nBy default, there are abbreviations for common git repos, so the above can also be written::\n\n    qwikstart run --repo gh:tonysyu/qwikstart examples/hello_world.yml\n\n\nSee Also\n========\n\n- `hygen <https://www.hygen.io/>`_: The scalable code generator that saves you\n  time.\n- `cookiecutter <https://cookiecutter.readthedocs.io/>`_:\n  A command-line utility that creates projects from cookiecutters (project\n  templates)\n- `pyscaffold <https://pyscaffold.org/>`_: Python project template generator\n  with batteries included.\n',
    'author': 'Tony S. Yu',
    'author_email': 'tsyu80@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tonysyu/qwikstart',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
