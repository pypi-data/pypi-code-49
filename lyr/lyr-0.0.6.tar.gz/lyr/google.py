import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}


def lyrics(query):
    query = quote_plus(query)
    search_url = 'https://www.google.com/search?q={}'.format(query)
    res = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    el = soup.find('g-expandable-content', {'data-eb': '0'})
    if not el:
        return
    els = el.find_all('span', {'jsname': 'YS01Ge'})
    lines = []
    for el in els:
        lines.append(el.get_text())
    lyrics = '\n'.join(lines)
    return lyrics