# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ratus']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ratus',
    'version': '0.0.3',
    'description': 'Simple expression language.',
    'long_description': '# Ratus\n\n[![Documentation Status](https://readthedocs.org/projects/ratus/badge/?version=latest)](https://ratus.readthedocs.io/en/latest/?badge=latest)\n[![CircleCI](https://circleci.com/gh/nick96/ratus.svg?style=svg)](https://circleci.com/gh/nick96/ratus)\n[![PyPI](https://img.shields.io/pypi/v/ratus)](https://pypi.org/project/ratus/)\n\nRatus is a simple expression language that can be used to easily extend Python\napplications with an embedded expression language. Evaluating basic expressions\nis as simple as:\n\n``` python\nfrom ratus import Evaluator\n\nevaluator = Evaluator()\nevaluator.evaluate("1 + 1") # => 1\nevaluator.evaluate("1 > 1") # => False\nevaluator.evaluate("if(1 < 2, 10, 5)") #  => 5\n```\n\nFor more information, please check out the\n[docs](https://ratus.readthedocs.io/en/latest/)\n\n## What\'s in a name?\n\nWhen I first started this project I did a bit of research around parsing\ntechniques as this is really the most complex part. One idea that that really\nstuck out to me was [packrat](https://bford.info/packrat/) parsing. This\ntechnique allows for linear time parsing, as opposed to the usual exponential\ntime of backtracking parsing.\n\nCurrently packrat parsing isn\'t implemented for `ratus` but I\'m working on it!\n\n## Roadmap\n\n### `v1.0.0`\n\n- [ ] Fully document all features\n  - [ ] API\n  - [ ] Grammar\n- [ ] Fix known bugs\n  - [ ] Don\'t require functions to be the root of an expression\n    - e.g. ``pow(2, 2) + 1`` should be allowed\n',
    'author': 'Nick Spain',
    'author_email': 'nicholas.spain96@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nick96/ratus',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
