# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vprad',
 'vprad.actions',
 'vprad.auth',
 'vprad.conf',
 'vprad.site',
 'vprad.site.jinja',
 'vprad.views',
 'vprad.views.generic']

package_data = \
{'': ['*'],
 'vprad': ['static/brand/favicon512x512.png',
           'static/brand/favicon512x512.png',
           'static/brand/favicon512x512.png',
           'static/brand/logo_dark_bg.png',
           'static/brand/logo_dark_bg.png',
           'static/brand/logo_dark_bg.png',
           'static/brand/logo_light_bg.png',
           'static/brand/logo_light_bg.png',
           'static/brand/logo_light_bg.png',
           'static/vprad/*',
           'templates_old/vprad/*',
           'templates_old/vprad/layouts/*',
           'templates_old/vprad/partials/*',
           'templates_old/vprad/render_partials/*',
           'templates_old/vprad/templatetags/*'],
 'vprad.actions': ['jinja2/vprad/actions/*'],
 'vprad.site': ['jinja2/vprad/*',
                'jinja2/vprad/layout/*',
                'jinja2/vprad/macros/*',
                'jinja2/vprad/views/*'],
 'vprad.views': ['jinja2/vprad/views/detail/*', 'jinja2/vprad/views/list/*']}

install_requires = \
['Jinja2>=2.11.1,<3.0.0',
 'attrs>=19.3.0,<20.0.0',
 'bleach>=3.1.0,<4.0.0',
 'django-allauth>=0.41.0,<0.42.0',
 'django-braces>=1.14.0,<2.0.0',
 'django-environ>=0.4.5,<0.5.0',
 'django-filter>=2.2.0,<3.0.0',
 'django-model-utils>=4.0.0,<5.0.0',
 'django-select2>=7.2.0,<8.0.0',
 'django-tables2>=2.2.1,<3.0.0',
 'django>=3.0.3,<4.0.0']

setup_kwargs = {
    'name': 'vprad',
    'version': '0.1.0',
    'description': 'Very Pythonic Rapid Application Development',
    'long_description': 'Very Pythonic Rapid Application Development\n===========================================\n\nThis Django package allows you to rapidly build applications with minimal\neffort on the frontend side.\n\nIt is mainly targeted at Line-Of-Bussiness applications, backend, etc.\n\nIt borrows ideas from Lino, Apache Isis, Cuba Platform and some others.\n\n**Documentation is forthcoming.**\n\nIn the meantime you might take a look at the demo_project folder:\n\n- See the settings,\n- See the partners/actions.py\n- See the contacts/views.py\n\n',
    'author': 'Marc Fargas',
    'author_email': 'telenieko@telenieko.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/telenieko/vprad',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
