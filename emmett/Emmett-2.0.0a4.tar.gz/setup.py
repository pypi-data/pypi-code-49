# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['emmett',
 'emmett.asgi',
 'emmett.asgi.loops',
 'emmett.asgi.protocols',
 'emmett.asgi.protocols.http',
 'emmett.asgi.protocols.ws',
 'emmett.language',
 'emmett.libs',
 'emmett.orm',
 'emmett.orm.migrations',
 'emmett.routing',
 'emmett.templating',
 'emmett.testing',
 'emmett.tools',
 'emmett.tools.auth',
 'emmett.validators',
 'emmett.wrappers',
 'tests']

package_data = \
{'': ['*'],
 'emmett': ['assets/*', 'assets/debug/*'],
 'tests': ['languages/*', 'templates/*', 'templates/auth/*']}

install_requires = \
['click>=0.6',
 'h11>=0.9.0,<0.10.0',
 'pendulum>=2.0.0',
 'pyDAL==17.3',
 'pyaes>=1.6.0,<1.7.0',
 'python-rapidjson>=0.9.1,<0.10.0',
 'pyyaml>=5.3.0,<5.4.0',
 'renoir>=1.0.1,<1.1.0',
 'severus==1.0.0b2',
 'uvicorn>=0.11.1,<0.12.0',
 'websockets>=8.0']

extras_require = \
{':sys_platform != "win32"': ['httptools>=0.0.13,<0.1.0',
                              'uvloop>=0.14.0,<0.15.0']}

entry_points = \
{'console_scripts': ['emmett = emmett.cli:main']}

setup_kwargs = {
    'name': 'emmett',
    'version': '2.0.0a4',
    'description': 'The web framework for inventors',
    'long_description': '![Emmett](https://github.com/emmett-framework/emmett/blob/master/artwork/logo-bwb-xb-xl.png)\n\nEmmett is a full-stack Python web framework designed with simplicity in mind.\n\nThe aim of Emmett is to be clearly understandable, easy to be learned and to be \nused, so you can focus completely on your product\'s features:\n\n```python\nfrom emmett import App, request, response\nfrom emmett.orm import Database, Model, Field\nfrom emmett.tools import service, requires\n\nclass Task(Model):\n    name = Field.string()\n    is_completed = Field.bool(default=False)\n\napp = App(__name__)\napp.config.db.uri = "postgres://user:password@localhost/foo"\ndb = Database(app)\ndb.define_models(Task)\napp.pipeline = [db.pipe]\n\ndef is_authenticated():\n    return request.headers["Api-Key"] == "foobar"\n    \ndef not_authorized():\n    response.status = 401\n    return {\'error\': \'not authorized\'}\n\n@app.route(methods=\'get\')\n@service.json\n@requires(is_authenticated, otherwise=not_authorized)\nasync def todo():\n    page = request.query_params.page or 1\n    tasks = Task.where(\n        lambda t: t.is_completed == False\n    ).select(paginate=(page, 20))\n    return {\'tasks\': tasks}\n```\n\n[![pip version](https://img.shields.io/pypi/v/emmett.svg?style=flat)](https://pypi.python.org/pypi/emmett)\n![Tests Status](https://github.com/emmett-framework/emmett/workflows/Tests/badge.svg)\n\n## Documentation\n\nThe documentations is available under the [docs folder](https://github.com/emmett-framework/emmett/tree/master/docs) folder.\n\n## Examples\n\nThe "bloggy" example described in the [Tutorial](http://weppy.org/docs/latest/tutorial) is available under the *examples* folder. \n\n## Status of the project\n\nThis is an alpha stage aiming to have full async support. It can be used only with Python 3.7 and above versions.\n\n## How can I help?\n\nWe would be very glad if you contributed to the project in one or all of these ways:\n\n* Talking about Emmett with friends and on the web\n* Adding issues and features requests here on GitHub\n* Participating in discussions about new features and issues here on GitHub\n* Improving the documentation\n* Forking the project and writing beautiful code\n\n## License\n\nEmmmett is released under the BSD License.\n\nHowever, due to original license limitations, some components are included \nin Emmett under their original licenses. Please check the LICENSE file for \nmore details.\n',
    'author': 'Giovanni Barillari',
    'author_email': 'gi0baro@d4net.org',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/emmett-framework/emmett',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
