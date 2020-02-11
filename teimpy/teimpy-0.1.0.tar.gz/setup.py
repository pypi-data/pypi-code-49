# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['teimpy', 'teimpy.impl', 'teimpy.libsixel']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.16.0,<2.0.0', 'pillow>=6.0.0,<7.0.0']

setup_kwargs = {
    'name': 'teimpy',
    'version': '0.1.0',
    'description': 'Python libray for displaying images on terminal',
    'long_description': "# teimpy\nPython library for displaying image on terminal.\n\n[![Actions Status](https://github.com/ar90n/teimpy/workflows/Python%20package/badge.svg)](https://github.com/ar90n/teimpy/actions)\n[![PyPI version](https://badge.fury.io/py/teimpy.svg)](https://badge.fury.io/py/teimpy)\n[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/amplify-education/serverless-domain-manager/master/LICENSE)\n\n## Installation\n\n```bash\n$ pip\n```\n\n## Example\n\n```python\nimport numpy as np\nfrom teimpy import get_drawer, Mode\n\nR = np.array([1.0, 0, 0])\nG = np.array([0, 1.0, 0])\nB = np.array([0, 0, 1.0])\n\ndef _get_color(x, y):\n    tmp = (y * (1.0 - x) * R + (1.0 -y ) * x * G + (1.0 - y) * (1.0 - x) * B)\n    return (255 * tmp).astype(np.uint8)\n\ntics = np.linspace(0, 1, 128)\nxs, ys = np.meshgrid(tics, tics)\nbuffer = np.vectorize(_get_color, signature='(),()->(3)')(xs, ys)\nprint(get_drawer(Mode.ITERM2_INLINE_IMAGE).draw(buffer))\n```\n![Result of doit.py](https://github.com/ar90n/teimpy/raw/docs/doit.png)\n\n\n## Feature\n\n* Resize images to fit terminal size.\n* Drawing with iterm2 inline image.\n![Drawing with iterm2 inline image](https://github.com/ar90n/teimpy/raw/docs/inline_image.png)\n* Drawing with Braille fonts.\n![Drawing with Braille ofnts](https://github.com/ar90n/teimpy/raw/docs/braille.png)\n* Drawing with half block fonts.\n![Drawing with half block fonts](https://github.com/ar90n/teimpy/raw/docs/half_block.png)\n\n\n## License\nThis software is released under the MIT License, see [LICENSE](LICENSE).\n",
    'author': 'Masahiro Wada',
    'author_email': 'argon.argon.argon@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ar90n/teimpy',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
