# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['brilliantimagery',
 'brilliantimagery.dng',
 'brilliantimagery.ljpeg',
 'brilliantimagery.meta_image',
 'brilliantimagery.ppm',
 'brilliantimagery.sequence',
 'brilliantimagery.tools']

package_data = \
{'': ['*']}

install_requires = \
['cython>=0.29.15,<0.30.0',
 'numpy>=1.18.1,<2.0.0',
 'opencv-contrib-python>=4.1.2,<5.0.0',
 'toml>=0.10.0,<0.11.0',
 'tqdm>=4.41.1,<5.0.0']

setup_kwargs = {
    'name': 'brilliantimagery',
    'version': '0.2.2',
    'description': 'A python DNG editing package.',
    'long_description': "Brilliant Imagery\n=================\n\nA DNG based photo editing package. It can do things such as:\n\n* Decode and render lossless JPG images.\n* Encode lessless JPG images.\n* Render DNG images.\n* Edit DNG metadata.\n* Ramp Adobe Lightroom edits for image sequences.\n* Stabilize shaky image sequences using the Adobe Lightroom crop property.\n\nDocumentation\n-------------\n\nDocs can be found at `brilliantimagery.org/docs <https://www.brilliantimagery.org/docs/>`_\n\nInstallation\n------------\n\nFrom PyPI\n~~~~~~~~~\n\n::\n\n$ pip install brilliantimagery\n\nFrom Source\n~~~~~~~~~~~\n\nThe `Poetry <https://python-poetry.org/>`_ package and dependency manager is used by BrilliantImagery so install it if you haven't already done so. Some of the project files must be compiled. This accomplished within the below instructions.\n\nClone the `git repo <https://github.com/brilliantimagery/brilliantimagery.git>`_.\n\nFrom within the top ``/brilliantimagery`` folder, the one that contains the ``pyproject.toml`` file, install BrilliantImagery:\n\n::\n\n$ poetry install\n\n\nDevelopment\n-----------\n\nTesting\n~~~~~~~\n\nRunning the included tests can be used as a way to ensure that the package has been properly installed.\n\n**Running Tests**\n\nTo run all of the tests:\n\n::\n\n$ poetry run pytest\n\n**Coverage Reports**\n\nTerminal coverage reports can be generated:\n\n::\n\n$ poetry run pytest --cov=brilliantimagery\n\nHTML coverage reports can be generated when tests are run:\n\n::\n\n$ poetry run pytest --cov=brilliantimagery --cov-report=html\n\nDocs\n~~~~\n\nAfter making changes to the docs, to update them, assuming ``./brilliantiamgery`` is the current working directory, activate a poetry shell:\n\n::\n\n$ poetry shell\n\nChange the working directory to the ``/docs`` folder:\n\n::\n\n$ cd docs\n\nAnd then run clean and make the html docs:\n\n::\n\n$ make clean && make html\n\nChangelog\n---------\n\n* 0.2.2: Fixed version bug.\n\n* 0.2.1: Fixed build bug and a test.\n\n* 0.2.0: Enabled saving and loading projects as well as reusing offsets and brightnesses between runs.\n\n* 0.1.1: Fixed bug affecting sequences where multiple images have the same stored capture time.\n",
    'author': 'Chad DeRosier',
    'author_email': 'chad.derosier@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://www.brilliantimagery.org',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.0,<4.0.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
