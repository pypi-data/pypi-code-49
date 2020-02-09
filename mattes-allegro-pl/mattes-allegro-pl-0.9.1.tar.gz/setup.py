# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['allegro_pl']

package_data = \
{'': ['*']}

install_requires = \
['allegro-pl-rest-api>=2020.1,<2021.0',
 'oauthlib>=3.0,<4.0',
 'requests-oauthlib>=1.2,<2.0',
 'tenacity>=6.0.0,<7.0.0',
 'zeep>=3.3,<4.0']

setup_kwargs = {
    'name': 'mattes-allegro-pl',
    'version': '0.9.1',
    'description': 'Python client for Allegro.pl API',
    'long_description': "Python client for Allegro.pl API\n================================\n\n.. image:: https://travis-ci.com/mattesilver/allegro-pl.svg?branch=master\n    :target: https://travis-ci.com/mattesilver/allegro-pl\n\n.. image:: https://img.shields.io/pypi/v/mattes-allegro-pl.svg\n    :target: https://pypi.org/project/mattes-allegro-pl/\n\n.. image:: https://codecov.io/gh/mattesilver/allegro-pl/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/mattesilver/allegro-pl\n\n\nSupports both Rest and SOAP APIs\n\nUsage:\n\n.. code-block::\n\n    import allegro_pl\n    cs = ClientCodeStore('CLIENT ID','CLIENT SECRET')\n    ts = TokenStore('ACCESS TOKEN','REFRESH TOKEN)\n\n    auth = ClientCredentialsAuth(cs, ts)\n    allegro = allegro_pl.Allegro(auth)\n\n    rest_service = allegro.rest_service()\n\n    categories = rest_service.get_categories(cat_id)\n\n    # access to soap service\n    soap_service = allegro.soap_service()\n\n    # direct access to rest and soap clients:\n    rest_service = allegro.rest_client()\n    soap_client = allegro.soap_client()\n",
    'author': 'Raphael Krupinski',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mattesilver/allegro-pl/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
