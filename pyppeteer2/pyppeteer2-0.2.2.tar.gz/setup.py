# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyppeteer']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.3,<2.0.0',
 'pyee>=7.0.1,<8.0.0',
 'tqdm>=4.42.1,<5.0.0',
 'urllib3>=1.25.8,<2.0.0',
 'websockets>=8.1,<9.0']

entry_points = \
{'console_scripts': ['pyppeteer-install = pyppeteer.command:install']}

setup_kwargs = {
    'name': 'pyppeteer2',
    'version': '0.2.2',
    'description': 'Headless chrome/chromium automation library (unofficial port of puppeteer)',
    'long_description': "Pyppeteer2\n==========\n\n[![PyPI](https://img.shields.io/pypi/v/pyppeteer2.svg)](https://pypi.python.org/pypi/pyppeteer2)\n[![PyPI version](https://img.shields.io/pypi/pyversions/pyppeteer2.svg)](https://pypi.python.org/pypi/pyppeteer2)\n[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://miyakogi.github.io/pyppeteer2)\n[![Travis status](https://travis-ci.org/miyakogi/pyppeteer2.svg)](https://travis-ci.org/miyakogi/pyppeteer2)\n[![AppVeyor status](https://ci.appveyor.com/api/projects/status/nb53tkg9po8v1blk?svg=true)](https://ci.appveyor.com/project/miyakogi/pyppeteer2)\n[![codecov](https://codecov.io/gh/miyakogi/pyppeteer2/branch/master/graph/badge.svg)](https://codecov.io/gh/miyakogi/pyppeteer2)\n_Note: this is a WIP continuation of pyppeteer project_  \n\nUnofficial Python port of\n[puppeteer](https://github.com/GoogleChrome/puppeteer) JavaScript (headless)\nchrome/chromium browser automation library.\n\n* Free software: MIT license (including the work distributed under the Apache 2.0 license)\n* Documentation: https://miyakogi.github.io/pyppeteer\n\n## Installation\n\nPyppeteer requires python 3.6+.\n(experimentally supports python 3.5)\n\nInstall by pip from PyPI:\n\n```\npython3 -m pip install pyppeteer\n```\n\nOr install latest version from [github](https://github.com/miyakogi/pyppeteer):\n\n```\npython3 -m pip install -U git+https://github.com/miyakogi/pyppeteer.git@dev\n```\n\n## Usage\n\n> **Note**: When you run pyppeteer first time, it downloads a recent version of Chromium (~100MB).\n> If you don't prefer this behavior, run `pyppeteer-install` command before running scripts which uses pyppeteer.\n\n**Example**: open web page and take a screenshot.\n\n```py\nimport asyncio\nfrom pyppeteer import launch\n\nasync def main():\n    browser = await launch()\n    page = await browser.newPage()\n    await page.goto('http://example.com')\n    await page.screenshot({'path': 'example.png'})\n    await browser.close()\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\n**Example**: evaluate script on the page.\n\n```py\nimport asyncio\nfrom pyppeteer import launch\n\nasync def main():\n    browser = await launch()\n    page = await browser.newPage()\n    await page.goto('http://example.com')\n    await page.screenshot({'path': 'example.png'})\n\n    dimensions = await page.evaluate('''() => {\n        return {\n            width: document.documentElement.clientWidth,\n            height: document.documentElement.clientHeight,\n            deviceScaleFactor: window.devicePixelRatio,\n        }\n    }''')\n\n    print(dimensions)\n    # >>> {'width': 800, 'height': 600, 'deviceScaleFactor': 1}\n    await browser.close()\n\nasyncio.get_event_loop().run_until_complete(main())\n```\n\nPyppeteer has almost same API as puppeteer.\nMore APIs are listed in the\n[document](https://miyakogi.github.io/pyppeteer/reference.html).\n\n[Puppeteer's document](https://github.com/GoogleChrome/puppeteer/blob/master/docs/api.md#)\nand [troubleshooting](https://github.com/GoogleChrome/puppeteer/blob/master/docs/troubleshooting.md) are also useful for pyppeteer users.\n\n## Differences between puppeteer and pyppeteer\n\nPyppeteer is to be as similar as puppeteer, but some differences between python\nand JavaScript make it difficult.\n\nThese are differences between puppeteer and pyppeteer.\n\n### Keyword arguments for options\n\nPuppeteer uses object (dictionary in python) for passing options to\nfunctions/methods. Pyppeteer accepts both dictionary and keyword arguments for\noptions.\n\nDictionary style option (similar to puppeteer):\n\n```python\nbrowser = await launch({'headless': True})\n```\n\nKeyword argument style option (more pythonic, isn't it?):\n\n```python\nbrowser = await launch(headless=True)\n```\n\n### Element selector method name (`$` -> `querySelector`)\n\nIn python, `$` is not usable for method name.\nSo pyppeteer uses\n`Page.querySelector()`/`Page.querySelectorAll()`/`Page.xpath()` instead of\n`Page.$()`/`Page.$$()`/`Page.$x()`. Pyppeteer also has shorthands for these\nmethods, `Page.J()`, `Page.JJ()`, and `Page.Jx()`.\n\n### Arguments of `Page.evaluate()` and `Page.querySelectorEval()`\n\nPuppeteer's version of `evaluate()` takes JavaScript raw function or string of\nJavaScript expression, but pyppeteer takes string of JavaScript. JavaScript\nstrings can be function or expression. Pyppeteer tries to automatically detect\nthe string is function or expression, but sometimes it fails. If expression\nstring is treated as function and error is raised, add `force_expr=True` option,\nwhich force pyppeteer to treat the string as expression.\n\nExample to get page content:\n\n```python\ncontent = await page.evaluate('document.body.textContent', force_expr=True)\n```\n\nExample to get element's inner text:\n\n```python\nelement = await page.querySelector('h1')\ntitle = await page.evaluate('(element) => element.textContent', element)\n```\n\n## Future Plan\n\n1. Catch up development of puppeteer\n    * Not intend to add original API which puppeteer does not have\n\n## Credits\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.\n",
    'author': 'pyppeteer',
    'author_email': 'pyppeteer@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pyppeteer/pyppeteer2',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
