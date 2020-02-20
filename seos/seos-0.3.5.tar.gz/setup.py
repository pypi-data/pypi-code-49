# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['seos']

package_data = \
{'': ['*']}

install_requires = \
['google-api-python-client>=1.7,<2.0',
 'google_auth_oauthlib>=0.4.1,<0.5.0',
 'oauth2client>=3,<4',
 'rainbow-bridge-logger>=0.6.0,<0.7.0']

entry_points = \
{'console_scripts': ['seos = seos:extract_logs']}

setup_kwargs = {
    'name': 'seos',
    'version': '0.3.5',
    'description': 'Simple Extractor on Sheets or SEOS wraps extraction on Google Sheets',
    'long_description': '# Seos\n\n[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)\n[![PyPI pyversions](https://img.shields.io/pypi/pyversions/seos)](https://pypi.python.org/pypi/seos/)\n[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/mamerisawesome/seos/graphs/commit-activity)\n[![Coverage](https://raw.githubusercontent.com/mamerisawesome/seos/master/assets/coverage.svg?sanitize=true)](https://github.com/mamerisawesome/seos)\n[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)\n\nSimple Extractor on Sheets (or SEOS) is an extraction tool focused on Google Sheet data scraping. It uses Google\'s Python API client to access those data; this allows the library to access on a lower level functions defined by Google without the need of using another Sheets abstraction.\n\n## Features\n\nSeos features are put below and their status if they\'re well-tested using PyTest.\n\n| Feature | Status            |\n|----------------|-------------------|\n| **Connection to a Google Sheet given an OAuth credentials file and Sheet ID** | ![Passed unit test](https://img.shields.io/static/v1?label=&message=Passed%20unit%20tests&color=green) |\n| **Extraction on a sheet with a defined scope** | ![Passed unit test](https://img.shields.io/static/v1?label=&message=Passed%20unit%20tests&color=green) |\n| **Sheet name switching** | ![Passed unit test](https://img.shields.io/static/v1?label=&message=Passed%20unit%20tests&color=green) |\n\n## Installation\n\n```bash\n# if using poetry\n# highly recommended\npoetry add seos\n\n# also works with standard pip\npip install seos\n```\n\n## Getting Started\n\nSeos uses APIs defined by Google to access Sheets data; but the idea is that developing with Seos should be understandable when connecting to a data and changing contexts; e.g. change in Sheet Name or change in scope.\n\nThe initial step would be to pass a credentials file and the sheet ID as an entrypoint to the data. It assumes that you have a credentials file taken from `Google Cloud` in `JSON format`.\n\n```python\nfrom seos import Seos\nextractor = Seos(\n    credentials_file="./credentials.json"\n    spreadsheet_id="<SPREADSHEET-ID>"\n)\n```\n\nOnce an extractor context is created, we can then define the `sheet name` and `scope` then executing extract if you\'re happy with the parameters.\n\n```python\nextractor.sheet_name = "Report - June 1, 1752"\nextractor.scope = "A1:D1"\nextractor.extract()\n```\n\nWith this, changing the scope and the sheet name will act as a cursor for your sheet data. We can get anything from the sheet just by changing the scope.\n\n```python\nextractor.sheet_name = "Report - June 1, 1752"\nextractor.scope = "A1:D" # get all from A1 until end of column D\nextractor.extract()\n```\n\nWe can even do sheet switching if necessary for data that contains several contexts.\n\n```python\nextractor.sheet_name = "Report - June 1, 1752"\nextractor.scope = "A1:D"\nextractor.extract()\n\nextractor.sheet_name = "Report - June 2, 1752"\nextractor.scope = "B5:G5"\nextractor.extract()\n```\n',
    'author': 'Almer Mendoza',
    'author_email': 'atmalmer23@gmail.com',
    'maintainer': 'Don Dilidili, Kiana Villaera',
    'maintainer_email': None,
    'url': 'https://github.com/mamerisawesome/seos',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
