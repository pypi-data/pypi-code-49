# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['saitama', 'saitama.queries']

package_data = \
{'': ['*']}

install_requires = \
['psycopg2>=2.8.0,<3.0.0', 'toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['punch = saitama.punch:main']}

setup_kwargs = {
    'name': 'saitama',
    'version': '0.4.0',
    'description': 'A python toolset to manage postgres migrations and testing',
    'long_description': '<p align="center">\n<a href="https://travis-ci.org/spapanik/saitama"><img alt="Build" src="https://travis-ci.org/spapanik/saitama.svg?branch=master"></a>\n<a href="https://coveralls.io/github/spapanik/saitama"><img alt="Coverage" src="https://coveralls.io/repos/github/spapanik/saitama/badge.svg?branch=master"></a>\n<a href="https://github.com/spapanik/saitama/blob/master/LICENSE.txt"><img alt="License" src="https://img.shields.io/github/license/spapanik/saitama"></a>\n<a href="https://pypi.org/project/saitama"><img alt="PyPI" src="https://img.shields.io/pypi/v/saitama"></a>\n<a href="https://pepy.tech/project/saitama"><img alt="Downloads" src="https://pepy.tech/badge/saitama"></a>\n<a href="https://github.com/psf/black"><img alt="Code style" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>\n</p>\n\n# Saitama: A postgres migrations manager and test runner\n\nSaitama offers an easy way to manage migrations and run postgres unittests.\n\n## Installation\n\nThe easiest way is to use pip to install saitama.\n\n```bash\npip install --user saitama\n```\n\n## Configuration\nTo configure saitama for your project, you can use any toml file.\n\n```toml\n[tool.saitama]\nhost = "<postgres host>"\nport = "<postgres port>"\ndbname = "<postgres database name>"\nuser = "<postgres user>"\npassword = "<postgres password>"\nmigrations = "<path to migrations dir>"\ntests = "<path to tests dir>"\n```\n\nAll of settings are optional, and the default `host`, `port`, `dbname`, `user` and `password` are the ones specified by `psycopg2`, the default migrations directory is `migrations/`, relative to the parent directory of the toml file, and the default test directory is `tests/`, again relative to the toml file.\n\n\n## Usage\nSaitama, once installed offers a single command, `punch`, that controls the migrations and the testing. `punch` follows the GNU recommendations for command line interfaces, and offers:\n* `-h` or `--help` to print help, and\n* `-V` or `--version` to print the version\n\n### Migrations\nYou can use punch to migrate forward or backward to a specific migration. The migrations should be named `\\d+_.+\\.sql`. Backwards are considered all the migrations that the first underscore after the digits is followed by `backwards_`.\n\n```\nusage: punch migrate [-h] [-H HOST] [-P PORT] [-d DBNAME] [-u USER]\n                     [-p PASSWORD] [-s SETTINGS] [-D] [-f] [-b] [-y]\n                     [migration]\n\npositional arguments:\n  migration                        The target migration number. If unspecified,\n                                   punch will migrate to latest one\n\noptional arguments:\n  -h, --help                       Show this help message and exit\n  -H HOST, --host HOST             The postgres host\n  -P PORT, --port PORT             The postgres port\n  -d DBNAME, --dbname DBNAME       The postgres database\n  -u USER, --user USER             The postgres user\n  -p PASSWORD, --password PASSWORD The user\'s password\n  -s SETTINGS, --settings SETTINGS The path to the settings file\n  -D, --drop                       Drop the existing db and create a new one\n  -f, --fake                       Fake the migrations up to the specified one\n  -b, --backwards                  Backwards migration\n  -y, --yes                        Run in non-interactive mode\n```\n\n### Test\nTesting will create a database named `test_<dbname>`, run all the migrations to this database, run the tests in the test directory, and produce a report. An exit code 1 is returned if any assertion fails.\n\n```\nusage: punch test [-h] [-H HOST] [-P PORT] [-d DBNAME] [-u USER] [-p PASSWORD]\n                  [-s SETTINGS]\n\noptional arguments:\n  -h, --help                       Show this help message and exit\n  -H HOST, --host HOST             The postgres host\n  -P PORT, --port PORT             The postgres port\n  -d DBNAME, --dbname DBNAME       The postgres database\n  -u USER, --user USER             The postgres user\n  -p PASSWORD, --password PASSWORD The user\'s password\n  -s SETTINGS, --settings SETTINGS The path to the settings file\n```\n\n### Writing a migration\nIn order to write a migration you just have to write an sql file:\n\n```sql\n-- /path/to/0001_initial_migration.sql\nCREATE TABLE users(\n    user_id  INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,\n    username TEXT,\n    password TEXT\n);\n```\nYou can also specify a backwards migration\n\n```sql\n-- /path/to/0001_backwards_initial_migration.sql\nDROP TABLE users;\n```\n\n### Writing a test\nIn order to write a migration you just have to write an PL/pgSQL function in an sql file which returns the result of `unittest.result();`. You can make assertions by calling `unittest.assert`. The function should be in the `unittest` schema.\n\n```sql\n-- /path/to/test_name.sql\nCREATE FUNCTION unittest.bar()\n     RETURNS unittest.test_result\n    LANGUAGE plpgsql\nAS\n$$\nDECLARE\n   _cnt INT;\nBEGIN\n    INSERT\n      INTO users (username, password)\n    VALUES (\'user\', \'hashed_and_salted_password\');\n\n    SELECT count(*)\n      FROM users\n      INTO _cnt;\n\n    PERFORM unittest.assert(_cnt <> 0, \'No user was created!\');\n\n    RETURN unittest.result();\nEND\n$$;\n```\n',
    'author': 'Stephanos Kuma',
    'author_email': 'spapanik21@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/spapanik/saitama',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.0,<4.0.0',
}


setup(**setup_kwargs)
