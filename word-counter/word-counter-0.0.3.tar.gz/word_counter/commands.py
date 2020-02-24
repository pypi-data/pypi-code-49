#!/usr/bin/env python
import collections
import json

import click
import requests
from bs4 import BeautifulSoup
from polyglot.text import Text, WordList


def get(urls: tuple, klass: str = 'entry-content') -> list:
    wlist = []
    for url in urls:
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.find(class_=klass).get_text()
        words = Text(text).words
        for word in words:
            wlist.append(word)
    return wlist


def get_common_most(words: list) -> dict:
    common_words = collections.Counter(words).most_common()
    dic = {}
    for word in common_words:
        dic.update({word[0]: word[1]})
    return dic


@click.command()
@click.argument('urls', required=True, nargs=-1)
@click.option('--klass', '-k', required=False, default='entry-content')
def word_counter(
    urls: str,
    klass: str,
) -> None:
    """
    Count the number of words on the specified URL(s).

    Required arguments:

        - urls
            Specify the target URL for counting words.
            It is possible to specify multiple URLs.

    Optional arguments:

        - klass
            Specify the HTML class name that counts the number of words.
            Default is 'entry-content'.
    """
    wlist = get(urls=urls, klass=klass)
    count = len(list(set(wlist)))
    count_duplicates = len(wlist)
    wdic = get_common_most(words=wlist)

    dic = dict()
    dic.update(
        count=count,
        count_duplicates=count_duplicates,
        words=wdic,
    )
    click.echo(json.dumps(dic, indent=2, ensure_ascii=False, sort_keys=False))
