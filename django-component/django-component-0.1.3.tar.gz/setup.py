# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['django_component']

package_data = \
{'': ['*']}

install_requires = \
['django>=1.11']

setup_kwargs = {
    'name': 'django-component',
    'version': '0.1.3',
    'description': 'Django template tags to create composable components',
    'long_description': 'django-component\n#################\n\n**Modern components for django templates**\nDeclarative and composable components inspired by javascript frameworks.\n\nSupports Python **3.6+** and Django **1.11**, **2.0+**, and **3.0+**\n\nUsage\n=====\n\nDescribe your component:\n\n.. code-block:: python\n\n    # myapp/templatetags/mycomponents.py\n\n    from django_component import Library, Component\n\n    register = Library()\n\n    @register.component\n    class Card(Component):\n        template = "myapp/card.html"\n\n        class Media:\n            css = {"all": ["myapp/card.css"]}\n            js = ["myapp/card.js"]\n        \n\n.. code-block:: html\n\n    # myapp/templates/myapp/card.html\n\n    <section class="card">\n        <header>{{ header }}</header>\n        <h1>{{ short_title }}</h1>\n        <div>{{ children }}</div>\n    </section>\n\nAnd use them in your templates\n\n.. code-block:: html\n\n    {% load mycomponents %}\n    {% components_css %}\n\n    {% Card title="My card\'s title" %}\n        This will be accessible as the `children` variable.\n        It\'s just django template, <span>{{ variable }}</span> !\n\n        {% slot header %}\n            This <img src="foo.jpg" />\n            will be in the header of the card\n        {% endslot %}\n    {% /Card %}\n\n    {% components_js %}\n\n``django-component`` also enable context processing per component, see the documentation (TODO) for the complete api.\n\nWhy django-component?\n======================\n\n``django-component`` make it easy to create reusable template components.\nDjango has some features to address this, but they all come with some limitations.\n``django-component`` unify these features (``block``, ``includes``, ``inclusion_tag``, ``simple_tag``) under an unique api.\nIn addition ``django-component`` address one of my greatest frustration with reusable components in django: **tracking css and js dependencies** for each component and **include them only when they are effectively used**.\n\n\nInstallation\n============\n\n.. code-block:: sh\n\n    pip install django-component\n\nThen add ``django-component`` to your INSTALLED_APPS,\nit is also recommended to add django-component.templatetags as builtins templatetags\n\n.. code-block:: python\n\n    INSTALLED_APPS = [\n        ...,\n        "django_component",\n        ...\n    ]\n\n\n    TEMPLATES=[\n        {\n            \'OPTIONS\': {\n                \'builtins\': [\n                    \'django_component.templatetags\',\n                ]\n            },\n        }\n    ],\n',
    'author': 'Jérôme Bon',
    'author_email': 'bon.jerome@protonmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.com/Mojeer/django_components',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
