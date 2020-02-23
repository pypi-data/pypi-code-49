# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['proggy', 'proggy.tty']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'proggy',
    'version': '0.3.0',
    'description': 'A progress bar generator.',
    'long_description': "Proggy\n======\n\nProgressively progressing through progress bar generation.\n\nProggy generates text-based progress bars. Mildly inspired by Rust's\n[indicatif](https://github.com/mitsuhiko/indicatif).\n\nProggy only renders progress bars to a string. Displaying them is, as of now,\nnot handled and left to the user.\n\nExamples\n--------\n\n### API usage\n\n```\n>>> from proggy import ProgressBar\n>>> pb = ProgressBar(30, 100, progress=75)\n>>> pb.render()\n'⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       '\n```\n\n### CLI output\n\n`test.py`:\n```python\nimport time\n\nfrom proggy.tty import TTYProgressBar\n\n\nwith TTYProgressBar(size=30, total=100) as p:\n    for i in range(100):\n        time.sleep(0.1)\n        p.progress += 1\n        p.draw()\n```\n\nOutput:\n\n![test.py output](gif/test.gif)\n",
    'author': 'Tarcísio Eduardo Moreira Crocomo',
    'author_email': 'tarcisioe@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
