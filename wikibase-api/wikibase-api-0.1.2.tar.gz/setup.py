# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wikibase_api', 'wikibase_api.models']

package_data = \
{'': ['*'], 'wikibase_api': ['utils/*']}

install_requires = \
['requests-oauthlib>=1.0,<2.0', 'requests>=2.20,<3.0']

setup_kwargs = {
    'name': 'wikibase-api',
    'version': '0.1.2',
    'description': 'Wrapper library for the Wikibase API',
    'long_description': '# wikibase-api\n\n**`wikibase-api` is a Python library for simple access to the [Wikibase API](https://www.wikidata.org/w/api.php?action=help).**\n\nIt simplifies the authentication process and can be used to query and edit information on Wikidata or any other Wikibase instance.\n\n**For a simpler, object-oriented abstraction of the Wikibase API, have a look at [`python-wikibase`](https://github.com/samuelmeuli/python-wikibase).**\n\n## Installation\n\n```sh\npip install wikibase-api\n```\n\n## Usage\n\nSimple example for fetching all information about a Wikidata page:\n\n```py\nfrom wikibase_api import Wikibase\n\nwb = Wikibase()\nr = wb.entity.get("Q1")\nprint(r)\n```\n\nOutput:\n\n```python\n{\n  "entities": {\n    "Q1": {\n      # ...\n    }\n  },\n  "success": 1,\n}\n```\n\n**See the [documentation](https://wikibase-api.readthedocs.io) for descriptions and examples of all commands.**\n\n## Development\n\n### Contributing\n\nSuggestions and contributions are always welcome! Please discuss larger changes via issue before submitting a pull request.\n\n### Setup\n\nSee [this guide](https://wikibase-api.readthedocs.io/en/latest/development/development.html) on how to set up a development environment for this package.\n\n## Related\n\n- [`python-wikibase`](https://github.com/samuelmeuli/python-wikibase) – Wikibase queries and edits made easy\n',
    'author': 'Samuel Meuli',
    'author_email': 'me@samuelmeuli.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/samuelmeuli/wikibase-api',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
