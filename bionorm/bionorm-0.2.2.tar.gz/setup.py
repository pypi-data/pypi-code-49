# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bionorm']

package_data = \
{'': ['*'], 'bionorm': ['templates/*']}

install_requires = \
['biopython>=1.76,<2.0',
 'click>=7.0,<8.0',
 'click_plugins>=1.1.1,<2.0.0',
 'coverage>=5.0.3,<6.0.0',
 'importlib_metadata>=1.5.0,<2.0.0',
 'ruamel.yaml>=0.16.6,<0.17.0',
 'sequencetools>=0.0.5,<0.0.6']

entry_points = \
{'console_scripts': ['bionorm = bionorm:cli']}

setup_kwargs = {
    'name': 'bionorm',
    'version': '0.2.2',
    'description': 'normalize and verify genomic data',
    'long_description': "bionorm\n=======\n``bionorm`` normalizes and validates genomic data files prior to further processing\nor inclusion in a data store such as that of the\n`Legume Federation <https://www.legumefederation.org/en/data-store/>`_.\n\nPrerequisites\n-------------\nPython 3.6 or greater is required.\nThis package is tested under Linux and MacOS using Python 3.7.\n\nInstallation for Users\n----------------------\nInstall via pip or (better yet) `pipx <https://pipxproject.github.io/pipx/>`_: ::\n\n     pipx install bionorm\n\nFor Developers\n--------------\nIf you plan to develop ``bionorm``, you'll need to install\nthe `poetry <https://python-poetry.org>`_ dependency manager.\nIf you haven't previously installed ``poetry``, execute the command: ::\n\n    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python\n\nNext, get the master branch from GitHub ::\n\n\tgit clone https://github.com/ncgr/bionorm.git\n\nChange to the ``bionorm/`` directory and install with poetry: ::\n\n\tpoetry install -v\n\nRun ``bionorm`` with ``poetry``: ::\n\n    poetry run bionorm\n\nUsage\n-----\nInstallation puts a single script called ``bionorm`` in your path.  The usage format is::\n\n    bionorm [GLOBALOPTIONS] COMMAND [COMMANDOPTIONS][ARGS]\n\nGlobal Options\n--------------\nThe following options are global in scope and, if used, must be placed before\n``COMMAND``. Not all commands support every global option:\n\n============================= ====================================================\n    --verbose/-v              Log debugging info to stderr.\n    --quiet/-q                Suppress logging to stderr.\n    --no_log                  Suppress logging to file.\n    --progress                Show a progress bar.\n    --first_n                 Process only this many records. [default: all]\n    --warnings_as_errors/-e   Warnings cause exceptions.\n============================= ====================================================\n\nCommands\n--------\nA listing of commands is available via ``bionorm --help``.\nThe currently implemented commands are:\n\n============================= ====================================================\n  prefix_fasta                Prefix FASTA files for data store standard.\n  prefix_gff                  Prefix and sort GFF3 file for data store standard.\n  busco                       Perform BUSCO checks.\n  detector                    Detect/correct incongruencies among files.\n  fasta                       Check for GFF/FASTA consistency.\n  generate_readme             Generates a README file with details of genome.\n  index                       Indexes FASTA file.\n============================= ====================================================\n\nEach command has its ``COMMANDOPTIONS``, which may be listed with: ::\n\n    bionorm COMMAND --help\n\nProject Status\n--------------\n+-------------------+------------+------------+\n| Latest Release    | |pypi|     | |bionorm|  |\n+-------------------+------------+            +\n| GitHub            | |repo|     |            |\n+-------------------+------------+            +\n| License           | |license|  |            |\n+-------------------+------------+            +\n| Travis Build      | |travis|   |            |\n+-------------------+------------+            +\n| Coverage          | |coverage| |            |\n+-------------------+------------+            +\n| Code Grade        | |codacy|   |            |\n+-------------------+------------+            +\n| Dependencies      | |depend|   |            |\n+-------------------+------------+            +\n| Issues            | |issues|   |            |\n+-------------------+------------+------------+\n\n.. |bionorm| image:: docs/normal.jpg\n     :alt: Make me NORMAL, please!\n\n.. |pypi| image:: https://img.shields.io/pypi/v/bionorm.svg\n    :target: https://pypi.python.org/pypi/bionorm\n    :alt: Python package\n\n.. |repo| image:: https://img.shields.io/github/commits-since/ncgr/bionorm/0.1.0.svg\n    :target: https://github.com/ncgr/bionorm\n    :alt: GitHub repository\n\n.. |license| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg\n    :target: https://github.com/ncgr/bionorm/blob/master/LICENSE.txt\n    :alt: License terms\n\n.. |travis| image:: https://img.shields.io/travis/ncgr/bionorm.svg\n    :target:  https://travis-ci.org/ncgr/bionorm\n    :alt: Travis CI\n\n.. |codacy| image:: https://api.codacy.com/project/badge/Grade/b23fc0c167fc4660bb649320e14dac7f\n    :target: https://www.codacy.com/gh/ncgr/bionorm?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ncgr/bionorm&amp;utm_campaign=Badge_Grade\n    :alt: Codacy.io grade\n\n.. |coverage| image:: https://codecov.io/gh/ncgr/bionorm/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/ncgr/bionorm\n    :alt: Codecov.io test coverage\n\n.. |issues| image:: https://img.shields.io/github/issues/ncgr/bionorm.svg\n    :target:  https://github.com/ncgr/bionorm/issues\n    :alt: Issues reported\n\n.. |depend| image:: https://api.dependabot.com/badges/status?host=github&repo=ncgr/bionorm\n     :target: https://app.dependabot.com/accounts/ncgr/repos/236847525\n     :alt: dependabot dependencies\n",
    'author': 'Connor Cameron',
    'author_email': 'ctc@ncgr.org',
    'maintainer': 'Joel Berendzen',
    'maintainer_email': 'joelb@ncgr.org',
    'url': 'https://github.com/ncgr/ncgr',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
