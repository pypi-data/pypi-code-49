# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['paperparser']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
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
    'version': '0.2.1',
    'description': 'A tool for parsing academic papers',
    'long_description': '# PaperParser\n\nParses academic paper information from URLs.\n\nThis is a project by [Winder Research](https://WinderResearch.com), a Cloud-Native Data Science consultancy.\n\n## Installation\n\n```python\npip install paperparser\n```\n\n## Usage\n\n### CLI\n\n```bash\n$ paperparser --help                                \nUsage: paperparser [OPTIONS] URL STRATEGY\n\n  Parse the bibtex from a URL using the STRATEGY.\n\nOptions:\n  --version  Show the version and exit.\n  --help     Show this message and exit.\n\n$ paperparser https://arxiv.org/abs/1812.02900 arxiv\n{\'title\': \'Off-Policy Deep Reinforcement Learning without Exploration\', \'journal\': \'CoRR\', \'volume\': \'abs/1812.02900\', \'year\': \'2018\', \'url\': \n\'http://arxiv.org/abs/1812.02900\', \'archivePrefix\': \'arXiv\', \'eprint\': \'1812.02900\', \'timestamp\': \'Tue, 01 Jan 2019 15:01:25 +0100\', \'biburl\': \'https://dblp.org/rec/journals/corr/abs-1812-02900.bib\', \'bibsource\': \'dblp computer science bibliography, https://dblp.org\'}\n```\n### Python\n\n```python\nfrom paperparser import page\n\np = page.BibTeXPage(url=url, strategy=strategy)\nprint(p.as_dict())\nprint(p.abstract())\n```\n\n## Strategies\n\n### `"arxiv"`\n\nParses bibtex from [dblp](https://dblp.uni-trier.de) and abstracts directly.\n\n### `"nips"`\n\nParses bibtex and abstracts directly.\n\n### `"acm"`\n\nParses bibtex via the doi from [scipython](https://scipython.com) and abstracts directly.',
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
