from os import linesep
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import googlesearch

domains = ['www.musixmatch.com/lyrics']

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}


def lyrics(query):
    it = googlesearch.search(query, domains=domains)
    url = next(it)
    if not url:
        return
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    els = soup.find_all('span', {'class': 'lyrics__content__ok'})
    if not els or len(els) == 0:
        return
    text = ''
    for el in els:
        text += el.string
    text = linesep.join([s for s in text.splitlines() if s])
    return text
