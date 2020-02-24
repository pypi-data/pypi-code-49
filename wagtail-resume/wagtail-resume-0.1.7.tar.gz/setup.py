# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['wagtail_resume', 'wagtail_resume.migrations', 'wagtail_resume.templatetags']

package_data = \
{'': ['*'],
 'wagtail_resume': ['static/wagtail_resume/css/*',
                    'static/wagtail_resume/images/*',
                    'static/wagtail_resume/js/*',
                    'templates/wagtail_resume/*',
                    'templates/wagtail_resume/blocks/*']}

install_requires = \
['Django>=2.2.2',
 'wagtail-markdown>=0.5',
 'wagtail-metadata>=3.0.0',
 'wagtail>=2.7']

setup_kwargs = {
    'name': 'wagtail-resume',
    'version': '0.1.7',
    'description': 'A Wagtail project made to simplify creation of resumes for developers.',
    'long_description': '# Wagtail resume\n\n![Lint](https://github.com/adinhodovic/wagtail-resume/workflows/Test/badge.svg)\n![Test](https://github.com/adinhodovic/wagtail-resume/workflows/Lint/badge.svg)\n[![Coverage](https://codecov.io/gh/adinhodovic/wagtail-resume/branch/master/graphs/badge.svg)](https://codecov.io/gh/adinhodovic/wagtail-resume/branch/master)\n[![Supported Python versions](https://img.shields.io/pypi/pyversions/wagtail-resume.svg)](https://pypi.org/project/wagtail-resume/)\n[![PyPI Version](https://img.shields.io/pypi/v/wagtail-resume.svg?style=flat)](https://pypi.org/project/wagtail-resume/)\n\nWagtail-resume is a reusable Wagtail page model designed to make the creation of a good resume easy and quick. Additionally, it will be fully integrated into your site/blog.\n\n## Preview\n\n![Resume Preview](https://i.imgur.com/b0TxeGe.png)\n\nThe full resume example is [live and accesible here.](https://hodovi.cc/wagtail-resume-sample)\n\n## Dependencies\n\n- Wagtail-metadata\n    - It uses wagtail-metadata for all meta & SEO fields.\n- Wagtail-markdown\n\n## Installation\n\nInstall wagtail-resume with pip:\n\n`pip install wagtail-resume`\n\nAdd the application to installed Django applications:\n\n```py\nINSTALLED_APPS = [\n    ...\n    "wagtail_resume",\n    ...\n]\n```\n\nRun the migrations.\n\n## Getting started\n\nImport and extend the BaseResumePage:\n\n```python\nfrom wagtail_resume.models import BaseResumePage\n\n\nclass ResumePage(BaseResumePage):\n    pass\n```\n\nHead over to the Wagtail admin and create your resume!\n\n## Default Fields\n\nDefault resume fields:\n\n- Role\n- Profile picture\n- Social links\n- About\n- Work Experience\n- Contributions (Opensource/projects)\n- Writing (internal Wagtail pages or external URLs)\n- Education (Degrees/Courses/Certificates)\n\n## Customization\n\nWagtail-resume currently supports 4 customizations:\n\n- Heading for a section\n- Icon for a section (Fontawesome)\n- Font style\n- Background color\n\nThe background-color should be specified in hex (e.g #FFFFFF) or [css supported colors](https://www.w3schools.com/cssref/css_colors.asp) and the font should be available on Google fonts. The fonts supported are only the ones from [Google Fonts](https://fonts.google.com/) so make sure to check what fonts are available.\n',
    'author': 'Adin Hodovic',
    'author_email': 'hodovicadin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/adinhodovic/wagtail-resume',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
