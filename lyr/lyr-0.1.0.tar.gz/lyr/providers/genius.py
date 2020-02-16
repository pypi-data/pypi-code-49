import requests
from urllib.parse import quote_plus

headers = {
    'Host': 'api.genius.com',
    'Accept': '*/*',
    'Content-Type': 'application/json',
    'X-Genius-iOS-Version': '6.0.6',
    'User-Agent': 'Genius/825 CFNetwork/1121.2.2 Darwin/19.2.0',
}


def lyrics(query):
    search_resp = _search_multi(query)
    song_id = _song_from_search(search_resp)
    song_resp = _songs(song_id)
    return _clean_lyrics(_lyrics_from_song(song_resp))


def _search_multi(query, per_page='3'):
    params = (
        ('q', query),
        ('per_page', per_page),
    )
    response = requests.get('https://api.genius.com/search/multi',
                            headers=headers,
                            params=params)
    return response.json()


def _songs(song_id, text_format='plain'):
    params = (('text_format', text_format), )
    response = requests.get('https://api.genius.com/songs/{}'.format(song_id),
                            headers=headers,
                            params=params)
    return response.json()


def _song_from_search(result):
    for section in result['response']['sections']:
        if section['type'] != 'top_hit':
            continue
        for hit in section['hits']:
            if hit['type'] != 'song':
                continue
            return hit['result']['id']


def _lyrics_from_song(result):
    return result['response']['song']['lyrics']['plain']


def _clean_lyrics(lyrics):
    lines = []
    for line in lyrics.split('\n'):
        line = line.strip()
        if line.startswith('[') and line.endswith(']'):
            continue
        if line.startswith('{') and line.endswith('}'):
            continue
        if line == '':
            continue
        lines.append(line)
    return '\n'.join(lines)