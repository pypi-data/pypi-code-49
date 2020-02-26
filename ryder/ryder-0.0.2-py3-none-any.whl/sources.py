from .clean import correct_url, simple_filter
from .utils import get_source, get_stop_urls, request


def get_urls(root, url):
    stop_urls = get_stop_urls()
    source = get_source(url)
    protocol = "https:" if "https:" in url else "http:"

    # get all urls
    urls = root.xpath("//a/@href")
    urls = [correct_url(source, protocol, x) for x in urls]

    # get their sources
    sources = [get_source(x) for x in urls]

    # filters
    filters = [simple_filter(source, x, stop_urls) for x in urls]

    # check
    data = []
    for i in range(len(urls)):
        if filters[i]:
            data.append({
                "url": urls[i],
                "source": sources[i]
            })
    return data


def build(url):
    html, root = request(url)
    return get_urls(root, url)
