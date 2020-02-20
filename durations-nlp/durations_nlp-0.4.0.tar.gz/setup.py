# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['durations_nlp']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'durations-nlp',
    'version': '0.4.0',
    'description': 'A python durations parsing library.',
    'long_description': '# durations_nlp\n\n[![CircleCI](https://circleci.com/gh/timwedde/durations_nlp.svg?style=svg)](https://circleci.com/gh/timwedde/durations_nlp)\n[![codecov](https://codecov.io/gh/timwedde/durations_nlp/branch/master/graph/badge.svg)](https://codecov.io/gh/timwedde/durations_nlp)\n[![Downloads](https://pepy.tech/badge/durations_nlp)](https://pepy.tech/project/durations_nlp)\n\nA python durations parsing library, providing a straight-forward API to parse duration string representations such as `1d`, `1 day 2 hours` or `2 days 3h 26m 52s` and convert them to numeric values.\n\n## What and Why\nIt\'s easier and more straight forward to read a duration expressed in natural language (at least for a human), as an expression rather than an amount. When writing configuration files for example:\n\n```yaml\ninterval: 3 hours\n```\n\nis easier to understand for a human than\n\n```yaml\ninterval: 10800  # seconds\n```\n\n## Installation\n\n`durations_nlp` can be installed via pip:\n```bash\n$ pip install durations_nlp\n```\n\n## Usage\nTo parse a duration string representation, just instantiate a Duration object and let it work for you. A Duration representation is composed of as many ``<value><scale>`` pairs as you need to express it:\n* A value is an integer amount.\n* A scale is a duration unit in it\'s short or long form (both singular and plural).\n* Duration pairs can be separated with sep characters and expressions such as `,` or `and`\n\n### Example Input\n\n* `1d`\n* `2 days`\n* `2 days and 4 hours`\n* `4M, 22d and 6hours`\n\n### Scales Reference\n\n* Century: `c`, `century`, `centuries`\n* Decade: `D`, `decade`, `decades`\n* Year: `y`, `year`, `Year`\n* Month: `M`, `month`, `months`\n* Week: `w`, `week`, `weeks`\n* Day: `d`, `day`, `days`\n* Hour: `h`, `hour`, `hours`\n* Minute:`m`, `minute`, `minutes`\n* Second: `s`, `second`, `seconds`\n* Milisecond: `ms`, `milisecond`, `miliseconds`\n\n### Usage Example\n\n```python\nfrom durations_nlp import Duration\n\none_hour = "1hour"\n\none_hour_duration = Duration(one_hour)\none_hour_duration.to_seconds()\n# >>> 3600.0\none_hour_duration.to_minutes()\n# >>> 60.0\n\n# You can even compose durations in their short\n# and long variations\ntwo_days_three_hours = "2 days, 3h"\ntwo_days_three_hours_duration = Duration(two_days_three_hours)\ntwo_days_three_hours_duration.to_seconds()\n# >>> 183600.0\ntwo_days_three_hours_duration.to_hours()\n# >>> 51.0\n```\n',
    'author': 'Tim Wedde',
    'author_email': 'timwedde@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/timwedde/durations_nlp',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
