# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cson_to_markdown']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.2.1,<0.3.0', 'pyyaml>=5.1,<6.0', 'smart-getenv>=1.1,<2.0']

entry_points = \
{'console_scripts': ['cson_to_markdown = cson_to_markdown:main']}

setup_kwargs = {
    'name': 'cson-to-markdown',
    'version': '0.1.3',
    'description': 'Extracts the markdown section from .cson files.',
    'long_description': '# Cson To Markdown\n## What\nRecursively scans given folder for `.cson` files, extracts the metadata and markdown,\nand writes a `.md` file and a `meta/.yml` file.\nWritten specifically for use with [Boostnote](https://github.com/BoostIO/Boostnote).\n\n## Why?\nI write everything in Markdown format because I like the formatting, and my favourite markdown editor so far is Boostnote.\nEverything is stored in a dedicated git repository and pushed whenever changes occur.\nThis works great!\n\n*The problem* though, is that Boostnote stores the file in a `cson` format, without subfolders  and without legible note-titles.\nI wrote something that extracts this information without disturbing the original files, and writes both the markdown and the metadata somewhere else.\nThey\'re created in the subfolder to which they belong in the application, with the note title as filename.\n\n**Caution:** A new version is in the works and will be announced which might completely break this tool.\n\n## How to install\n\n`pip install cson-to-markdown`\n\n## How to use\n### 1. CLI\nI use Google\'s [python-fire](https://github.com/google/python-fire) to create the CLI.\nYou can run `cson_to_markdown --help` to get more information on the module.\n\nThere\'s 3 arguments that can be provided; `cson_to_markdown $arg1 $arg2 $arg3`\n\n1. The folder with the `.cson` files that need to be converted (looks recursive  in this path for all compatible files).\n1. **Optional** target folder for markdown file output. If no value is provided, they will be stored in the same folder as the `.cson` files.\n1. **Optional** folder containing the `boostnote.json` file. This contains the key-name pairs of the folders defined in the Boostnote aplication itself.\n\n```bash\n# Call module directly\ncson_to_markdown ~/folder/with/notes ~/output/folder ~/settings/dir\n\n# Through python\npython -m cson_to_markdown ~/folder/with/notes ~/output/folder ~/settings/dir\n```\n\n### 2. Python:\n```python\nfrom cson_to_markdown import FileConverter\n\n\nconverter = FileConverter("folder/with/cson", "optional/target/folder", "optional/boostnote/settings/dir")\nconverter.convert()\n```\n\n### 3. Git hooks\nYou can leverage the usefulness of git hooks, to make use of this module.\nBased off of [this StackOverflow answer](https://stackoverflow.com/a/12802592/7291804), I implemented the following:\n**Note:** This is not a clean way to do this, think before you copy paste this.\n\n1. Create pre-commit hook in notes repository:\n`vim .git/hooks/pre-commit`\n\n```bash\n#!/bin/bash\n\necho\ntouch .commit\nexit\n```\n\n2. Create post-commit hook to create and add new files to the commit:\n`vim .git/hooks/post-commit`\n\n```bash\n#!/bin/bash\n\ncson_to_markdown $INSERT_NOTES_FOLDER $OPTIONAL_MARKDOWN_OUTPUT_FOLDER $OPTIONAL_BOOSTNOTE_SETTINGS_FOLDER\n\nif [ -a .commit ]\n    then\n    rm .commit\n    git add .\n    git commit --amend -C HEAD --no-verify\nfi\nexit\n```\n\n3. Make both executable:\n`chmod u+x .git/hooks/pre-commit .git/hooks/post-commit`\n\n\n## How to configure\nThere are a few settings that can be configured through environment variables, defined in `cson_to_markdown/config.py`.\nWe will by default first look at an appropriately named environemnt variable, and fall back to the defaults if none were found.\n\nThese are the current settings, which work for the Boostnote use-case specifically.\n```python\n_config = {\n    "MARKDOWN_START": "content: \'\'\'",\n    "MARKDOWN_END": "\'\'\'",\n    "TITLE_INDICATOR": \'title: "\',\n    "FOLDER_INDICATOR": \'folder: "\',\n    "YAML_STRING_INDICATOR": \'"\',\n    "CSON_EXTENSION": ".cson",\n    "MARKDOWN_EXTENSION": ".md",\n    "METADATA_EXTENSION": ".yml",\n    "METADATA_FOLDER": "meta",\n    "BNOTE_SETTINGS_FILE": "boostnote.json",\n}\n```\n\nTo overwrite, simply set a new environment variable in your terminal, or add it to your `.bashrc` file:\n`export MARKDOWN_START="new start delimiter"`\n',
    'author': 'Bram Vereertbrugghen',
    'author_email': 'bramvereertbrugghen@live.be',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/BramVer/cson-to-markdown',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
