#!/usr/bin/env python
import collections
import json
import logging

import click
import requests
from bs4 import BeautifulSoup
from polyglot.text import Text, WordList


def get_logger() -> logging.Logger:
    logging.basicConfig(
        format="[%(asctime)s] %(message)s",
        level=logging.INFO,
        datefmt="%d-%b-%y %H:%M:%S",
    )
    logger = logging.getLogger("count-words")
    logger.setLevel(logging.INFO)
    return logger


def get_words(urls: tuple, klass: str = 'entry-content') -> list:
    wlist = []
    for url in urls:
        html = requests.get(url).content
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.find(class_=klass).get_text()
        words = Text(text).words
        for word in words:
            wlist.append(word)
    return wlist


def count_words(urls: tuple, klass: str = 'entry-content') -> int:
    return len(get_words(urls=urls, klass=klass))


def _ranking(words: list) -> dict:
    common_words = collections.Counter(words).most_common()
    dic = {}
    for word in common_words:
        dic.update({word[0]: word[1]})
    return dic


def get_words_ranking(urls: tuple, klass: str = 'entry-content') -> dict:
    words = get_words(urls=urls, klass=klass)
    return _ranking(words)


@click.command()
@click.argument('urls', required=True, nargs=-1)
@click.option('--klass', '-k', required=False, default='entry-content')
@click.option('--count-only', '-c', is_flag=True, default=False)
@click.option('--one-line', '-o', is_flag=True, default=False)
@click.option('--quiet', '-w', is_flag=True, default=False)
@click.option('--sort', '-s', is_flag=True, default=False)
def word_counter(
    urls: str,
    klass: str,
    count_only: bool = False,
    one_line: bool = False,
    quiet: bool = False,
    sort: bool = False
) -> None:  # noqa 501
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

    Optional flags:

        - --count-only
            Count the types of words.

        - --one-line
            Specify when you want to output the result in one line.

        - --quiet
            Disable logging.

        - --sort
            Specify when you want to sort the JSON output results.
    """
    logger = get_logger()
    if(quiet):
        logging.disable(logging.FATAL)
    if(count_only):
        click.echo(count_words(urls=urls, klass=klass))
        return True

    words = get_words(urls=urls, klass=klass)
    if(one_line):
        click.echo(words)
    _list = _ranking(words)
    click.echo(json.dumps(_list, indent=2, ensure_ascii=False, sort_keys=sort))
