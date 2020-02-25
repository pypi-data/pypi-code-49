# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scrapy_new']

package_data = \
{'': ['*'], 'scrapy_new': ['templates/*']}

install_requires = \
['inflection>=0.3.1,<0.4.0', 'mako>=1.1.1,<2.0.0', 'scrapy>=1.8.0,<2.0.0']

entry_points = \
{'scrapy.commands': ['new = scrapy_new.new:NewCommand']}

setup_kwargs = {
    'name': 'scrapy-new',
    'version': '0.1.4',
    'description': 'A package providing code generation command for scrapy CLI',
    'long_description': "# scrapy-command-new\n\nA package providing code generation command for scrapy CLI.\n\n*The project is a WIP, so expect major changes and additions (latter, mostly).\nMaster branch is to be considered as always ready to use, with major changes/features introduced in feature branches.*\n\nThis is a part of a bigger project - [Scrapy Boilerplate](https://github.com/groupbwt/scrapy-boilerplate).\n\nThe command works with a specific scrapy project structure (not the default one). Rationale for this is described [here](https://github.com/groupbwt/scrapy-boilerplate#file-and-folder-structure).\n\n## Usage\n\nThis is a scrapy command to generate class files and automatically add imports to respective module's `__init__` files. It can be used as follows:\n\n```\nscrapy new spider SampleSpider\n```\n\nThe first argument (`spider`) is a type of class file to be generated, and can be one of the following:\n\n- command\n- extension\n- item\n- middleware\n- model\n- pipeline\n- spider_middleware\n- spider\n\nThe second argument is class name.\n\nAlso for `pipeline` and `spider` class an option `--rabbit` can be used to add RabbitMQ connection code to generated source.\n\nOption `--item` with value `CLASSNAME` is supported for generating pipelines, which adds an import and type-check for a provided item class to the resulting code.\n\nOption `--settings` is also supported for pipelines, with an optional integer value `PRIORITY` that adds the pipeline being generated to scrapy `settings.py` file with specified priority (default 300).\n\n## Installation\n\nThis command is included in the [Scrapy Boilerplate](https://github.com/groupbwt/scrapy-boilerplate) out of the box. If you want to install it manually, you can get it from PyPi:\n\n```\npip install scrapy-new\n```\n\n**Please note** that this package won't work with default Scrapy project structure, it requires a specific custom one, as described [here](https://github.com/groupbwt/scrapy-boilerplate#file-and-folder-structure).\n",
    'author': 'Kristobal Junta',
    'author_email': 'junta.kristobal@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/groupbwt/scrapy-command-new',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
