# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pixler']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pixler',
    'version': '0.1.1',
    'description': 'Draw a pixel map with braille characters',
    'long_description': '# Pixler\n\nA library to draw pixles with unicode braille characters\n\n## Example\n\n```\nIn [1]: from pixler import Pixler\n\nIn [2]: planet_pixel_map = [\n   ...:     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0],\n   ...:     [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],\n   ...:     [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],\n   ...:     [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],\n   ...:     [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],\n   ...:     [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],\n   ...:     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],\n   ...:     [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],\n   ...:     [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],\n   ...:     [1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],\n   ...:     [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],\n   ...:     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\n   ...: ]\n   ...:\n   ...: pixler = Pixler.from_pixels(planet_pixel_map)\n\nIn [3]: print(pixler.get_frame())\n⠀⢠⠒⣉⠕⢲⢉⠆\n⢀⢗⠉⠀⠀⢀⠇⠀\n⠣⠬⠒⠤⠔⠊⠀⠀\n```\n',
    'author': 'Axel',
    'author_email': 'pixler@absalon.is',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ikornaselur/pixler',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
