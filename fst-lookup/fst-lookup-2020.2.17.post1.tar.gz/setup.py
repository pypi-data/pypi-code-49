# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fst_lookup']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'fst-lookup',
    'version': '2020.2.17.post1',
    'description': 'Lookup Foma FSTs',
    'long_description': 'FST Lookup\n==========\n\n[![Build Status](https://travis-ci.org/eddieantonio/fst-lookup.svg?branch=master)](https://travis-ci.org/eddieantonio/fst-lookup)\n[![codecov](https://codecov.io/gh/eddieantonio/fst-lookup/branch/master/graph/badge.svg)](https://codecov.io/gh/eddieantonio/fst-lookup)\n[![PyPI version](https://img.shields.io/pypi/v/fst-lookup.svg)](https://pypi.org/project/fst-lookup/)\n[![calver YYYY.MM.DD](https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg)](http://calver.org/)\n\nImplements lookup for [Foma][] finite state transducers.\n\nSupports Python 3.5 and up.\n\n[Foma]: https://fomafst.github.io/\n\n\nInstall\n-------\n\n    pip install fst-lookup\n\nUsage\n-----\n\nImport the library, and load an FST from a file:\n\n> Hint: Test this module by [downloading the `eat` FST](https://github.com/eddieantonio/fst-lookup/raw/master/tests/data/eat.fomabin)!\n\n```python\n>>> from fst_lookup import FST\n>>> fst = FST.from_file(\'eat.fomabin\')\n```\n\n### Assumed format of the FSTs\n\n`fst_lookup` assumes that the **lower** label corresponds to the surface\nform, while the **upper** label corresponds to the lemma, and linguistic\ntags and features: e.g., your `LEXC` will look something like\nthis—note what is on each side of the colon (`:`):\n\n```lexc\nMultichar_Symbols +N +Sg +Pl\nLexicon Root\n    cow+N+Sg:cow #;\n    cow+N+Pl:cows #;\n    goose+N+Sg:goose #;\n    goose+N+Pl:geese #;\n    sheep+N+Sg:sheep #;\n    sheep+N+Pl:sheep #;\n```\n\nIf your FST has labels on the opposite sides—e.g., the **upper** label\ncorresponds to the surface form and the **upper** label corresponds to\nthe lemma and linguistic tags—then instantiate the FST by providing\nthe `labels="invert"` keyword argument:\n\n```python\nfst = FST.from_file(\'eat-inverted.fomabin\', labels="invert")\n```\n\n> **Hint**: FSTs originating from the HFST suite are often inverted, so\n> try to loading the FST inverted first if `.generate()` or `.analyze()`\n> aren\'t working correctly!\n\n\n### Analyze a word form\n\nTo _analyze_ a form (take a word form, and get its linguistic analyzes)\ncall the `analyze()` function:\n\n```python\ndef analyze(self, surface_form: str) -> Iterator[Analysis]\n```\n\nThis will yield all possible linguistic analyses produced by the FST.\n\nAn analysis is a tuple of strings. The strings are either linguistic\ntags, or the _lemma_ (base form of the word).\n\n`FST.analyze()` is a generator, so you must call `list()` to get a list.\n\n```python\n>>> list(sorted(fst.analyze(\'eats\')))\n[(\'eat\', \'+N\', \'+Mass\'),\n (\'eat\', \'+V\', \'+3P\', \'+Sg\')]\n```\n\n\n### Generate a word form\n\nTo _generate_ a form (take a linguistic analysis, and get its concrete\nword forms), call the `generate()` function:\n\n```python\ndef generate(self, analysis: str) -> Iterator[str]\n```\n\n`FST.generate()` is a Python generator, so you must call `list()` to get\na list.\n\n```python\n>>> list(fst.generate(\'eat+V+Past\')))\n[\'ate\']\n```\n\n\nContributing\n------------\n\nIf you plan to contribute code, it is recommended you use [Pipenv].\nFork and clone this repository, then install development dependencies\nby typing:\n\n    pipenv install\n\nThen, do all your development within a virtual environment, managed by\nPipenv:\n\n    pipenv shell\n\n### Type-checking\n\nThis project uses `mypy` to check static types. To invoke it on this\npackage, type the following:\n\n    mypy -p fst_lookup\n\n### Running tests\n\nTo run this project\'s tests, we use `py.test`:\n\n    py.test\n\n\n### Fixtures\n\nIf you are creating or modifying existing test fixtures (i.e., mostly\npre-built FSTs used for testing), you will need the following\ndependencies:\n\n * GNU `make`\n * [Foma][]\n\nFixtures are stored in `tests/data/`. Here, you will use `make` to\ncompile all pre-built FSTs from source:\n\n    make\n\n[Pipenv]: https://github.com/pypa/pipenv\n\n\nLicense\n-------\n\nCopyright © 2019 Eddie Antonio Santos. Released under the terms of the\nApache license. See `LICENSE` for more info.\n',
    'author': 'Eddie Antonio Santos',
    'author_email': 'easantos@ualberta.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/eddieantonio/fst-lookup',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
