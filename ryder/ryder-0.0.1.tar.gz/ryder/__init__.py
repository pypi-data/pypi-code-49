from .sources import build
from .articles import read


def article(url):
    return read(url)


def source(url):
    return build(url)