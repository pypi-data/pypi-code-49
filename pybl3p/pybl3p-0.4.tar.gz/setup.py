# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pybl3p']

package_data = \
{'': ['*']}

install_requires = \
['notebook', 'pandas', 'requests', 'websockets']

setup_kwargs = {
    'name': 'pybl3p',
    'version': '0.4',
    'description': 'A python wrapper for the bl3p cryptocurrency exchange',
    'long_description': '# pybl3p\nA Python bl3p API\n\n## installation\n\n```shell script\n$ pip install pybl3p\n```\n\n## usage\n\nFor the public API\n```python\nfrom pybl3p.public import orderbook\norderbook()\n```\n\nFor the private API first set your public and private key as environment variables:\n```shell script\nexport BL3P_PUB="........-....-....-....-............"\nexport BL3P_PRIV="(long string with a-z/A-Z/0-9 and =)"\n```\n\n```python\nfrom pybl3p.private import depth_full\ndepth_full()\n```\n',
    'author': 'Gijs Molenaar',
    'author_email': 'gijs@pythonic.nl',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/gijzelaerr/pybl3p',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
