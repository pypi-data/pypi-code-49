# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wagtail_contact_reply', 'wagtail_contact_reply.migrations']

package_data = \
{'': ['*'], 'wagtail_contact_reply': ['templates/wagtailforms/*']}

install_requires = \
['wagtail>=2.6']

setup_kwargs = {
    'name': 'wagtail-contact-reply',
    'version': '0.1.0',
    'description': 'Reply to contact form submissions directly from Wagtail',
    'long_description': "# Wagtail Contact Reply\n\n> Reply to contact form submissions directly from the Wagtail admin\n\n![Preview](misc/direct-reply-feature.gif)\n\n### Installation\n\n```\npip install wagtail-contact-reply\n```\n\n```python\nINSTALLED_APPS = [\n    # ....\n    'wagtail_contact_reply',  # Must be before wagtail.contrib.forms\n    'wagtail.contrib.forms',\n    # ...\n]\n```\n\n### Contributing\nI'm always open to PR's to improve this code and I'm not too picky about how it gets done. If you can make a contribution, I invite you to open a pull request (or an issue).\n\n### Todos\nThings I want to do with this package but may or may not get the time to do...\n\n- [ ] Save replies to each contact submission\n- [ ] View replies from each contact submission\n- [ ] Allow BCC emails\n- [ ] Optionally email all other admins\n- [ ] Add a hook after the reply email is sent\n- [ ] Create default settings to fallback on\n- [ ] Add JavaScript form validation (ie. If the form is trying to be submitted but is missing a required field, show an alert box above the button)\n- [ ] A few standard tests for at least _some_ coverage\n\n### Contibutors\n- [x] Kalob Taulien\n- [ ] _Your name soon?_\n",
    'author': 'Kalob Taulien',
    'author_email': 'kalob.taulien@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/KalobTaulien/wagtail-contact-reply',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<=3.8',
}


setup(**setup_kwargs)
