# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pelican', 'pelican.plugins.jinja2content']

package_data = \
{'': ['*']}

install_requires = \
['pelican>=4.2,<5.0']

extras_require = \
{'markdown': ['markdown>=3.1.1,<4.0.0']}

setup_kwargs = {
    'name': 'pelican-jinja2content',
    'version': '1.0.0',
    'description': 'Pelican plugin for using Jinja template code within post content',
    'long_description': '# Jinja2Content Plugin for Pelican\n\n[![Build Status](https://img.shields.io/github/workflow/status/pelican-plugins/jinja2content/build)](https://github.com/pelican-plugins/jinja2content/actions) [![PyPI Version](https://img.shields.io/pypi/v/pelican-jinja2content)](https://pypi.org/project/pelican-jinja2content/)\n\nThis plugin allows the use of Jinja2 directives inside your Pelican articles and pages.\n\nIn this approach, your content is *first* rendered by the Jinja template engine. The result is then passed to the normal Pelican reader as usual. There are two consequences for usage. First, this means the Pelican context and Jinja variables [usually visible](http://docs.getpelican.com/en/stable/themes.html#templates-and-variables) to your article or page template are _not_ available at rendering time. Second, it means that if any of your input content could be parsed as Jinja directives, they will be rendered as such. This is unlikely to happen accidentally, but it’s good to be aware of.\n\nAll input that needs Pelican variables such as `article`, `category`, etc., should be put inside your *theme’s* templating. As such, the main use of this plugin is to automatically generate parts of your articles or pages.\n\nMarkdown, reStructured Text, and HTML input are all supported. Note that by enabling this plugin, all input files of these file types will be pre-processed with the Jinja renderer. It is not currently supported to selectively enable or disable `jinja2content` for only some of these input sources.\n\n\nExample\n-------\n\nOne usage is to embed repetitive HTML in Markdown articles. Since Markdown doesn’t allow customization of layout, if anything more sophisticated than just displaying an image is necessary, one is forced to embed HTML in Markdown articles (i.e. hard-code `<div>` tags and then select them from the theme’s CSS). However, with `jinja2content`, one can do the following:\n\nFile `my-cool-article.md`\n```\n# My cool title\n\nMy cool content.\n\n{% from \'img_desc.html\' import img_desc %}\n{{ img_desc("/images/my-cool-image.png",\n    "This is a cool tooltip",\n    "This is a very cool image.") }}\n```\n\nWhere file `img_desc.html` contains:\n```\n{% macro img_desc(src, title=\'\', desc=\'\') -%}\n<div class="img-desc">\n  <p><img src="{{ src }}" title="{{ title }}"></p>\n  {% if desc %}\n  <p><em>{{ desc }}</em></p>\n  {% endif %}\n</div>\n{%- endmacro %}\n```\n\nThe result will be:\n```\n# My cool title\n\nMy cool content.\n\n<div class="img-desc">\n  <p><img src="/images/my-cool-image.png" title="This is a cool tooltip"></p>\n  <p><em>This is a very cool image.</em></p>\n</div>\n```\n\nAfter this, the Markdown will be rendered into HTML and only then the theme’s templates will be applied.\n\nIn this way, Markdown articles have more control over the content that is passed to the theme’s `article.html` template, without the need to pollute the Markdown with HTML. Another added benefit is that now `img_desc` is reusable across articles.\n\nNote that templates rendered with `jinja2content` can contain Markdown as well as HTML, since they are added before the Markdown content is converted to HTML.\n\n\nInstallation\n------------\n\nThis plugin can be installed via:\n\n    pip install pelican-jinja2content\n\n\nConfiguration\n-------------\n\nThis plugin accepts the setting `JINJA2CONTENT_TEMPLATES` which should be set to a list of paths relative to `PATH` (the main content directory, usually `"content"`). `jinja2content` will look for templates inside these directories, in order. If they are not found in any, the theme’s templates folder is used.\n\n\nExtending\n---------\n\nThis plugin is structured such that it should be quite easy to extend readers for other file types to also render Jinja template logic. It should be sufficient to create a new reader class that inherits from the `JinjaContentMixin` and then your desired reader class. See class definitions in the source for examples.\n\n\nContributing\n------------\n\nContributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].\n\nTo start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.\n\n\nAcknowledgements\n----------------\n\n- Original implementation by @joachimneu and re-worked by @Leonardo.\n- Updated to support reST and HTML input by @micahjsmith.\n- Converted to new plugin format by @justinmayer.\n- Replaces [pelican-jinj2content](https://github.com/joachimneu/pelican-jinja2content/tree/f73ef9b1ef1ee1f56c80757b4190b53f8cd607d1), which had become unmaintained.\n\n\n[existing issues]: https://github.com/pelican-plugins/jinja2content/issues\n[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html\n',
    'author': 'Pelican Dev Team',
    'author_email': 'authors@getpelican.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/pelican-plugins/jinja2content',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
