# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['canonicalwebteam', 'canonicalwebteam.blog']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=1.0,<2.0', 'feedgen>=0.8,<0.9', 'requests>=2.22,<3.0']

setup_kwargs = {
    'name': 'canonicalwebteam.blog',
    'version': '5.0.0',
    'description': 'Flask extension to add a nice blog to your website',
    'long_description': '# Canonical blog extension\n\nThis extension allows you to add a simple frontend section to your flask app. All the articles\nare pulled from [Canonical\'s Wordpress back-end](https://admin.insights.ubuntu.com/wp-admin/) through the JSON API.\n\nThis extension provides a blueprint with 3 routes:\n\n- "/": that returns the list of articles\n- "/<slug>": the article page\n- "/feed": provides a RSS feed for the page.\n\n## How to install\n\nTo install this extension as a requirement in your project, you can use PIP;\n\n```bash\npip install canonicalwebteam.blog\n```\n\nSee also the documentation for (pip install)[https://pip.pypa.io/en/stable/reference/pip_install/].\n\n## How to use\n\n### Templates\n\nThe module expects HTML templates at `blog/index.html`, `blog/article.html`, `blog/blog-card.html`, `blog/archives.html`, `blog/upcoming.html` and `blog/author.html`.\n\nAn example of these templates can be found at https://github.com/canonical-websites/jp.ubuntu.com/tree/master/templates/blog.\n\n### Flask\n\nIn your app you can then:\n\n``` python3\n    import flask\n    from canonicalwebteam.blog import BlogViews\n    from canonicalwebteam.blog.flask import build_blueprint\n\n    app = flask.Flask(__name__)\n\n    # ...\n\n    blog_views = BlogViews()\n    app.register_blueprint(build_blueprint(blog_views), url_prefix="/blog")\n```\n\nYou can customise the blog through the following optional arguments:\n\n``` python3\n    blog_views = BlogViews(\n        blog_title="Blog",\n        tag_ids=[1, 12, 112],\n        exclude_tags=[26, 34],\n        feed_description="The Ubuntu Blog Feed",\n        per_page=12, # OPTIONAL (defaults to 12)\n    )\n    app.register_blueprint(build_blueprint(blog_views), url_prefix="/blog")\n```\n\n## Development\n\nThe blog extension leverages [poetry](https://poetry.eustace.io/) for dependency management.\n\n### Regenerate setup.py\n\n``` bash\npoetry install\npoetry run poetry-setup\n```\n\n## Testing\n\nAll tests can be run with `poetry run pytest`.\n\n### Regenerating Fixtures\n\nAll API calls are caught with [VCR](https://vcrpy.readthedocs.io/en/latest/) and saved as fixtures in the `fixtures` directory. If the API updates, all fixtures can easily be updated by just removing the `fixtures` directory and rerunning the tests.\n\nTo do this run `rm -rf fixtures && poetry run pytest`.\n',
    'author': 'Canonical webteam',
    'author_email': 'webteam@canonical.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
