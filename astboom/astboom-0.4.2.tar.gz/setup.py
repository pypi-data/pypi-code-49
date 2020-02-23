# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['astboom', 'astboom.visualizers']

package_data = \
{'': ['*']}

install_requires = \
['asciitree>=0.3.3,<0.4.0',
 'click>=7.0,<8.0',
 'libcst>=0.3.1,<0.4.0',
 'pyyaml>=5.3,<6.0']

entry_points = \
{'console_scripts': ['astboom = astboom.cli:cli']}

setup_kwargs = {
    'name': 'astboom',
    'version': '0.4.2',
    'description': 'Visualize Python AST in console.',
    'long_description': "# astboom\n![PyPI](https://img.shields.io/pypi/v/astboom) \n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/astboom)\n![GitHub](https://img.shields.io/github/license/lensvol/astboom)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\nVisualize Python AST/CST/ST in console using ASCII graphics using various engines.\n\nEngines available:\n* **[ast](https://docs.python.org/3/library/ast.html)** module\n* **[parser](https://docs.python.org/3/library/parser.html)**  module\n* **lib2to3**\n* **[LibCST](https://github.com/Instagram/LibCST)**\n\n## Example\n\n![Example usage](https://raw.githubusercontent.com/lensvol/astboom/master/docs/example.png)\n\n## Usage\n\nSimply provide a valid Python source code string as an argument\nand a corresponding AST/CST/ST will be displayed.\n\n### AST\n\n```\nUsage: astboom ast [OPTIONS] [SOURCE]\n\n  Display Abstract Syntax Tree for a given source.\n\nOptions:\n  --no-pos      Hide 'col_offset' and 'lineno' fields.\n  --hide-empty  Hide empty fields.\n```\n\n### lib2to3 CST\n\n```\nUsage: astboom cst [OPTIONS] [SOURCE]\n\n  Display Concrete Source Tree for a given source.\n\nOptions:\n  --show-prefix  Display value stored in 'prefix' field of the node.\n```\n\n### Python parse tree\n\n```\nUsage: astboom st [OPTIONS] [SOURCE]\n\n  Display Python parse tree for a given source.\n\n```\n\n### LibCST tree\n\n```\nUsage: astboom libcst [OPTIONS] [SOURCE]\n\n  Display LibCST tree for a given source.\n\nOptions:\n  --hide-default   Hide fields that contain default value\n                   (MaybeSentinel.DEFAULT).\n  --hide-empty     Hide fields that contain empty values ([], (), '').\n  --hide-fmt       Hide formatting-related fields and objects (whitespace,\n                   newlines).\n  --show-children  Show contents of the 'children' attribute.\n```\n\nIf no source provided as an argument, then tool will attempt to read it\nfrom *STDIN*.\n\n## Installation\n\n```shell script\n# pip install astboom\n```\n\n## Getting started with development\n\n```shell script\n# git clone https://github.com/lensvol/astboom\n# poetry install\n```\n\n## License\n\nThis project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details\n\n## Authors\n\n* **Kirill Borisov** ([lensvol@gmail.com](mailto:lensvol@gmail.com))\n",
    'author': 'Kirill Borisov',
    'author_email': 'lensvol@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lensvol/astboom',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
