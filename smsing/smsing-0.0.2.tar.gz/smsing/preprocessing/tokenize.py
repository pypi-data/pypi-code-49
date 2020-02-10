from typing import List

import nltk
from nltk.tokenize import TweetTokenizer


def tokenize(text: str) -> List[str]:
    return nltk.word_tokenize(text)


def wordpunct_tokenize(text: str) -> List[str]:
    return nltk.wordpunct_tokenize(text)


def tweet_tokenize(text: str) -> List[str]:
    return TweetTokenizer().tokenize(text)
