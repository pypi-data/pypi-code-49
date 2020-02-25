# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['basiclog']

package_data = \
{'': ['*']}

install_requires = \
['slackclient>=2.5.0,<3.0.0']

setup_kwargs = {
    'name': 'basiclog',
    'version': '0.1.1',
    'description': '',
    'long_description': '# Basic Log (basiclog)\n## Example code:\n```python\nimport traceback\nimport basiclog\n\nlogger = basiclog.log("debug", __file__)\n\n# for slack error messages\nlogger.add_slack_handler(slack_api_toke, slack_channel)\n\nlogger.info("Script has been started")\ntry:\n    main()\nexcept KeyboardInterrupt:\n    logger.info("Script has been stopped manually")\nexcept:\n    e = traceback.format_exc()\n    logger.error(e)\n```',
    'author': 'Ramon Brandt',
    'author_email': 'devramon22@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
