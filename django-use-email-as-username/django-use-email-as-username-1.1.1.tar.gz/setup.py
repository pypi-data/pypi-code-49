# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_use_email_as_username',
 'django_use_email_as_username.management.commands']

package_data = \
{'': ['*'],
 'django_use_email_as_username.management.commands': ['app_template/__init__.py-tpl',
                                                      'app_template/__init__.py-tpl',
                                                      'app_template/__init__.py-tpl',
                                                      'app_template/__init__.py-tpl',
                                                      'app_template/admin.py-tpl',
                                                      'app_template/admin.py-tpl',
                                                      'app_template/admin.py-tpl',
                                                      'app_template/admin.py-tpl',
                                                      'app_template/apps.py-tpl',
                                                      'app_template/apps.py-tpl',
                                                      'app_template/apps.py-tpl',
                                                      'app_template/apps.py-tpl',
                                                      'app_template/migrations/*',
                                                      'app_template/models.py-tpl',
                                                      'app_template/models.py-tpl',
                                                      'app_template/models.py-tpl',
                                                      'app_template/models.py-tpl']}

install_requires = \
['django>=1.11']

extras_require = \
{u'testing': ['coverage>=4.0,<5.0', 'codecov>=2.0.15,<3.0.0']}

setup_kwargs = {
    'name': 'django-use-email-as-username',
    'version': '1.1.1',
    'description': 'A Django app to use email as username for user authentication.',
    'long_description': "============================\nDjango use Email as Username\n============================\n\n.. image:: https://badge.fury.io/py/django-use-email-as-username.svg\n    :target: https://badge.fury.io/py/django-use-email-as-username\n\n.. image:: https://travis-ci.org/jmfederico/django-use-email-as-username.svg?branch=master\n    :target: https://travis-ci.org/jmfederico/django-use-email-as-username\n\n.. image:: https://codecov.io/gh/jmfederico/django-use-email-as-username/branch/master/graph/badge.svg\n    :target: https://codecov.io/gh/jmfederico/django-use-email-as-username\n\n.. image:: https://img.shields.io/badge/code%20style-black-000000.svg\n    :target: https://github.com/ambv/black\n\nA Django app to use email as username for user authentication.\n\n\nFeatures\n--------\n\n* Custom User model with no username field\n* Use email as username\n* Includes a django-admin command for quick install\n* Follow Django `best practices`_ for new Django projects and User models.\n\n.. _`best practices`: https://docs.djangoproject.com/en/dev/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project\n\n\nQuickstart\n----------\n\n1. Install **Django use Email as Username**::\n\n    $ pip install django-use-email-as-username\n\n2. Add it to your *INSTALLED_APPS*::\n\n    INSTALLED_APPS = (\n        ...\n        'django_use_email_as_username.apps.DjangoUseEmailAsUsernameConfig',\n        ...\n    )\n\n3. Create you new django app::\n\n    $ python manage.py create_custom_user_app\n\n4. Add the new app to your *INSTALLED_APPS*::\n\n    INSTALLED_APPS = (\n        ...\n        'django_use_email_as_username.apps.DjangoUseEmailAsUsernameConfig',\n        'custom_user.apps.CustomUserConfig',\n        ...\n    )\n\n5. Now instruct Django to use your new model::\n\n    AUTH_USER_MODEL = 'custom_user.User'\n\n6. Create and run migrations::\n\n    $ python manage.py makemigrations\n    $ python manage.py migrate\n\nYou now have a new Django app which provides a custom User model.\n\nYou can further modify the new User Model any time in the future, just remember\nto create and run the migrations.\n\n\nNotes\n-----\n\nThis app gives you a custom User model, which is `good practice`_ for new\nDjango projects.\n\n`Changing to a custom user model mid-project`_ is not easy.\n\n.. _`good practice`: https://docs.djangoproject.com/en/dev/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project\n.. _`Changing to a custom user model mid-project`: https://docs.djangoproject.com/en/dev/topics/auth/customizing/#changing-to-a-custom-user-model-mid-project\n\nIt is recommended to always create a custom User model at the beginning of every\nDjango project.\n\nCredits\n-------\n\nTools used in rendering this package:\n\n*  Cookiecutter_\n*  `Cookiecutter Django Package`_ by jmfederico_\n\n.. _Cookiecutter: https://github.com/audreyr/cookiecutter\n.. _`Cookiecutter Django Package`: https://github.com/jmfederico/cookiecutter-djangopackage\n.. _jmfederico: https://github.com/jmfederico\n",
    'author': 'Federico Jaramillo Mart\xc3\xadnez',
    'author_email': 'federicojaramillom@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jmfederico/django-use-email-as-username',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
