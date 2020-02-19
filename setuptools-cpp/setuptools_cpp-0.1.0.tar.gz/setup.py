# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['setuptools_cpp']

package_data = \
{'': ['*']}

install_requires = \
['pybind11', 'setuptools']

setup_kwargs = {
    'name': 'setuptools-cpp',
    'version': '0.1.0',
    'description': 'Simplified packaging for pybind11-based C++ extensions',
    'long_description': '<p align="center">\n  <a href="https://setuptools-cpp.davidmontague.xyz"><img src="https://setuptools-cpp.davidmontague.xyz/img/setuptools-cpp-logo.png" alt="setuptools-cpp"></a>\n</p>\n<p align="center">\n    Simplified packaging for <a href="https://pybind11.readthedocs.io/en/master/">pybind11</a>-based C++ extensions\n</p>\n<p align="center">\n<img src="https://img.shields.io/github/last-commit/dmontagu/setuptools-cpp.svg">\n<a href="https://github.com/dmontagu/setuptools-cpp" target="_blank">\n    <img src="https://github.com/dmontagu/setuptools-cpp/workflows/build/badge.svg" alt="Build">\n</a>\n<a href="https://codecov.io/gh/dmontagu/setuptools-cpp" target="_blank">\n    <img src="https://codecov.io/gh/dmontagu/setuptools-cpp/branch/master/graph/badge.svg" alt="Coverage">\n</a>\n<a href="https://app.netlify.com/sites/trusting-archimedes-72b369/deploys">\n    <img src="https://img.shields.io/netlify/28b2a077-65b1-4d6c-9dba-13aaf6059877" alt="Netlify status">\n</a>\n<br />\n<a href="https://pypi.org/project/setuptools-cpp" target="_blank">\n    <img src="https://badge.fury.io/py/setuptools-cpp.svg" alt="Package version">\n</a>\n    <img src="https://img.shields.io/pypi/pyversions/setuptools-cpp.svg">\n    <img src="https://img.shields.io/github/license/dmontagu/setuptools-cpp.svg">\n</p>\n\n---\n\n**Documentation**: <a href="https://setuptools-cpp.davidmontague.xyz" target="_blank">https://setuptools-cpp.davidmontague.xyz</a>\n\n**Source Code**: <a href="https://github.com/dmontagu/setuptools-cpp" target="_blank">https://github.com/dmontagu/setuptools-cpp</a>\n\n---\n\n## Features\n\n* **`Pybind11Extension`**: For standard Pybind11 extensions from C++ source files\n* **`CMakeExtension`**: Useful for incorporating CMake-dependent libraries like CGAL\n* **Poetry Compatibility**: Easy to use with [poetry](https://python-poetry.org/)\'s [custom build system](https://github.com/python-poetry/poetry/issues/11#issuecomment-379484540)\n\n\n## Basic Usage\n\nYou can use the `CMakeExtension` or `Pybind11Extension` classes in your `setup.py` as follows:\n\n```python\nfrom setuptools import setup\n\nfrom setuptools_cpp import CMakeExtension, ExtensionBuilder, Pybind11Extension\n\next_modules = [\n    # A basic pybind11 extension in <project_root>/src/ext1:\n    Pybind11Extension(\n        "my_pkg.ext1", ["src/ext1/ext1.cpp"], include_dirs=["src/ext1/include"]\n    ),\n\n    # An extension with a custom <project_root>/src/ext2/CMakeLists.txt:\n    CMakeExtension(f"my_pkg.ext2", sourcedir="src/ext2")\n]\n\nsetup(\n    name="my_pkg",\n    version="0.1.0",\n    packages=["my_pkg"],\n    # ... other setup kwargs ...\n    ext_modules=ext_modules,\n    cmdclass=dict(build_ext=ExtensionBuilder),\n    zip_safe=False,\n)\n```\n\nYou can then use standard setuptools commands like `python setup.py install`.\n\nSee the [User Guide](https://setuptools-cpp.davidmontague.xyz/user-guide/) for more details.\n\n## Requirements\n\nThis package is intended for use with Python 3.6+.\n\n## Installation\n\n```bash\npip install setuptools-cpp\n```\n\n## License\n\nThis project is licensed under the terms of the MIT license.\n',
    'author': 'David Montague',
    'author_email': 'davwmont@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://setuptools-cpp.davidmontague.xyz',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
