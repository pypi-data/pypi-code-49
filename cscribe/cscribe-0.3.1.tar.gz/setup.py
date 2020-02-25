# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['cscribe']

package_data = \
{'': ['*']}

install_requires = \
['cmlkit>=2.0.0a14', 'dscribe>=0.3,<0.4', 'numpy>=1.15']

setup_kwargs = {
    'name': 'cscribe',
    'version': '0.3.1',
    'description': 'cmlkit plugin for the dscribe package',
    'long_description': "# cscribe 🐫🖋️\n\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/cscribe.svg) [![PyPI](https://img.shields.io/pypi/v/cscribe.svg)](https://pypi.org/project/cscribe/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black) \n\n`cscribe` is a [`cmlkit`](https://github.com/sirmarcel/cmlkit/) plugin for [`dscribe`](https://github.com/SINGROUP/dscribe).\n\nIt provides `cmlkit`-style `Components` for the representations implemented in `dscribe`. At the moment, it supports:\n\n- `SOAP`: Supported, tested, used in [`repbench`](https://marcel.science/repbench).\n- `SF`: Supported, but only `g2` and `g4`. Untested in production.\n- `MBTR`: Supported, but untested in production. Local MBTR is also supported, but also untested.\n- Coulomb matrix, sine matrix, or ewald sum matrix are not currently supported. (Please submit a pull request!)\n\nIn general, `cscribe` implements a subset of the full capabilities of `dscribe`, in order to stay consistent with the choices made in `cmlkit`. For instance, you can't specify whether `periodic` is turned on or not, and `sparse` is not implemented. Please feel free to build your own customised `Components` based on the code here!\n\nThe exact parameters are documented in the code itself, please have a look!\n\n## Installation\n\n```\npip install cscribe\nexport CML_PLUGINS=cscribe\n````\n\nOr add `cscribe` to `$CML_PLUGINS` in your `.bashrc` or equivalent.\n",
    'author': 'Marcel Langer',
    'author_email': 'dev@sirmarcel.com',
    'url': 'https://github.com/sirmarcel/cscribe',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
