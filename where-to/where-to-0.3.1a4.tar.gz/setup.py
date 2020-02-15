# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['where_to']

package_data = \
{'': ['*']}

install_requires = \
['PILLOW>=7.0.0,<8.0.0', 'pywin32>=227,<228']

entry_points = \
{'console_scripts': ['where-to-console = where_to.cli:main'],
 'gui_scripts': ['where-to = where_to.cli:main']}

setup_kwargs = {
    'name': 'where-to',
    'version': '0.3.1a4',
    'description': 'Show upcoming Outlook meetings on the Windows lock screen',
    'long_description': '![where-to logo](https://github.com/blairconrad/where-to/raw/master/assets/where-to-128.png "where-to logo")\n\nwhere-to is a [Python](https://www.python.org/) command-line utility that\ndisplays upcoming Outlook appointments on a Windows lock screen.\n\nThe package is [available on pypi](https://pypi.org/project/where-to/) and can\nbe installed from the command line by typing\n\n```\npip install where-to\n```\n\nOnce installed, a `where-to` command will be added to your Python scripts\ndirectory. You can run it to show the next appointment, all appointments for the\nrest of the day only appointments due to start at this time.\n\nExamples:\n\n```shell\nwhere-to upcoming # shows all appointments for the rest of the day\nwhere-to next\nwhere-to now      # appointments starting between 10 minutes ago and 15  minutes hence\n```\n\nGet more help via `where-to --help`.\n\nNote that `where-to` is built to be console-less, so that when invoked from a Windows scheduled\ntask it will not pop up an annoying console window. The help message (and indeed all output)\nshould be presented in an instance of the notepad editor. If this isn\'t working, or if for some\nreason you want to see a display in a terminal window, the alternative executable `where-to-console`\nis also available. This can be combined with the `--display-mode list` option to print appointments\nrather than splash them on the lock screen.\n\n\n----\nLogo: [Calendar](https://thenounproject.com/paisley.299/uploads/?i=1968675) by\n[Paisley](https://thenounproject.com/paisley.299/) from\n[the Noun Project](https://thenounproject.com/).\n',
    'author': 'Blair Conrad',
    'author_email': 'blair@blairconrad.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/blairconrad/where-to.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
