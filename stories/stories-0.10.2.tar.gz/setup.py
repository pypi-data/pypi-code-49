# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['_stories',
 '_stories.contrib',
 '_stories.contrib.debug_toolbars',
 '_stories.contrib.debug_toolbars.django',
 '_stories.contrib.debug_toolbars.flask',
 '_stories.execute',
 'stories',
 'stories.contrib',
 'stories.contrib.debug_toolbars',
 'stories.contrib.sentry']

package_data = \
{'': ['*'],
 '_stories.contrib.debug_toolbars.django': ['templates/stories/debug_toolbar/*'],
 '_stories.contrib.debug_toolbars.flask': ['templates/stories/debug_toolbar/*']}

extras_require = \
{'mkdocs': ['mkdocs', 'mkdocs-material']}

entry_points = \
{'pytest11': ['stories = stories.contrib.pytest']}

setup_kwargs = {
    'name': 'stories',
    'version': '0.10.2',
    'description': 'Define a user story in the business transaction DSL',
    'long_description': "![logo](https://raw.githubusercontent.com/dry-python/brand/master/logo/stories.png)\n\n[![azure-pipeline](https://dev.azure.com/dry-python/stories/_apis/build/status/dry-python.stories?branchName=master)](https://dev.azure.com/dry-python/stories/_build/latest?definitionId=3&branchName=master)\n[![codecov](https://codecov.io/gh/dry-python/stories/branch/master/graph/badge.svg)](https://codecov.io/gh/dry-python/stories)\n[![docs](https://readthedocs.org/projects/stories/badge/?version=latest)](https://stories.readthedocs.io/en/latest/?badge=latest)\n[![gitter](https://badges.gitter.im/dry-python/stories.svg)](https://gitter.im/dry-python/stories)\n[![pypi](https://img.shields.io/pypi/v/stories.svg)](https://pypi.python.org/pypi/stories/)\n[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n\n---\n\n# The business transaction DSL\n\n- [Source Code](https://github.com/dry-python/stories)\n- [Issue Tracker](https://github.com/dry-python/stories/issues)\n- [Documentation](https://stories.readthedocs.io/en/latest/)\n- [Discussion](https://gitter.im/dry-python/stories)\n\n## Installation\n\nAll released versions are hosted on the Python Package Index. You can\ninstall this package with following command.\n\n```bash\npip install stories\n```\n\n## Usage\n\n`stories` provide a simple way to define a complex business scenario\nthat include many processing steps.\n\n```pycon\n\n>>> from stories import story, arguments, Success, Failure, Result\n>>> from django_project.models import Category, Profile, Subscription\n\n>>> class Subscribe:\n...\n...     @story\n...     @arguments('category_id', 'profile_id')\n...     def buy(I):\n...\n...         I.find_category\n...         I.find_profile\n...         I.check_balance\n...         I.persist_subscription\n...         I.show_subscription\n...\n...     def find_category(self, ctx):\n...\n...         category = Category.objects.get(pk=ctx.category_id)\n...         return Success(category=category)\n...\n...     def find_profile(self, ctx):\n...\n...         profile = Profile.objects.get(pk=ctx.profile_id)\n...         return Success(profile=profile)\n...\n...     def check_balance(self, ctx):\n...\n...         if ctx.category.cost < ctx.profile.balance:\n...             return Success()\n...         else:\n...             return Failure()\n...\n...     def persist_subscription(self, ctx):\n...\n...         subscription = Subscription(category=ctx.category, profile=ctx.profile)\n...         subscription.save()\n...         return Success(subscription=subscription)\n...\n...     def show_subscription(self, ctx):\n...\n...         return Result(ctx.subscription)\n\n```\n\n```pycon\n\n>>> Subscribe().buy(category_id=1, profile_id=1)\n<Subscription: Subscription object (8)>\n\n```\n\nThis code style allow you clearly separate actual business scenario from\nimplementation details.\n\n## License\n\nStories library is offered under the two clause BSD license.\n",
    'author': 'Artem Malyshev',
    'author_email': 'proofit404@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://dry-python.org/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
}


setup(**setup_kwargs)
