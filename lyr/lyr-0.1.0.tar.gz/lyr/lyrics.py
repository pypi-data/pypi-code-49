from lyr.providers import google, musixmatch, genius

providers = [google, musixmatch, genius]


def lyrics(query):
    for provider in providers:
        try:
            lyrics = provider.lyrics(query)
            if lyrics:
                return lyrics
        except:
            continue
