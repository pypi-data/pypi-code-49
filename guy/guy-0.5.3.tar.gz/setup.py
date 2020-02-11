# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['guy']
install_requires = \
['tornado>=6.0,<7.0']

setup_kwargs = {
    'name': 'guy',
    'version': '0.5.3',
    'description': 'A simple module for making HTML GUI applications with python3',
    'long_description': '**GUY** is a py3 module, which let you quickly release a GUI (html/js) for yours python (>=3.5) scripts, targetting **any** platforms ... and **android** too. \n\nA simple **guy\'s app** code, could be :\n\n```python\nfrom guy import Guy\n\nclass Simple(Guy):\n    """<button onclick="self.test()">test</button>"""\n\n    async def test(self):\n        print("Your name is", await self.js.prompt("What\'s your name ?") )\n\nif __name__ == "__main__":\n    app=Simple()\n    app.run()\n```\n\nA **guy\'s app** can be runned in 3 modes :\n\n- can reuse a chrome browser (in app mode), on the host. To keep the minimal footprint. (**app mode**)\n- can embbed its CEF (like electron) (thanks cefpython3), to provide all, to the users. (**cef mode**)\n- can act as a classical web server. Any browser can be a client (**server mode**)\n\nA **guy\'s app** can be released as :\n\n - a simple py3 file, with only guy dependancy (**app mode** & **server mode**)), or with guy+cefpython3 dependancies (**cef mode**))\n - a freezed executable (pyinstaller compliant) (all modes)\n - a [pip/package app](https://guy-docs.glitch.me/howto_build_whl_package/) (all modes)\n - an **apk** for android (with buildozer/kivy) (**app mode** only)\n\nRead the [Guy\'s DOCUMENTATION](https://guy-docs.glitch.me/) !\n\nAvailable on :\n\n - [Guy\'s Github](https://github.com/manatlan/guy)\n - [Guy\'s Pypi](https://pypi.org/project/guy/)\n\nHere is a [demo](https://starter-guy.glitch.me/#/) ([sources](https://glitch.com/edit/#!/starter-guy)), of a simple guy\'s app (server mode).\n\nHere is a [demo](https://starter-guy-vuejs.glitch.me/#/) ([sources](https://glitch.com/edit/#!/starter-guy-vuejs)), of a guy\'s app serving a vuejs/sfc UI.\n\nHere is a simple **guy\'s app** (**app mode**):\n<p align="center">\n    <table>\n        <tr>\n            <td valign="top">\n                On Ubuntu<br>\n<img src="https://manatlan.github.io/guy/shot_ubuntu.png" width="300" border="1" style="border:1px solid black"/>             </td>\n            <td valign="top">\n                On Android10<br>\n    <img src="https://manatlan.github.io/guy/shot_android10.jpg" width="300" border="1" style="border:1px solid black"/>                \n           </td>\n        </tr>\n    </table>\n</p>\n\n[![Join the chat at https://gitter.im/guy-python/community](https://badges.gitter.im/jessedobbelaere/ckeditor-iconfont.svg)](https://gitter.im/guy-python/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)',
    'author': 'manatlan',
    'author_email': 'manatlan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/manatlan/guy',
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
