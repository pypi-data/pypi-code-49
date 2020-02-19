# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yasl', 'yasl.bin']

package_data = \
{'': ['*']}

install_requires = \
['importlib-metadata']

entry_points = \
{'console_scripts': ['sparkbar = yasl.bin.sparkbar:main']}

setup_kwargs = {
    'name': 'yasl',
    'version': '1.0.2',
    'description': 'Yet another sparkline program/library',
    'long_description': '# Yet Another Sparkline (yasl)\n\n[![Actions Status](https://github.com/MomsFriendlyRobotCompany/yasl/workflows/CheckPackage/badge.svg)](https://github.com/MomsFriendlyRobotCompany/yasl/actions)\n![GitHub](https://img.shields.io/github/license/MomsFriendlyRobotCompany/yasl)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/yasl)\n![PyPI](https://img.shields.io/pypi/v/yasl)\n\n\nWhy? Well, it is actually really easy to do this and I wanted some different\ncontrols that the other programs didn\'t have. Also, I like the MIT license.\n\n## Usage\n\nYou can run it from the command line:\n\n```bash\n  kevin@dalek psl $ sparkbar.py  1 2 3E+0 4\n   ▂▅█\n  kevin@dalek psl $ sparkbar.py -z 1 2 3E+0 4\n   ▎▋█\n  kevin@dalek psl $ sparkbar.py 1 2 3 4 3 2 1 0 3 5\n  ▁▃▄▆▄▃▁ ▄█\n```\n\nOr call it from a python program:\n\n```python\n  #!/usr/bin/env python\n\n  from math import sin, pi\n  from yasl import Spark\n\n  if __name__ == "__main__":\n      sp = Spark()\n      data = [0,3,6,8.5,7,5,2,8,-8,1]\n\n      print(u\'max: {:.2f} min: {:.2f} [{}]\'.format(max(data),min(data),sp.vbar(data)))\n\n      data = []\n      for i in range(36):\n          data.append((sin(4*pi*i/36)))\n\n      print(u\'max: {:.2f} min: {:.2f} [{}]\'.format(max(data),min(data),sp.hbar(data)))\n\n      sp.dump()\n```\n\n```bash\n  kevin@dalek psl $ python3 example.py\n  max: 8.50 min: -8.00 [▃▅▆█▇▆▄▇ ▄]\n  max: 0.98 min: -0.98 [▌▋▊▉██▉▊▋▌▎▏    ▏▎▍▋▊▉▉█▉▊▋▌▎▏    ▏▎]\n```\n\n# MIT License\n\n**Copyright (c) 2017 Kevin J. Walchko**\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n',
    'author': 'walchko',
    'author_email': 'walchko@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://pypi.org/project/pyservos/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
