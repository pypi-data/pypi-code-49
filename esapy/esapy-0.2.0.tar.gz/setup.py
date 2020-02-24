# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['esapy']

package_data = \
{'': ['*']}

install_requires = \
['nbconvert', 'pyperclip>=1.7.0,<2.0.0', 'pyyaml>=5.1,<6.0', 'requests']

entry_points = \
{'console_scripts': ['esa-token = esapy.loadrc:get_token_and_team',
                     'esa-up = esapy.entrypoint:main',
                     'jupyter-esa-up = esapy.entrypoint:main']}

setup_kwargs = {
    'name': 'esapy',
    'version': '0.2.0',
    'description': 'A python implementation of esa.io API',
    'long_description': '# esapy\n\nA python implementation of esa.io API\n\nThe main purpose of this package is implementation of easy uploading and sharing jupyter notebook to esa.io service.\n\n\n\n## INSTALATION\n\n1. Install pandoc\n\n    ```shell\n    $ sudo apt install pandoc\n    ```\n    \n    This package call nbconvert internally.\n\n1. Install package\n\n    ```shell\n    $ pip install esapy\n    ```\n\n1. generate esa.io token with read/write permission.\n\n1. make configuration file in your home directory (~/.esapyrc).\n\n    ```YAML: ~/.esapyrc\n    token: your_token\n    team: your_team\n    ```\n\n    - You can set them as environment variables: ESA_PYTHON_TOKEN, ESA_PYTHON_TEAM.\n    - Environment variables are prior to .esapyrc file.\n    - You can check your token using `esa-token`. \n\n\n\n## HOW TO USE\n\n1. Prepare .ipynb file\n\n1. Convert to markdown and upload images.\n\n    ```shell\n    $ esa-up target.ipynb\n    ```\n\n    This package (for now) will call nbconvert and upload images, and will not upload markdown file as new post.\n\n1. Post a new article by copy-and-paste the generated markdown file.\n\n\n## DOCUMENT\n\n### commands\nThis package registers following cli commands.\n- esa-up <target.ipynb>\n  - upload your notebook\n- jupyter-esa-up <target.ipynb>\n  - an alias of `esa-up`\n- esa-token\n  - show your token and team name\n\n### config file\nThe config file (~/.esapyrc) should be written in yaml format.\nAn example is shown below.\n```yaml: ~/.esapyrc\ntoken: your_token\nteam: your_team\n\naction:\n  goto_clipboard: true\n```\n\nIf `action.goto_clipboard` is true, a markdown body with modified urls will be copied to clipboard.  Default is false.\n\n## License\nCopyright (c) 2020 Kosuke Mizuno  \nThis package is released under the MIT license (see LICENSE file).\n',
    'author': 'Kosuke Mizuno',
    'author_email': 'dotmapu@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/KosukeMizuno/esapy',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
