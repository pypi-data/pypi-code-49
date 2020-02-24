# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zuora_aqua_client_cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0,<8.0', 'flake8>=3.7,<4.0', 'requests>=2.22,<3.0']

entry_points = \
{'console_scripts': ['zacc = zuora_aqua_client_cli.cli:cli']}

setup_kwargs = {
    'name': 'zuora-aqua-client-cli',
    'version': '1.1.0',
    'description': 'Run ZOQL queries through AQuA from the command line',
    'long_description': '# zuora-aqua-client-cli [![Build Status](https://travis-ci.com/molnarjani/zuora-aqua-client-cli.svg?branch=master)](https://travis-ci.com/molnarjani/zuora-aqua-client-cli)\n\nRun ZOQL queries through AQuA from the command line\n\n\n# Installation\n\n#### Mac\n`pip3 install zuora-aqua-client-cli`\nThe executable will be installed to `/usr/local/bin/zacc`\n\n#### Linux\n`pip3 install zuora-aqua-client-cli`\nThe executable will be installed to `~/.local/bin/zacc`\n\nMake sure `~/.local/bin/` is added to your `$PATH`\n\n# Configuration\nConfiguration should be provided by the `-c /path/to/file` option.\n\nIf option is not provided, will be read from `~/.zacc.ini`\n\n#### Example config\n```\n[zacc]\n# When environement option is ommited the default environment will be used\ndefault_environment = preprod\n\n[prod]\n# Use production Zuora endpoints, defaults to `false`\nproduction = true                                            \nclient_id = <oauth_client_id>\nclient_secret = <oauth_client_secret>\n\n[mysandbox]\nclient_id = <oauth_client_id>\nclient_secret = <oauth_client_secret>\n```\n\n# Usage\n\n#### Cheatsheet\n```\n# List fiels for resource\n$ zacc describe Account\nAccount\n  AccountNumber - Account Number\n  AdditionalEmailAddresses - Additional Email Addresses\n  AllowInvoiceEdit - Allow Invoice Editing\n  AutoPay - Auto Pay\n  Balance - Account Balance\n  ...\nRelated Objects\n  BillToContact<Contact> - Bill To\n  DefaultPaymentMethod<PaymentMethod> - Default Payment Method\n  ParentAccount<Account> - Parent Account\n  SoldToContact<Contact> - Sold To\n\n# Request a bearer token, then exit\n$ zacc bearer\nBearer aaaaaaaaaaaaaaaaaaaaaaaaaaa\n\n# Execute an AQuA job\n$ zacc query -z "select Account.Name from Account where Account.CreatedDate > \'2019-01-10\'"\nAccount.Name\nJohn Doe\nJane Doe\n\n# Save results to CSV file instead of printing it\n$ zacc query -z ~/query_names.zoql -o account_names.csv\n\n# Execute an AQuA job from a ZOQL query file\n$ zacc query -z ~/query_names.zoql\nAccount.Name\nJohn Doe\nJane Doe\n\n# Use different configurations than default\n$ zacc -c ~/.myotherzaccconfig.ini -e notdefualtenv query -z ~/query_names.zoql\n```\n\n## Commands\n\n#### zacc\n```\nUsage: zacc [OPTIONS] COMMAND [ARGS]...\n\n  Sets up an API client, passes to commands in context\n\nOptions:\n  -c, --config-filename PATH  Config file containing Zuora ouath credentials\n                              [default: /Users/prezi/.zacc.ini]\n  -e, --environment TEXT      Zuora environment to execute on\n  --help                      Show this message and exit.\n\nCommands:\n  bearer    Prints bearer than exits\n  describe  List available fields of Zuora resource\n  query     Run ZOQL Query\n```\n\n#### zacc query\n```\nUsage: zacc query [OPTIONS]\n\n  Run ZOQL Query\n\nOptions:\n  -z, --zoql TEXT          ZOQL file or query to be executed\n  -o, --output PATH        Where to write the output to, default is STDOUT\n  -m, --max-retries FLOAT  Maximum retries for query\n  --help                   Show this message and exit.\n```\n\n#### zacc describe\n```\nzacc describe --help                                                                                                                      932ms \ue0b3 Thu Feb  6 14:58:13 2020\nUsage: zacc describe [OPTIONS] RESOURCE\n\n  List available fields of Zuora resource\n\nOptions:\n  --help  Show this message and exit.\n```\n\n#### zacc bearer\n```\nUsage: zacc bearer [OPTIONS]\n\n  Prints bearer than exits\n\nOptions:\n  --help  Show this message and exit.\n```\n\n# Useful stuff\nHas a lot of graphs on Resource relationships:\nhttps://community.zuora.com/t5/Engineering-Blog/AQUA-An-Introduction-to-Join-Processing/ba-p/13262\n',
    'author': 'Janos Molnar',
    'author_email': 'janosmolnar1001@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/molnarjani/zuora-aqua-client-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
