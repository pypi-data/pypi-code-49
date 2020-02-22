import re

import requests
from bs4 import BeautifulSoup

def get_search_results(keywords, n=10):
    if not isinstance(keywords, str):
        keywords = ' '.join(keywords)
    
    params = {
        'search_query': keywords
    }
    
    url = "https://youtube.com/results"
    r = requests.get(url, params=params)
    soup = BeautifulSoup(r.content, 'html.parser')
    regex = re.compile(r'/watch\?v=(?P<content_id>.+)')
    ret = []
    for link in soup('a', href=regex, class_='yt-uix-tile-link'):
        title = link.text.strip()
        href = link['href']
        m = regex.search(href).group
        content_id = m('content_id')
        row = dict(
            title=title,
            link="https://youtu.be/{}".format(content_id)
        )
        ret.append(row)
    return ret[:n]
