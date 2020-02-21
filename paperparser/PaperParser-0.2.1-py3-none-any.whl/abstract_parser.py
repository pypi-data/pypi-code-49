"""Strategies for parsing abstracts."""
from typing import Callable

from pyquery import PyQuery as pq  # type: ignore
import requests

ABSTRACT_PLUGINS = dict()


def abstract_plugin(func: Callable) -> Callable:
    """Register a function as a abstract plug-in."""
    ABSTRACT_PLUGINS[func.__name__] = func
    return func


def abstract(strategy: str, url: str) -> str:
    """Get abstract for given strategy."""
    return ABSTRACT_PLUGINS[strategy](url)


@abstract_plugin
def arxiv(url: str) -> str:
    """Parse arxiv abstract."""
    page = requests.get(url)
    d = pq(page.content)
    return d("#abs > blockquote").text()


@abstract_plugin
def nips(url: str) -> str:
    """Parse nips abstract."""
    page = requests.get(url)
    d = pq(page.content)
    return d("p.abstract").text()


@abstract_plugin
def acm(url: str) -> str:
    """Parse acm abstract."""
    page = requests.get(url)
    d = pq(page.content)
    return d("div.abstractSection").text()
