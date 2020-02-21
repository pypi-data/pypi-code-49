# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pasteboard']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pasteboard',
    'version': '0.3.1',
    'description': 'Pasteboard - Python interface for reading from NSPasteboard (macOS clipboard)',
    'long_description': "# Pasteboard\n\n[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0) [![Build](https://github.com/tobywf/pasteboard/workflows/Build/badge.svg?branch=master&event=push)](https://github.com/tobywf/pasteboard/actions)\n\n[Pasteboard](https://pypi.org/project/pasteboard/) exposes Python bindings for reading and writing macOS' AppKit [NSPasteboard](https://developer.apple.com/documentation/appkit/nspasteboard). This allows retrieving different formats (HTML/RTF fragments, PDF/PNG/TIFF) and efficient polling of the pasteboard.\n\nNow with type hints!\n\n## Installation\n\nObviously, this module will only compile on **macOS**:\n\n```bash\npip install pasteboard\n```\n\n## Usage\n\n### Getting the contents\n\n```pycon\n>>> import pasteboard\n>>> pb = pasteboard.Pasteboard()\n>>> pb.get_contents()\n'pasteboard'\n>>> pb.get_contents(diff=True)\n>>>\n```\n\nUnsurprisingly, `get_contents` gets the contents of the pasteboard. This method\ntakes two optional arguments:\n\n**type** - The format to get. Defaults to `pasteboard.String`, which corresponds\nto [NSPasteboardTypeString](https://developer.apple.com/documentation/appkit/nspasteboardtypestring?language=objc). See the `pasteboard` module members for other\noptions such as HTML fragment, RTF, PDF, PNG, and TIFF. Not all formats of [NSPasteboardType](https://developer.apple.com/documentation/appkit/nspasteboardtype?language=objc) are implemented.\n\n**diff** - Defaults to `False`. When `True`, only get and return the contents if it has changed since the last call. Otherwise, `None` is returned. This can be used to efficiently monitor the pasteboard for changes, which must be done by polling (there is no option to subscribe to changes).\n\n`get_contents` will return the appropriate type, so [str](https://docs.python.org/3/library/stdtypes.html#str) for string types,\nand [bytes](https://docs.python.org/3/library/stdtypes.html#bytes) for binary types. `None` is returned when:\n\n* There is no data of the requested type (e.g. an image was copied but a string was requested)\n* **diff** is `True`, and the contents has not changed since the last call\n* An error occurred\n\n### Setting the contents\n\n```pycon\n>>> import pasteboard\n>>> pb = pasteboard.Pasteboard()\n>>> pb.set_contents('pasteboard')\nTrue\n>>>\n```\n\nAnalogously, `set_contents` sets the contents of the pasteboard. This method\ntakes two arguments:\n\n**data** - [str](https://docs.python.org/3/library/stdtypes.html#str) or [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object), required. There is no type checking. So if `type` indicates a string type and `data` is bytes-like but not UTF-8 encoded, the behaviour is undefined.\n\n**type** - The format to set. Defaults to `pasteboard.String`, which corresponds to [NSPasteboardTypeString](https://developer.apple.com/documentation/appkit/nspasteboardtypestring?language=objc). See the `pasteboard` module members for other options such as HTML fragment, RTF, PDF, PNG, and TIFF. Not all formats of [NSPasteboardType](https://developer.apple.com/documentation/appkit/nspasteboardtype?language=objc) are implemented.\n\n`set_contents` will return `True` if the pasteboard was successfully set; otherwise, `False`. It may also throw [RuntimeError](https://docs.python.org/3/library/exceptions.html#RuntimeError) if `data` can't be converted to an AppKit type.\n\n## Development\n\nYou don't need to know this if you're not changing `pasteboard.m` code. There are some integration tests in `tests.py` to check the module works as designed (using [pytest](https://docs.pytest.org/en/latest/) and [hypothesis](https://hypothesis.readthedocs.io/en/latest/)).\n\nThis project uses [pre-commit](https://pre-commit.com/) to run some linting hooks when committing. When you first clone the repo, please run:\n\n```\npre-commit install\n```\n\nYou may also run the hooks at any time:\n\n```\npre-commit run --all-files\n```\n\nDependencies are managed via [poetry](https://python-poetry.org/). To install all dependencies, use:\n\n```\npoetry install\n```\n\nThis will also install development dependencies (`pytest`). To run the tests:\n\n```\npoetry run pytest tests.py --verbose\n```\n\n## License\n\nFrom version 0.3.0 and forwards, this library is licensed under the Mozilla Public License Version 2.0. For more information, see `LICENSE`.\n",
    'author': 'Toby Fleming',
    'author_email': 'tobywf@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/tobywf/pasteboard',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
