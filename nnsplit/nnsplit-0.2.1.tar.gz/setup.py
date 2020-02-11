# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nnsplit']

package_data = \
{'': ['*'],
 'nnsplit': ['data/*',
             'data/de/*',
             'data/de/tfjs_model/*',
             'data/en/*',
             'data/en/tfjs_model/*']}

install_requires = \
['numpy>=1,<2', 'torch>=1.4,<2.0']

setup_kwargs = {
    'name': 'nnsplit',
    'version': '0.2.1',
    'description': 'Fast, robust sentence splitting with bindings for Python, Rust and Javascript.',
    'long_description': '# NNSplit Python Bindings\n\n![PyPI](https://img.shields.io/pypi/v/nnsplit)\n![CI](https://github.com/bminixhofer/nnsplit/workflows/CI/badge.svg)\n![License](https://img.shields.io/github/license/bminixhofer/nnsplit)\n\nFast, robust sentence splitting with bindings for Python, Rust and Javascript and pretrained models for English and German.\n\n## Installation\n\nNNSplit has PyTorch as the only dependency.\n\nInstall it with pip: `pip install nnsplit`\n\n## Usage\n\n```python\n>>> from nnsplit import NNSplit\n>>> splitter = NNSplit("en")\n# NNSplit does not depend on proper punctuation and casing to split sentences\n>>> splitter.split(["This is a test This is another test."])\n[[[Token(text=\'This\', whitespace=\' \'),\n   Token(text=\'is\', whitespace=\' \'),\n   Token(text=\'a\', whitespace=\' \'),\n   Token(text=\'test\', whitespace=\' \')],\n  [Token(text=\'This\', whitespace=\' \'),\n   Token(text=\'is\', whitespace=\' \'),\n   Token(text=\'another\', whitespace=\' \'),\n   Token(text=\'test\', whitespace=\'\'),\n   Token(text=\'.\', whitespace=\'\')]]]\n```\n\nModels for German (`NNSplit("de")`) and English (`NNSplit("en")`) come prepackaged with NNSplit. Alternatively, you can also load your own model:\n\n```python\nimport torch\nmodel = torch.jit.load("/path/to/your/model.pt") # a regular nn.Module works too\n\nsplitter = NNSplit(model)\n```\n\nSee `train.ipynb` for the code used to train the pretrained models.\n\n## Development\n\nNNSplit uses [Poetry](https://python-poetry.org/) for dependency management. I made a small `Makefile` to automate some steps. Take a look at the `Makefile` and run `make install`, `make build`, `make test` to install, build and test the library, respectively.',
    'author': 'Benjamin Minixhofer',
    'author_email': 'bminixhofer@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
