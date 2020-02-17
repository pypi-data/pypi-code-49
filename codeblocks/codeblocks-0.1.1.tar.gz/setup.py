# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['codeblocks']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['codeblocks = codeblocks:main']}

setup_kwargs = {
    'name': 'codeblocks',
    'version': '0.1.1',
    'description': 'Extract and process code blocks from markdown files.',
    'long_description': '# codeblock\n\nExtract and process code blocks from markdown files.\n\n# Examples\n\nExtract Python code blocks:\n```\ncodeblock --python README.md\n```\n\nCheck formatting of Python code blocks with black:\n```\ncodeblock --python README.md | black --check -\n```\n\nReformat Python code blocks with black, in place:\n```\ncodeblock --python README.md -- black -\n```\n\nType check Python code blocks with mypy:\n```\nmypy somemodule anothermodule <(codeblock --python README.md)\n```\n\n# Full type checking example\n\n```python\ndef plus(x: int, y: int) -> int:\n    return x + y\n\nplus(1, \'2\')\n```\n\n```\n$ mypy --pretty --strict <(codeblock --python README.md)\n/dev/fd/63:5: error: Argument 2 to "plus" has incompatible type "str"; expected "int"\n        plus(1, \'2\')\n                ^\nFound 1 error in 1 file (checked 1 source file)\n```\n\n# TODO\n\n* [ ] protect against empty (and weird?) in-place modifications\n* [ ] use same regex for both modes\n* [ ] example for pytest\n* [ ] automatically add `async` for functions with `await` in them\n* [ ] support other languages\n* [ ] use proper markdown parser\n* [ ] support multiple files\n\n# Related\n\n* https://github.com/nschloe/excode\n* https://github.com/jonschlinkert/gfm-code-blocks\n* [blacken-docs][] ([does not support `black --check`][blacken-check])\n* [prettier works out of the box for supported languages][prettier] ([PR][prettier-pr])\n\n[blacken-docs]: https://github.com/asottile/blacken-docs\n[blacken-check]: https://github.com/asottile/blacken-docs/issues/42\n[prettier]: https://prettier.io/blog/2017/11/07/1.8.0.html#markdown-support\n[prettier-pr]: https://github.com/prettier/prettier/pull/2943\n',
    'author': 'Alexey Shamrin',
    'author_email': 'shamrin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
