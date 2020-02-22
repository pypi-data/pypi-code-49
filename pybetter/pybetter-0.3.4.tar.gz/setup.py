# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pybetter', 'pybetter.transformers']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0',
 'libcst>=0.3.1,<0.4.0',
 'pyemojify>=0.2.0,<0.3.0',
 'pygments>=2.5.2,<3.0.0']

entry_points = \
{'console_scripts': ['pybetter = pybetter.cli:main']}

setup_kwargs = {
    'name': 'pybetter',
    'version': '0.3.4',
    'description': 'Tool for fixing trivial problems with your code.',
    'long_description': '# pybetter\n![PyPI](https://img.shields.io/pypi/v/pybetter) \n![Travis CI](https://img.shields.io/travis/com/lensvol/pybetter)\n![Code coverage](https://img.shields.io/codecov/c/github/lensvol/pybetter)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pybetter)\n![License](https://img.shields.io/github/license/lensvol/pybetter)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nTool for fixing trivial problems with your code.\n\nOriginally intended as an example for my PyCon Belarus 2020 talk about [LibCST](https://github.com/Instagram/LibCST).\n\n## Usage\n\nSimply provide a valid Python source code file as one of the argument and it will try to fix any issues it could find.\n\n```\nUsage: pybetter [OPTIONS] [PATHS]...\n\nOptions:\n  --noop           Do not make any changes to the source files.\n  --diff           Show diff-like output of the changes made.\n  --select CODES   Apply only improvements with the provided codes.\n  --exclude CODES  Exclude improvements with the provided codes.\n  --help           Show this message and exit.\n```\n\n\n\n## Example\n\n```shell\n# cat test.py\ndef f():\n    return (42, "Hello, world")\n\n# pybetter test.py\n--> Processing \'test.py\'...\n  [+] (B003) Remove parentheses from the tuple in \'return\' statement.\nAll done!\n\n# cat test.py\ndef f():\n    return 42, "Hello, world"\n\n```\n\n\n\n## Available fixers\n\n* **B001: Replace \'not A in B\' with \'A not in B\'**\n\n  Usage of `A not in B` over `not A in B` is recommended both by Google and [PEP-8](https://www.python.org/dev/peps/pep-0008/#programming-recommendations). Both of those forms are compiled to the same bytecode, but second form has some potential of confusion for the reader. \n\n  ```python\n  # BEFORE:\n  if not 42 in counts:\n      sys.exit(-1)\n  \n  # AFTER:\n  if 42 not in counts:\n      sys.exit(-1)\n  ```\n\n  \n\n* **B002: Default values for `kwargs` are mutable.**\n\n  As described in [Common Gotchas](https://docs.python-guide.org/writing/gotchas/#mutable-default-arguments) section of "The Hitchhiker\'s Guide to Python", mutable arguments can be a tricky thing. This fixer replaces any default values that happen to be lists or dicts with **None** value, moving initialization from function definition into function body.\n\n  ```python\n  # BEFORE\n  def p(a=[]):\n      print(a)\n    \n  # AFTER\n  def p(a=None):\n      if a is None:\n          a = []\n      \n      print(a)\n  ```\n\n  Be warned, that this fix may break code which *intentionally* uses mutable default arguments (e.g. caching).\n\n* **B003: Remove parentheses from the tuple in \'return\' statement.**\n\n  If you are returning a tuple from the function by implicitly constructing it, then additional parentheses around it are redundant.\n\n  ```python\n  # BEFORE:\n  def hello():\n      return ("World", 42)\n  \n  # AFTER:\n  def hello():\n      return "World", 42\n  ```\n\n* **B004: `__all__` attribute is missing.**\n\n  Regenerate missing `__all__` attribute, filling it with the list of top-level function and class names.\n\n  *NB*: It will ignore any names starting with `_` to prevent any private members from ending up in the list.\n  \n  ```python\n  # BEFORE:\n  def hello():\n      return ("World", 42)\n  \n  class F:\n      pass\n  \n  # AFTER:\n  def hello():\n      return "World", 42\n  \n  class F:\n      pass\n  \n  __all__ = [\n    "F",\n    "hello",\n  ]\n  ```\n  \n* **B005: Replace "A == None" with "A is None"**\n\n  "Comparisons to singletons like None should always be done with `is` or `is not`, never the equality operators." ([PEP8](https://www.python.org/dev/peps/pep-0008/))\n\n  ```python\n  # BEFORE:\n  \n  if a == None:\n      pass\n    \n  # AFTER:\n  \n  if a is None:\n      pass\n  ```\n  \n* **B006: Remove comparisons with either \'False\' or \'True\'.**\n\n  [PEP8](https://www.python.org/dev/peps/pep-0008/) recommends that conditions should be evaluated without explicit equality comparison with `True`/`False` singletons. In Python, every non-empty value is treated as `True` and vice versa,\n\n  so in most cases those comparisons can be safely eliminated.\n\n  *NB*: `is True` and `is False` checks are not affected, since they can be used to explicitly check for equality with a specific singleton, instead of using abovementioned "non-empty" heuristic.\n\n  ```python\n  # BEFORE:\n  \n  if a == False or b == True or c == False == True:\n      pass\n    \n  # AFTER:\n  \n  if a or b or c:\n      pass\n  \n  ```\n  \n* **B007: Convert f-strings without expressions into regular strings.**\n\n  It is wasteful to use f-string mechanism if there are no expressions to be extrapolated. \n\n  ```python\n  # BEFORE:\n  a = f"Hello, world"\n  \n  # AFTER:\n  a = "Hello, world"\n  ```\n\n* **B008: Collapse nested `with` statements**\n\n  Degenerate `with` statements can be rewritten as a single compound `with` statement, if following conditions are satisfied:\n\n  * There are no statements between `with` statements being collapsed;\n  * Neither of `with` statements has any leading or inline comments.\n\n  ```python\n  # BEFORE:\n  with a():\n      with b() as other_b:\n          print("Hello, world!")\n\n  # AFTER:\n  with a(), b() as other_b:\n      print("Hello, world!")\n  ```\n\n* **B009: Replace unhashable list literals in set constructors**\n\n  Lists cannot be used as elements of the sets due to them being mutable and hence "unhashable". We can fix the more trivial cases of list literals being used to create a set by converting them into tuples.\n\n  ```python\n  # BEFORE:\n  a = {\n    [1, 2, 3],\n  }\n  b = set([[1, 2], ["a", "b"]])\n  c = frozenset([[1, 2], ["a", "b"]])\n\n  # AFTER:\n  a = {\n    (1, 2, 3)\n  }\n  b = set([(1, 2), ("a", "b")])\n  c = frozenset([(1, 2), ("a", "b")])\n  ```\n\n\n\n**NB:** Each of the fixers can be disabled on per-line basis using [flake8\'s "noqa" comments](http://flake8.pycqa.org/en/3.1.1/user/ignoring-errors.html#in-line-ignoring-errors).\n\n## Installation\n\n```shell script\n# pip install pybetter\n```\n\n## Getting started with development\n\n```shell script\n# git clone https://github.com/lensvol/pybetter\n# poetry install\n```\n\n## License\n\nThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details\n\n## Authors\n\n* **Kirill Borisov** ([lensvol@gmail.com](mailto:lensvol@gmail.com))\n',
    'author': 'Kirill Borisov',
    'author_email': 'lensvol@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lensvol/pybetter',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
