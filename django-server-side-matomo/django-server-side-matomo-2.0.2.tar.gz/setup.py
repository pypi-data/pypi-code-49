# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['server_side_matomo']

package_data = \
{'': ['*']}

install_requires = \
['Django>=1.11',
 'celery[redis]>=4.1.0',
 'django-ipware>=2.1.0',
 'piwikapi>=0.3']

setup_kwargs = {
    'name': 'django-server-side-matomo',
    'version': '2.0.2',
    'description': 'Send analytics data to Matomo using celery',
    'long_description': "Let your Django app perform server side analytics with Matomo. Server side analytics is a great way to get some analytics while respecting user privacy (only you see the data, no internet wide tracking) and performance (no js tracker needed!)\n\n# Quickstart\n\nYou'll need to have celery set up because making the Matomo request in your Django request would be really slow. This project will collect some data from a request using middleware, serialize it, and send it to celery. Works fine with the default celery json serializer. Running celery will not be described here.\n\n1. Install via pip `django-server-side-matomo`\n2. Add to INSTALLED_APPS `'server_side_matomo',`\n3. Add to MIDDLEWARE `'server_side_matomo.middleware.MatomoMiddleware'`\n4. Set the following in settings.py\n\n- MATOMO_SITE_ID = '1'  # Your site's Matomo ID\n- MATOMO_API_URL = 'https://your.site.com/piwik.php'\n- MATOMO_TOKEN_AUTH = 'your auth token'\n- MATOMO_TRACK_USER_ID = False  # Set to True to track user ID. See https://matomo.org/docs/user-id/\n\n# Testing and Development\n\nOnly merge requests with unit tests will be accepted. Please open an issue first if you'd like to propose a feature. I don't plan to add many features to this project myself. Unless other people are interested in doing the work - I have no plans to support things like Google Analytics.\n\n## Testing\n\nA Docker Compose file is provided to quickly try out the project. Just run in a web container:\n\n`./manage.py test`\n\nTested with Django 3.0 and Python 3.7.\n",
    'author': 'David Burke',
    'author_email': 'david@burkesoftware.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/burke-software/django-server-side-matomo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
