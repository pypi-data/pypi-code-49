# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['barbara']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.0.0,<8.0.0',
 'poetry-version>=0.1.3,<1.0.0',
 'python-dotenv>=0.10.1,<1.0.0',
 'pyyaml>=5.1.0,<6.0.0']

entry_points = \
{'console_scripts': ['barb = barbara.cli:barbara_develop']}

setup_kwargs = {
    'name': 'barbara',
    'version': '2.0.2',
    'description': 'Environment variable management',
    'long_description': ".. image:: https://repository-images.githubusercontent.com/131429006/7eb3f680-8572-11e9-8c3d-68b1476c50e8#\n\n|python| |downloads| |license| |version|\n\nEnvironment variable management\n\nNew in 2.0!\n-----------\n\n- Features have been dropped:\n  - Legacy templates aren't supported anymore\n  - Subvariables aren't supported anymore\n  - SSM support has been dropped, as there are better ways to do this\n\n- Schema-version has been added to document schema to make it easier for me to deprecate and change the schema if necessary\n\nInstallation\n------------\n\n.. code:: shell\n\n    $ pip install barbara\n\nUsage\n-----\n\nYAML Format (.env.yml)\n----------------------\n\n1. Create an ``.env.yml`` for your project\n\n.. code:: yaml\n\n   schema-version: 2\n   project:\n     name: your_project\n     output: env-file\n\n   environment:\n     ENVIRONMENT_NAME: development\n     DATABASE_URL: postgres://root@db:5432/mydb\n     DEBUG: 1\n     MEDIA_DIRS: media,static\n     CSRF_COOKIE_SECURE: 0\n\n\n\n2. Run ``barb`` and you'll be prompted for the values\n\n.. code:: bash\n\n   $ barb\n   env-file does not exist. Create it? [y/N]: y\n   Creating environment: env-file\n   Skip Existing: True\n   DATABASE_URL:\n   user [root]:\n   password [root]: wordpass\n   host [127.0.0.1]:\n   port [5432]:\n   db_name [sample]:\n   ENVIRONMENT_NAME [development]:\n   Environment ready!\n\n3. Inspect the generated file, see your values!\n\n.. code:: bash\n\n   $ cat .env\n   DATABASE_URL=root:wordpass@127.0.0.1:5432/sample\n   ENVIRONMENT_NAME=development\n\n\nWhy ``barbara``?\n----------------\n\nBecause `Barbara Liskov <https://en.wikipedia.org/wiki/Barbara_Liskov>`__ created the `Liskov Substitution\nPrinciple <https://en.wikipedia.org/wiki/Liskov_substitution_principle>`__ and is a prolific contributor to\ncomputer science and software engineering. Barbara is one of the Newton's metaphorical giants that enables us\nto see further. I humbly dedicate my project to her and her contributions and offer this project to its\nconsumers with a license befitting that dedication.\n\n\n\n.. |python| image:: https://img.shields.io/pypi/pyversions/barbara.svg?logo=python&logoColor=yellow&style=for-the-badge\n.. |downloads| image:: https://img.shields.io/pypi/dm/barbara.svg?style=for-the-badge\n.. |license| image:: https://img.shields.io/pypi/l/barbara.svg?style=for-the-badge\n.. |version| image:: https://img.shields.io/pypi/v/barbara.svg?style=for-the-badge\n",
    'author': 'Matthew de Verteuil',
    'author_email': 'onceuponajooks@gmail.com',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.0,<4.0.0',
}


setup(**setup_kwargs)
