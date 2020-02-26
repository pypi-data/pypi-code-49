# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['notty', 'notty.lib', 'notty.screens', 'notty.utils']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.3,<2.0.0',
 'click>=7.0,<8.0',
 'colorama>=0.4.3,<0.5.0',
 'prompt_toolkit>=3.0.3,<4.0.0']

entry_points = \
{'console_scripts': ['notty = notty.app:main']}

setup_kwargs = {
    'name': 'notty',
    'version': '1.3.7',
    'description': '📝⚡ Fast terminal-based notes application',
    'long_description': '<p align="center"><img width=512 src="https://raw.githubusercontent.com/jarvis394/notty/master/notty.png" alt="terminal view" /></p>\n<h1 align="center">notty</h1>\n<h6 align="center">📝⚡ Fast terminal-based notes application</h6>\n\n## Setup\n\nInstallation via `pip`:\n\n```bash\n$ pip install notty\n```\n\nUpdating:\n\n```bash\n$ pip install notty --upgrade\n```\n\nExecuting:\n```bash\n$ notty\nUsage: notty [OPTIONS] COMMAND [ARGS]...\n```\n\n**If you\'re using Anaconda:**\n1. Create new virtual environment\n    ```bash\n    (base) $ conda create -n YOURNAME python=3\n    Collecting package metadata (current_repodata.json): done\n    Solving environment: done\n    ... # hit [y] for the packages\' installation\n    ```\n2. Activate newly created environment\n    ```bash\n    (base) $ conda activate YOURNAME\n    (YOURNAME) $\n    ```\n3. Install via `pip`:\n    ```bash\n    (YOURNAME) $ pip install notty --upgrade\n    ```\n4. To return to the `(base)` environment, run `conda deactivate`:\n    ```bash\n    (YOURNAME) $ conda deactivate\n    (base) $ \n    ```\n\n*Currently built for **Python 3.x***\n\n## Usage\n\nFor more information, run `notty --help`\n\n|Command|Aliases|Description|\n|-|-|-|\n|create|*c, create*|Creates a new note|\n|list|*l, list*|Lists all notes.<br />Actually, it can create, delete, rename the notes, so it might be the most important thing here|\n|edit `<id>`|*e, edit*|Edits the note with a given ID (opens up a default editor)|\n\n## Contribution\n\n...is welcomed. PR\'s are widely opened.\n\n## Contact\n\nMe: [VK](https://vk.com/tarnatovski)\n',
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
