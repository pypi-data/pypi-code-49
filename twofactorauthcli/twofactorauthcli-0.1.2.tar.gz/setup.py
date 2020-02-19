# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['twofactorauthcli']

package_data = \
{'': ['*']}

install_requires = \
['pyotp>=2.3.0,<3.0.0', 'pyyaml>=5.3,<6.0', 'tabulate>=0.8.6,<0.9.0']

entry_points = \
{'console_scripts': ['2fa = twofactorauthcli:main']}

setup_kwargs = {
    'name': 'twofactorauthcli',
    'version': '0.1.2',
    'description': '2FA in your computer',
    'long_description': '# Two Factor Authentication CLI\n\n> 2FA in your computer\n\n## HOWTO\n\nJust install the tool with `pip` and then use the shortcut `2fa`.\n\n```bash\n$ pip install twofactorauthcli\n$ 2fa\n```\n\nIn the use, the tool will show you where to config it.\n\n## TODO\n\n**This is a MVP**, usable but limited. There are some ideas to implement:\n\n- The tests are stupid, rethink them.\n- Explain how to get the codes.\n- Improve configuration, making the path configurable or even better making it editable trought the CLI.\n- Show how many time left for the next codes change.\n- Get a code fast and copied to clipboard, something like `2fa copy aws`.\n',
    'author': 'Angel Fernandez',
    'author_email': 'angelfernandezibanez@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/anxodio/twofactorauthcli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
