# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jollyip']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'icmplib>=1.0.2,<2.0.0', 'rich>=0.3.3,<0.4.0']

entry_points = \
{'console_scripts': ['jollyip = jollyip.cli:run_ping']}

setup_kwargs = {
    'name': 'jollyip',
    'version': '0.0.2',
    'description': 'Scan an IP range, but happily',
    'long_description': '<div align="center">\n  <br/>\n  <h1>Jolly IP</h1>\n  <br/>\n  <strong>Scan an IP range, but happily.</strong>\n  <br/>\n  <br/>\n  <pre>\n  Jolly IP is the happier, Java-free alternative to Angry IP Scanner.</pre>\n</div>\n\n## Installation\n\n```console\n$ pip3 install --user jollyip\n```\n\n- jollyIP requires **Python 3.5 or later**\n- jollyIP must be run as root (`sudo jollyip`)\n\n## About\n\nJolly IP was made during a fit of rage, after being told I had to install Java in order to install [Angry IP Scanner](https://angryip.org/) on macOS (which I refuse to do). While Angry IP is a great app, as a network engineer, most of the time I just need a quick CLI solution to scan something or generate some ARP entries. Jolly IP has the added advantage of being able to specify hosts, subnets, ranges, or any combination thereof in a single command.\n\nAs such, very little testing outside macOS has been done. That said, The [underlying ICMP library](https://github.com/ValentinBELYN/icmplib) supports macOS, Linux, and Windows, as do all other minor dependencies. If you run into a compatibility issue, please [raise an issue](https://github.com/checktheroads/jollyip/issues) and I\'ll do what I can.\n\n## Usage\n\n### IP\n\n```console\n# jollyip 192.0.2.1\nStarting jolly ping to 192.0.2.1...\n\n  Response from 192.0.2.1 received in 28.32 ms\n\nCompleted jolly ping to 192.0.2.1\n\n┏━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━┓\n┃ Targets ┃ Transmitted ┃ Alive ┃ Unreachable ┃\n┡━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━┩\n│ 1       │ 1           │ 1     │ 0           │\n└─────────┴─────────────┴───────┴─────────────┘\n```\n\n### Subnet\n\n```console\n# jollyip 2001:db8::/126\nStarting jolly ping to 2001:db8::/126...\n\n  Response from 2001:db8::1 received in 117.16 ms\n  Response from 2001:db8::2 received in 102.13 ms\n  2001:db8::3 is unreachable\n\nCompleted jolly ping to 2001:db8::/126\n```\n\n### Range\n\n```console\n# jollyip 192.0.2.1-6\nStarting jolly ping to 192.0.2.1-6...\n\n  Response from 192.0.2.1 received in 26.68 ms\n  Response from 192.0.2.2 received in 26.52 ms\n  Response from 192.0.2.3 received in 24.91 ms\n  192.0.2.4 is unreachable\n  192.0.2.5 is unreachable\n  Response from 192.0.2.6 received in 30.06 ms\n\nCompleted jolly ping to 192.0.2.1-6\n\n┏━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━┓\n┃ Targets ┃ Transmitted ┃ Alive ┃ Unreachable ┃\n┡━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━┩\n│ 6       │ 6           │ 4     │ 2           │\n└─────────┴─────────────┴───────┴─────────────┘\n```\n\n### Complex Range\n```console\n# jollyip 192.0.2.1,192.0.2.9-13,192.0.2.64/29\nStarting jolly ping to 192.0.2.1,192.0.2.9-13,192.0.2.64/29...\n\n  Response from 192.0.2.1 received in 29.96 ms\n  192.0.2.9 is unreachable\n  Response from 192.0.2.10 received in 26.49 ms\n  Response from 192.0.2.11 received in 23.04 ms\n  Response from 192.0.2.12 received in 25.28 ms\n  192.0.2.13 is unreachable\n  192.0.2.64 is unreachable\n  192.0.2.65 is unreachable\n  192.0.2.66 is unreachable\n  192.0.2.67 is unreachable\n  192.0.2.68 is unreachable\n  192.0.2.69 is unreachable\n  192.0.2.70 is unreachable\n  192.0.2.71 is unreachable\n\nCompleted jolly ping to 192.0.2.1,192.0.2.9-13,192.0.2.64/29\n\n┏━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━┓\n┃ Targets ┃ Transmitted ┃ Alive ┃ Unreachable ┃\n┡━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━┩\n│ 14      │ 14          │ 4     │ 10          │\n└─────────┴─────────────┴───────┴─────────────┘\n```\n\n### Mixing Protocols\n```console\n# jollyip 2001:db8::0/126,192.0.0.241,192.0.2.1-2\n\nStarting jolly ping to 2001:db8::/126,192.0.0.241,192.0.2.1-2...\n\n  Response from 2001:db8::1 received in 107.85 ms\n  Response from 2001:db8::2 received in 112.27 ms\n  2001:db8::3 is unreachable\n  Response from 192.0.0.241 received in 43.93 ms\n  Response from 192.0.2.1 received in 29.02 ms\n  Response from 192.0.2.2 received in 25.38 ms\n\nCompleted jolly ping to 2001:db8::/126,192.0.0.241,192.0.2.1-2\n\n┏━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━┳━━━━━━━━━━━━━┓\n┃ Targets ┃ Transmitted ┃ Alive ┃ Unreachable ┃\n┡━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━╇━━━━━━━━━━━━━┩\n│ 7       │ 7           │ 5     │ 2           │\n└─────────┴─────────────┴───────┴─────────────┘\n```',
    'author': 'Matt Love',
    'author_email': 'matt@allroads.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/checktheroads/jollyip',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
