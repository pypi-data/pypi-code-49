# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['betterconf']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'betterconf',
    'version': '2.1',
    'description': 'Minimalistic Python library for your configs.',
    'long_description': '# Minimalistic Python library for your configs.\n\nBetterconf (**better config**) is a Python library for project configuration\nmanagment. It allows you define your config like a regular Python class.\n\nFeatures:\n\n* Easy to hack.\n* Less boilerplate.\n* Minimal code to do big things.\n\n## Installation\n\nI recommend you to use poetry:\n\n```sh\npoetry add betterconf\n```\n\nHowever, you can use pip:\n\n```sh\npip install betterconf\n```\n\n## How to?\n\nTry to write a simple config:\n```python\nfrom betterconf import field, Config\n\nclass MyConfig(Config):\n    my_var = field("my_var")\n\ncfg = MyConfig()\nprint(cfg.my_var)\n```\n\nTry to run:\n```sh\nmy_var=1 python our_file.py\n```\n\nWith default values:\n```python\nfrom betterconf import field, Config\n\nclass MyConfig(Config):\n    my_var = field("my_var", default="hello world")\n    my_second_var = field("my_second_var", default=lambda: "hi") # can be callable!\n\ncfg = MyConfig()\nprint(cfg.my_var)\nprint(cfg.my_second_var)\n# hello world\n# hi\n```\n\nOverride values when it\'s needed (for an example: test cases)\n```python\nfrom betterconf import field, Config\n\nclass MyConfig(Config):\n    my_var = field("my_var", default="hello world")\n\ncfg = MyConfig(my_var="WOW!")\nprint(cfg.my_var)\n# WOW!\n```\n\nBy default **betterconf** gets all values from `os.environ` but sometimes we need much.\nYou can create own `field\'s value provider` in minutes:\n\n```python\nfrom betterconf import field, Config\nfrom betterconf.config import AbstractProvider\n\nclass NameProvider(AbstractProvider):\n    def get(self, name: str):\n        return name\n\nclass Cfg(Config):\n    my_var = field("my_var", provider=NameProvider())\n\ncfg = Cfg()\nprint(cfg.my_var)\n# my_var\n```\n\nAlso we can cast our values to python objects (or just manipulate them):\n\n```python\nfrom betterconf import field, Config\n# out of the box we have `to_bool` and `to_int`\nfrom betterconf.caster import to_bool, to_int, AbstractCaster\n\n\nclass DashToDotCaster(AbstractCaster):\n    def cast(self, val: str):\n        return val.replace("-", ".")\n\nto_dot = DashToDotCaster()\n\nclass Cfg(Config):\n    integer = field("integer", caster=to_int)\n    boolean = field("boolean", caster=to_bool)\n    dots = field("dashes", caster=to_dot)\n\ncfg = Cfg()\nprint(cfg.integer, cfg.boolean, cfg.dots)\n# -500, True, hello.world\n\n```\n\n```sh\ninteger=-500 boolean=true dashes=hello-world python our_file.py\n```\n\n\n\n## License\nThis project is licensed under MIT License.\n\nSee [LICENSE](LICENSE) for details.\n\n\nMade with :heart: by [prostomarkeloff](https://github.com/prostomarkeloff) and our contributors.\n',
    'author': 'prostomarkeloff',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/prostomarkeloff/betterconf',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
