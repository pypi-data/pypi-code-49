# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sargilo',
 'sargilo.integrations',
 'sargilo.tests',
 'sargilo.tests.blog',
 'sargilo.tests.blog.migrations',
 'sargilo.tests.blog.south_migrations',
 'sargilo.tests.blog.tests',
 'sargilo.tests.django111_test_project',
 'sargilo.tests.django14_test_project',
 'sargilo.tests.django18_test_project',
 'sargilo.tests.django22_test_project',
 'sargilo.tests.django30_test_project']

package_data = \
{'': ['*']}

install_requires = \
['ruamel.yaml', 'typing']

setup_kwargs = {
    'name': 'sargilo',
    'version': '0.1.6',
    'description': '💾 Data loader for Humans',
    'long_description': 'Sargilo \n=======\n\n💾 Data loader for Humans\n\nSargilo lets you declare your data in a visually pleasing and non-frustrating way and loads it into your environment of choice. YAML usage, validation and auto-completion help you get boring jobs done.\n\n💡 Motivation\n-------------\n\nThe idea for this project came from the testing I had to do at work. Surely, you will need sample data to test the project you currently work on. After some time, two ways how to approach this have been emerged:\n\n- Create a minimal and abstract data sample for each test or group of tests and test against those\n- Find a more comphrehensive data set that satisfies most of edge cases and only add to it in rare cases\n\nThere are of course advantages and disadvantages to both approaches. However, I prefer the second approach and think of it as telling a little story. I prefer this way since the dataset can be used as a fixture when running your application and after working on it for quite some time, you will get a feeling for the result a function should produce, making it easier to spot errors.\n\n📦 Install\n----------\n\n```bash\npip install sargilo\n```\n\nOr if you prefer an alternative installation method\n\n```bash\npoetry add sargilo\npipenv install sargilo\n```\n\n🔗 Integrations\n---------------\n\nTo know how to load your data, `sargilo` has to know how to deal with your framework or ORM of choice. While `sargilo` provides the interface and basic functionaly, the specifics on how to load the data are up to the integration. Currently, the following integrations are supported:\n\n- Django (ORM)\n\n📒 Examples\n-----------\n\n```python\n# models.py\nfrom django import models\nfrom django.contrib.auth.models import User\n\n\nclass Tag(models.Model):\n    name = models.CharField(max_length=255, blank=False, null=False)\n\nclass Post(models.Model):\n    title = models.CharField(max_length=255)\n    content = models.TextField()\n\n    tag = models.ForeignKey(\n        Tag,\n        verbose_name=\'Tag\',\n        related_name=\'posts\',\n        on_delete=models.PROTECT\n    )\n\n    author = models.ForeignKey(\n        User,\n        verbose_name=\'Author\',\n        related_name=\'posts\',\n        on_delete=models.PROTECT\n    )\n```\n\n```yaml\n# dataset.yaml\nauth:\n  users:\n    - &Admin\n      username:     "Admin"\n      first_name:   "Christoph"\n      last_name:    "Smaul"\n      email:        "christoph@mail.de"\n      password:     "very_secret"\n      is_staff:      True\n      is_superuser:  True\n    - &Editor\n      username:     "Editor"\n      first_name:   "Wendy"\n      last_name:    "Lator"\n      email:        "wendy@mail.de"\n      password:     "very_secret"\n      is_staff:      True\n      is_superuser:  False\n\n\nblog:\n  tags:\n    - &TestTag\n      name: "Test"\n    - &BlueTag\n      name: "Blue"\n  posts:\n    - title: "Hello world"\n      text: "Lorem ipsum dolor amet sunt"\n      tag: *TestTag\n      author: *Admin\n\n    - title: "Just a test"\n      text: "This is just a test. This is just a test. This is just a test."\n      tag: *TestTag\n      author: *Editor\n```\n',
    'author': 'Nick Lehmann',
    'author_email': 'nick@lehmann.sh',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nick-lehmann/Sargilo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7',
}


setup(**setup_kwargs)
