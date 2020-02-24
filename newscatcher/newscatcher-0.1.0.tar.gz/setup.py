# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['newscatcher']

package_data = \
{'': ['*'], 'newscatcher': ['data/*']}

install_requires = \
['feedparser>=5.2.1,<6.0.0', 'requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'newscatcher',
    'version': '0.1.0',
    'description': 'Get the normalized latest news from (almost) any website',
    'long_description': "# Newscatcher\nProgrammatically collect normalized news from (almost) any website.\nBy [newscatcherapi.com][1].\n\n## Demo\n\n\n## Motivation\nWhile working on newscatcherapi -- JSON API to query the news articles,\nI came up with an idea to make a simple Python package that would allow\nto easily grab the live news data. \n\nWhen I used to be a junior data scientist working on my own side projects,\nit was difficult for me to operate with external data sources. I knew Python\nquite well, but in most cases it was not enough to build proper data pipelines\nthat required gathering data on my own. \n\nEven though I do not recommend to use this package for any production systems, I believe that it should be enough to test your assumptions and build some MVPs.\n\n## Installation\n`pip install newscatcher`\n\n## Tech/framework used\nThe package itself is nothing more than a SQLite database with \nRSS feed endpoints for each website and some basic wrapper of\n[feedparser][2].\n\n## Code Example/Documentation\nLet's review all possible usage of the package. \n\nIn its core, it has a class called *Newscatcher*. This class is all you need in order to get latest news.\n\nAfter installing your package, import the class:\n\n`from newscatcher import Newscatcher`\n \nNow you just need to put a url of a desired news source as an input into our class. \n**Please take the base form url of a website** (without `www.`,neither `https://`, nor `/` at the end of url).\n\nFor example: “nytimes”.com, “news.ycombinator.com” or “theverge.com”.\n\n`news_source = Newscatcher('blackfaldslife.com')`\n\nIf you have done it right and the source that you chose is presented in our database, you will get a variable with 3 components and 1 method:\n\n- `news_source.website` -- the same string that you entered inside the class.\n- `news_source.news` -- a list of a feedparser dictionary with latest news presented on the website. \n- `news_source.headlines` -- a list with latest headlines presented on the website.\n- `news_source.print_headlines()` -- print headlines of all latest articles.\n\nEach element of *news* list is a json object with all relevant and available information regarding an article. If you want to know more about the attributes that you can extract from this json, go check the official documentation of feedparser following this link: [feedparser\\_attributes][3]. You can find everything that begins with *entries[i]*. But be aware that not all the attributes are provided by the news website. \n\nIf for some reason you do not like classes, you can always import 2 main methods and use them separately.\n\n`from newscatcher import get_news`\n`news = get_news('wired.co.uk')`\n\nor\n\n`from newscatcher import get_headlines`\n`news = get_headlines('wired.co.uk')`\n\n\n## Licence\nMIT\n\n\n[1]:\t%3Chttps://newscatcherapi.com/%3E\n[2]:\t%3Chttps://pythonhosted.org/feedparser/index.html%3E\n[3]:\t%3Chttps://pythonhosted.org/feedparser/reference.html%3E\n",
    'author': 'Artem Bugara',
    'author_email': 'bugara.artem@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://www.newscatcherapi.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
