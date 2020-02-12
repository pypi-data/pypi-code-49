# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jetblack_markdown', 'jetblack_markdown.metadata']

package_data = \
{'': ['*'], 'jetblack_markdown': ['templates/*']}

install_requires = \
['docstring-parser>=0.6,<0.7', 'markdown>=3.1,<4.0']

setup_kwargs = {
    'name': 'jetblack-markdown',
    'version': '0.4.0',
    'description': 'A markdown extension for python documentation',
    'long_description': '# jetblack-markdown\n\nMarkdown extensions for automatic document generation\n(read the [docs](https://rob-blackbourn.github.io/jetblack-markdown/)).\n\n## Markdown Extension\n\nA markdown extension is provided for automatically documenting python code.\n\nModules are referred to as follows:\n\n```markdown\n# A Top Level Module\n\n@[jetblack_markdown]\n\n# A Package\n\n@[jetblack_markdown.autodoc]\n\n# A function\n\n@[jetblack_markdown.autodoc:makeExtension]\n\n# A class\n\n@[jetblack_markdown.autodoc.metadata:PropertyDescriptor]\n```\n\n## mkdocs integration\n\nThis site was generated using `mkdocs` and the following config:\n\n```yaml\nsite_name: jetblack-markdown\n\ndocs_dir: documentation\nsite_dir: docs\n\nmarkdown_extensions:\n  - admonition\n  - codehilite\n  - jetblack_markdown.autodoc:\n      class_from_init: true\n      ignore_dunder: true\n      ignore_private: true\n      ignore_all: false\n      prefer_docstring: true\n      template_folder: null\n\nextra_css:\n    - css/custom.css\n```\n\n### Configuration\n\nThere are some configuration parameters.\n\n* class_from_init (bool, optional): If True use the docstring from\n    the &#95;&#95;init&#95;&#95; function for classes. Defaults to\n    True.\n* ignore_dunder (bool, optional): If True ignore\n    &#95;&#95;XXX&#95;&#95; functions. Defaults to True.\n* ignore_private (bool, optional): If True ignore methods\n    (those prefixed &#95;XXX). Defaults to True.\n* ignore_all (bool): If True ignore the &#95;&#95;all&#95;&#95; member.\n* prefer_docstring (bool): If true prefer the docstring.\n* template_folder(Optional[str], optional): Specify a custom template folder.\n    The template "main.jinja2" will be rendered passing an `obj` parameter\n    which is a `jetblack.markdown.metadata.Descriptor`\n\n## Customizing\n\nAll the rendering is done with jinja2 templates. Start by copying the current\ntemplates from jetblack_markdown/templates and specify the `template_folder` in\nthe `mkdocs.yml`.\n\n',
    'author': 'Rob Blackbourn',
    'author_email': 'rob.blackbourn@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rob-blackbourn/jetblack-markdown',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
