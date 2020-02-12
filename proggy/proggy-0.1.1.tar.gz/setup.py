# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['proggy']
setup_kwargs = {
    'name': 'proggy',
    'version': '0.1.1',
    'description': 'A progress bar generator.',
    'long_description': "Proggy\n======\n\nProgressively progressing through progress bar generation.\n\nProggy generates text-based progress bars. Mildly inspired by Rust's\n[indicatif](https://github.com/mitsuhiko/indicatif).\n\nProggy only renders progress bars to a string. Displaying them is, as of now,\nnot handled and left to the user.\n\nExample\n-------\n\n```\n>>> from proggy import ProgressBar\n>>> pb = ProgressBar(30, 100, progress=75)\n>>> pb.render()\n'⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       '\n```\n",
    'author': 'Tarcísio Eduardo Moreira Crocomo',
    'author_email': 'tarcisioe@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
