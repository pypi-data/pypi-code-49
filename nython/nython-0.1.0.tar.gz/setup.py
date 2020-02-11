# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nython']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'nython',
    'version': '0.1.0',
    'description': 'Seamless Nim extension modules for Python',
    'long_description': '# Nython \n\nBuild Python Extension Modules for Nim libraries.\n\n## Synopsis\n\nThis is using Nim\'s compileToC command to generate C code that Python can then pakcage as an extension module and compile natively when your package is installed elsewhere.\n\n## System Reqs\n\n- [Nim](https://nim-lang.org/)\n- [Nimpy](https://github.com/yglukhov/nimpy)\n\n## Install\n\nUsing your favorite Python package manager, this library lives on pypi\n\n```\npip install nython\n```\n\n## Usage\n\nSee the example folder of a working project that uses nython (and runs all the tests).\n\n### Poetry\n\n- Add `nython` as package dependancy\n- In the `[tool.poetry]` section of the `pyproject.toml`, add `build = "build.py"\n- Create the file `build.py` in top level of your project. This will be called by poetry when creating the package, essentially it just needs to have a `build` function that takes a dict of setup kwargs and adds to it.\n- Add your Nim modules, nythonize them, and pass them back\n- Note: you must pass in nimbase.h\n- Note: your nim code must live in a directory that is included in your package build process. It can live side by side with your python.\n\n```python\n# Example build.py script\nfrom nython import nythonize\nfrom os.path import expanduser\n\n\ndef build(setup_kwargs):\n    """Called by poetry, the args are added to the kwargs for setup."""\n    nimbase = expanduser("~") + "/.choosenim/toolchains/nim-1.0.4/lib/nimbase.h"\n    setup_kwargs.update(\n        {\n            "ext_modules": nythonize(\n                nimbase, [{"name": "adder", "path": "ponim/adder.nim"}]\n            ),\n        }\n    )\n```\n\n### Setuptools\n\nTodo - but basically just add `ext_modules = nythonize(nimbase, [{"name": "adder", "path": "ponim/adder.nim"}])` to your setup call\n\n## Development\n\n### Goals\n\nCreate a seamless development experience for integrating Nim code with Python. Nim should be so easy to use that eventually you just end up writing Nim-only modules for Python, and then realize you don\'t really need Python and migrate to just Nim. This package should enable Nim in places and companies where it can\'t be selected as the primary language for a project, but it can be reached for when performance is needed. This should be easier to use than Cython.\n\n### Tests\n\nCurrently this is tested by running the code in the example project. I would like to find a better way to do this, so if you have a good idea, feel free to contribute!\n\nCurrently:\n\n```\ncd example\npoetry shell\npoetry install\npoetry run py_test\n```\n\nAnd that is it. \n\n### TODOs\n\n- Support Nimble / full nim projects with dependancies\n- Allow for fine-grained compiler option tuning\n- Remove the spurious .so file that ends up in your project root dir.\n- Remove the dep fo passing in nimbase.h and find it on the system somehow\n- Possibly create a nim install in your local virtualenv somehow, with nimpy\n- Generate some performance tests, although that is more on nimpy than this package',
    'author': 'Seth Stadick',
    'author_email': 'sstadick@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sstadick/nython',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
