# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stail']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.11.14,<2.0.0',
 'click>=7.0,<8.0',
 'colorama>=0.4.3,<0.5.0',
 'pyfiglet>=0.8.post1,<0.9']

entry_points = \
{'console_scripts': ['stail = stail:main']}

setup_kwargs = {
    'name': 'stail',
    'version': '0.1.2',
    'description': 'Step Function tailing CLI tool',
    'long_description': '# STail\nCLI Tool to run and tail a step function synchronously.\n\nTail feature coming soon!\n\n## Installation:\n```bash\npip install stail\n```\n\n## Usage\n\n### run\nRuns a step function synchronously.\n```bash\nstail run --arn [state machine arn] --input [input]\n```\n####Options:\n  --help  Show this message and exit.\n\n##### Example:\n```bash\nstail run --arn arn:aws:states:<region>:955883056721:stateMachine:<name> --input "{\\"param\\":\\"hello\\"}"\n```\n\n### version\nDisplays the version.\n```bash\nstail version\n```\n\nAuthor: Iman Kamyabi\nFeedback: contact@imankamyabi.com',
    'author': 'Iman Kamyabi',
    'author_email': 'contact@imankamyabi.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/imankamyabi/stail',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
