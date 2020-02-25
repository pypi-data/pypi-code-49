# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['notty', 'notty.lib', 'notty.screens', 'notty.utils']

package_data = \
{'': ['*']}

install_requires = \
['appdirs', 'click', 'colorama', 'prompt_toolkit']

entry_points = \
{'console_scripts': ['notty = notty.app:main']}

setup_kwargs = {
    'name': 'notty',
    'version': '1.3.4',
    'description': '📝⚡ Fast terminal-based notes application',
    'long_description': '<p align="center"><img width=512 src="https://raw.githubusercontent.com/jarvis394/notty/master/notty.png" alt="terminal view" /></p>\n<h1 align="center">notty</h1>\n<h6 align="center">📝⚡ Fast terminal-based notes application</h6>\n\n## Installation\n\nVia `pip`:\n\n```bash\n$ pip install notty\n```\n\nCurrently built on Python 3.7\n\n## Usage\n\n|Command|Aliases|Description|\n|-|-|-|\n|create|*c, create*|Creates a new note|\n|list|*l, list*|Lists all notes.<br />Actually, it can create, delete, rename the notes, so it might be the most important thing here|\n|edit `<id>`|*e, edit*|Edits the note with a given ID (opens up a default editor)|\n\n## Contribution\n\n...is welcomed. PR\'s are widely opened.\n\n## Contact\n\nMe: [VK](https://vk.com/tarnatovski)\n',
    'author': 'jarvis394',
    'author_email': 'tarnatovski@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jarvis394/notty',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
