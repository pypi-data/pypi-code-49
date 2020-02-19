# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['evergreen', 'evergreen.cli', 'evergreen.errors', 'evergreen.metrics']

package_data = \
{'': ['*']}

install_requires = \
['Click>=7.0,<8.0',
 'PyYAML>=5.1,<6.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'requests>=2.22.0,<3.0.0',
 'structlog>=19.1.0,<20.0.0',
 'tenacity>=5.0.4,<6.0.0']

entry_points = \
{'console_scripts': ['evg-api = evergreen.cli.main:main']}

setup_kwargs = {
    'name': 'evergreen.py',
    'version': '1.1.0',
    'description': 'Python client for the Evergreen API',
    'long_description': '# Evergreen.py\n\nA client library for the Evergreen API written in python. Currently supports the V2 version of\nthe API. For more details, see https://github.com/evergreen-ci/evergreen/wiki/REST-V2-Usage .\n\n![PyPI](https://img.shields.io/pypi/v/evergreen.py.svg) [![Coverage Status](https://coveralls.io/repos/github/evergreen-ci/evergreen.py/badge.svg?branch=master)](https://coveralls.io/github/evergreen-ci/evergreen.py?branch=master)\n\n## Usage\n\n```\n>>> from evergreen.api import EvgAuth, EvergreenApi\n>>> api = EvergreenApi.get_api(EvgAuth(\'david.bradford\', \'***\'))\n>>> project = api.project_by_id(\'mongodb-mongo-master\')\n>>> project.display_name\n\'MongoDB (master)\'\n```\n\n### Command Line Application\n\nA command line application is included to explore the evergreen api data. It is called `evg-api`.\n\n```\n$ evg-api --json list-hosts\n{\n    "host_id": "host num 0",\n    "host_url": "host.num.com",\n    "distro": {\n        "distro_id": "ubuntu1804-build",\n        "provider": "static",\n        "image_id": ""\n    },\n    "provisioned": true,\n    "started_by": "mci",\n    "host_type": "",\n    "user": "mci-exec",\n    "status": "running",\n    "running_task": {\n        "task_id": null,\n        "name": null,\n        "dispatch_time": null,\n        "version_id": null,\n        "build_id": null\n    },\n    "user_host": false\n}\n...\n```\n\n\n## Contributors Guide\n\n### Testing\n\nUse poetry and pytest for testing.    \n```\n$ poetry install\n$ poetry run pytest\n```\n\nTo get code coverage information:\n\n```\n$ poetry run pytest --cov=src --cov-report=html\n```\n\nThis will generate an html coverage report in `htmlcov/` directory.\n\nThere are a few tests that are slow running. These tests are not run by default, but can be included\nby setting the env variable RUN_SLOW_TESTS to any value.\n\n```\n$ RUN_SLOW_TEST=1 poetry run pytest\n```\n\n### Versioning and Deploy\n\nBefore deploying a new version, please update the `CHANGELOG.md` file with a description of what\nis being changed.\n\nDeploys to [PyPi](https://pypi.org/project/evergreen.py/) are done automatically on merges to master. \nIn order to avoid overwriting a previous deploy, the version should be updated on all changes. The\n[semver](https://semver.org/) versioning scheme should be used for determining the version number. \n\nThe version is found in the `pyproject.toml` file.\n\n### Merging\n\nMerges to master should be done by the evergreen [commit queue](https://github.com/evergreen-ci/evergreen/wiki/Commit-Queue#pr).\nAfter a PR has been reviewed, add a comment with the text `evergreen merge` to merge the PR.\n',
    'author': 'Alexander Costas',
    'author_email': 'alexander.costas@mongodb.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/evergreen-ci/evergreen.py',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
