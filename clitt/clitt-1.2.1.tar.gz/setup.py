# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clitt', 'clitt.config']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'colorama>=0.4.1,<0.5.0', 'tweepy>=3.8,<4.0']

entry_points = \
{'console_scripts': ['clitt = clitt.__main__:cli']}

setup_kwargs = {
    'name': 'clitt',
    'version': '1.2.1',
    'description': 'Use Twitter from your terminal!',
    'long_description': '# Clitt\n\nEver wanted to tweet straight from your terminal? Wait, is it just me?\n\n## How to install it?\n\nInstall Clitt using pip or pipx\n\n```bash\n    pip install --user clitt \\\\ pipx install clitt\n```\n\n## How to use it?\n\nClitt is meant to be simple (or at least as simple as a command line client for Twitter can be), so you just need to call `clitt` or `tt`, choose an action and pass the required parameters to perform the action. \n\nRunning `clitt` or `tt` for the first time will open a new tab on your browser with an authorization consent from Twitter, hit the authorize button, copy the code that will pop-up and paste it into the terminal. After the first time, your authorization token will be saved on your computer (and only there) for further uses.\n\n## What can i do with Clitt?\n\n#### Read your timeline\n\n```$ clitt read```\n\n![Clitt read](./docs/screenshot.png)\n\n#### Write a Tweet\n\n```$ clitt post "Hey, i\'m using Clitt to write this!"```\n\n#### DM someone\n\n```$ clitt dm @target "Hey, i\'m using Clitt to send you this DM!"```\n\n#### Read your chat with another user\n\n```$ clitt chat @target```\n\n## Future features\n\n- Search for tweets using keywords\n- Display and attach images to tweets\n- Implement filters and other customization options\n- Support theme colors\n\n## Contributing\n\nHave you thought about any cool features you wanted to see in Clitt? Send a PR. Found any bugs in the current implementation? Feel free to open an issue. Here\'s a guide to some things you might need to work on Clitt.\n\n##### Twitter dev account\n\nYou will need to make an application for a [Twitter developer account](https://developer.twitter.com/en/apply-for-access) if you want to publish your own version of Clitt, but for testing and development within this project you can use my key that is already included with this repository. If you have you own key, put it on the `config/keys.json` file inside the package.\n\n##### Tweepy\n\nTweepy is a Python wrapper for the Twitter REST API, it really makes life much more easier, you can check their [docs](https://tweepy.readthedocs.io/en/latest/) and probably will find what you looking for, but if you don\'t, search in the [Twitter docs](https://developer.twitter.com/en/docs).\n\n##### Clitt project structure\n\nIf you want to implement a new feature, write it in the `actions.py` file and if you need to, add a new argument treatment in `__main__.py`. Write simple and multiplatform code.',
    'author': 'Joao Vitor Maia',
    'author_email': 'maia.tostring@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/leviosar/clitt',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
