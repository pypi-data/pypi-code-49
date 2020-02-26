import os
from urllib.parse import (
    urlencode, urlparse, parse_qs, urlunparse)


def remove_campaign_from_url(url):
    # from : https://stackoverflow.com/questions/   \
    # 11640353/remove-utm-parameters-from-url-in-python
    parsed = urlparse(url)
    qd = parse_qs(parsed.query, keep_blank_values=True)
    filtered = dict((k, v) for k, v in qd.items() if not k.startswith('utm_'))
    newurl = urlunparse([
        parsed.scheme,
        parsed.netloc,
        parsed.path,
        parsed.params,
        urlencode(filtered, doseq=True), # query string
        parsed.fragment
    ])
    return newurl


def simple_filter(source, url, stop_urls):
    if len(url) == 0:
        return False
    if url[0] == "#":
        # if anchor, remove url
        return False
    if url == "/":
        # if home, return url
        return False
    
    if any((x in url for x in stop_urls)):
        # if url in stop_urls
        return False

    if len(source) + 16 >= len(url):
        return False
    return True


def correct_url(source, protocol, url):
    url = url.strip()
    if url[:2] == "//":
        return protocol + url
    elif url[:1] == "/":
        return source + url
    return url


def clean_str(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res is None:
            return res
        if "Ã©" in res or "Ã¨" in res:
            try:
                return res.encode("latin-1").decode("utf8", "ignore").strip()
            except UnicodeDecodeError:
                return res.strip()
        return res.strip()
    return wrapper
