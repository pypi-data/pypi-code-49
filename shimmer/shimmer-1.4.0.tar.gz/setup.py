# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shimmer',
 'shimmer.display',
 'shimmer.display.components',
 'shimmer.display.programmable',
 'shimmer.display.widgets',
 'shimmer.engine',
 'shimmer.engine.entity',
 'shimmer.engine.programmable',
 'shimmer.engine.staged_entity',
 'shimmer.engine.widgets']

package_data = \
{'': ['*']}

install_requires = \
['cocos2d>=0.6.7,<0.7.0',
 'janus>=0.4.0,<0.5.0',
 'more-itertools>=8.0.2,<9.0.0',
 'pyglet==1.4.3',
 'toml>=0.9,<0.10']

setup_kwargs = {
    'name': 'shimmer',
    'version': '1.4.0',
    'description': 'Create games in python, without hassle - batteries included!',
    'long_description': 'Shimmer\n-------\n\n<a href="https://github.com/MartinHowarth/shimmer/actions"><img alt="Actions Status" src="https://github.com/MartinHowarth/shimmer/workflows/Test/badge.svg"></a>\n<a href="https://github.com/MartinHowarth/shimmer/blob/master/LICENSE"><img alt="License: MIT" src="https://img.shields.io/github/license/MartinHowarth/shimmer"></a>\n<a href="https://pypi.org/project/shimmer/"><img alt="PyPI" src="https://img.shields.io/pypi/v/shimmer"></a>\n<a href="https://pepy.tech/project/shimmer"><img alt="Downloads" src="https://pepy.tech/badge/shimmer"></a>\n<a href="https://github.com/MartinHowarth/shimmer"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>\n\nHello!\n\nTesting\n-------\nThe following command should be used to run the tests:\n\n    poetry run pytest tests\n\nFor tests where a window is displayed, read the test description and\npress `Y` or `N` to pass or fail the test. This is intended to allow humans\nto validate that components look and behave as expected.\n\nMost components have non-graphical testing as well that covers the event handling, \nbut that is no replacement for a real human deciding whether it looks and feels good!\n\n## Running all non-graphical tests.\nSet `SKIP_GUI_TESTS=1` in your environment to skip graphical tests.\n\nThis skips all tests that require a GUI and user interaction.\n',
    'author': 'Martin Howarth',
    'author_email': 'howarth.martin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/MartinHowarth/shimmer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
