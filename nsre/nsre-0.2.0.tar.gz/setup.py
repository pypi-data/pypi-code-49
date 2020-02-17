# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nsre']

package_data = \
{'': ['*']}

install_requires = \
['networkx>=2.0,<3.0']

extras_require = \
{':python_version >= "3.6" and python_version < "3.7"': ['dataclasses>=0.6,<0.7']}

setup_kwargs = {
    'name': 'nsre',
    'version': '0.2.0',
    'description': 'Regular expressions for the 21st century. Match any data type.',
    'long_description': "Non-String Regular Expressions\n==============================\n\n[![Build Status](https://travis-ci.org/Xowap/nsre.svg?branch=develop)](https://travis-ci.org/Xowap/nsre)\n\nNSRE (Non-String Regular Expressions) is a new spin at regular expressions.\nIt's really abstract, even compared to regular expressions as you know them,\nbut it's also pretty powerful for some uses.\n\nHere's the twist: what if regular expressions could, instead of matching just\ncharacter strings, match any sequence of anything?\n\n```python\nfrom nsre import *\n\nre = RegExp.from_ast(seq('hello, ') + (seq('foo') | seq('bar')))\nassert re.match('hello, foo')\n```\n\nThe main goal here is matching NLU grammars when there is several possible\ninterpretations of a single word, however there is a lot of other things that\nyou could do. You just need to understand what NSRE is and apply it to\nsomething.\n\n> **Note** &mdash; This is inspired by\n> [this article](https://swtch.com/~rsc/regexp/regexp1.html) from Russ Cox,\n> which explains how Thompson NFA work, except that I needed to add some\n> features and then the implementation is much less elegant because I actually\n> don't know what I'm doing. But it seems to be working.\n\n## Documentation\n\n[✨ **Documentation is there** ✨](http://nsre.rtfd.io/)\n\n## Licence\n\nThis library is provided under the terms of the [WTFPL](./LICENSE).\n\nIf you find it useful, you can have a look at the\n[contributors](https://github.com/Xowap/nsre/graphs/contributors) page to\nknow who helped.\n",
    'author': 'Rémy Sanchez',
    'author_email': 'remy.sanchez@hyperthese.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://nsre.rtfd.io/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
