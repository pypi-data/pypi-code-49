"""Strategies for parsing bibtex."""
from typing import Callable
from urllib.parse import urljoin

from pyquery import PyQuery as pq  # type: ignore
import requests

BIBTEX_PLUGINS = dict()


def bibtex_plugin(func: Callable) -> Callable:
    """Register a function as a bibtex plug-in."""
    BIBTEX_PLUGINS[func.__name__] = func
    return func


def bibtex(strategy: str, url: str) -> str:
    """Get bibtex for given strategy."""
    return BIBTEX_PLUGINS[strategy](url)


@bibtex_plugin
def arxiv(url: str) -> str:
    """Get bibtex for arxiv papers."""
    page = requests.get(url)
    d = pq(page.content)
    arxiv_ids = d('meta[name="citation_arxiv_id"]')
    arxiv_id = arxiv_ids[0].attrib["content"]
    id = arxiv_id.replace(".", "-")
    bib_page_url = "https://dblp.uni-trier.de/rec/bib1/journals/corr/abs-" + id + ".bib"
    page = requests.get(bib_page_url)
    return page.content.decode("utf-8")


@bibtex_plugin
def nips(url: str) -> str:
    """Get bibtex for nips papers."""
    page = requests.get(url)
    d = pq(page.content)
    el = d('a:Contains("BibTeX")')
    bib_page_url = urljoin(url, el.attr["href"])
    page = requests.get(bib_page_url)
    return page.content.decode("utf-8")


@bibtex_plugin
def doi(url: str) -> str:
    """Get bibtex for doi papers."""
    bib_page_url = "https://scipython.com/apps/doi2bib/?doi=" + url
    page = requests.get(bib_page_url)
    d = pq(page.content)
    return d("#bibtex-box").text()


@bibtex_plugin
def acm(url: str) -> str:
    """Get bibtex for acm papers."""
    parts = url.split("/")
    return doi(parts[-2] + "/" + parts[-1])
