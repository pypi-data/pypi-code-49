# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cvapianalyser']

package_data = \
{'': ['*'], 'cvapianalyser': ['templates/*']}

install_requires = \
['cvapianalyser', 'jinja2', 'pyyaml', 'requests==2.22.0']

entry_points = \
{'console_scripts': ['cvapianalyser = cvapianalyser.CVApiAnalyser:main']}

setup_kwargs = {
    'name': 'cvapianalyser',
    'version': '1.1.0',
    'description': 'plugin tool for capturing API coverage with input of a SPEC file against API shark of CloudVector',
    'long_description': "# CV-APIAnalyser\n\ncvapianalyser is a Python library for analysing the api traffic captured by CloudVector's APIShark against an APISPEC for identifying the gap in API coverage mostly useful in a QA environment to understand the gap in test coverage. \n\nVisit https://www.cloudvector.com/api-shark-free-observability-security-monitoring-tool/#apishark\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.\n\n```bash\npip install cvapianalyser\n```\n\n## Usage\n\n```python \ncvapianalyser \n\n****************************************************************************************************\nCloudVector CommunityEdition - Coverage analysis plugin\n****************************************************************************************************\n\nEnter CommunityEdition(CE) host in format <host>:<port> : x.x.x.x:y\nEnter your CommunityEdition(CE) username : sandeep\nCommunityEdition(CE) password:\nEnter recording in CE to compare with : recording1\n```\n\ninstead of giving inputs every single time you can also alternatively create a file called my_cesetup.yaml in the path from where you are running the tool\n\n```yaml \nce_host:\nce_username:\nce_recording:\ninput_apispec:\n```\nyou can have multiple such my_cesetup.yaml for different CE setup or different recordings and run them from specific paths for its corresponding reports\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)",
    'author': 'Bala Kumaran',
    'author_email': 'balak@cloudvector.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
