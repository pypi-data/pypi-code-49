import re


def get_download_url(url):
    if "deckstats.net/decks/" in url:
        return url + "?include_comments=0&export_txt=1"
    if "tappedout.net/mtg-decks/" in url:
        return url + "?fmt=txt"
    if "pastebin.com/raw/" in url:
        return url
    if "deckbox.org/sets/" in url:
        return url + "/export"
    if "scryfall.com/" in url and "deck" in url:
        uuid = re.findall(r"[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}", url)[0]
        return "https://api.scryfall.com/decks/%s/export/text" % uuid
    if "mtggoldfish.com/deck/" in url:
        deckId = ''.join([ii for ii in url if ii.isdigit()]).strip()
        return "https://www.mtggoldfish.com/deck/download/" + deckId
