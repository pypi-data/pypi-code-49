import re
from string import punctuation
from typing import List

from bs4 import BeautifulSoup as Soup
from nltk.corpus import stopwords

import smsing.extraction as ext

PT_EMAIL = re.compile(r"\S+@\S+\.[a-z]{1,3}")
PT_MULTIPLE_SPACES = re.compile(r"\s{2,}")
PT_NUMBERS = re.compile(r"\b[0-9]+\b")


def remove_emails(text: str) -> str:
    return remove_multiple_spaces(re.sub(PT_EMAIL, "", text).strip())


def remove_html_tags(text: str) -> str:
    return Soup(text, "lxml").text


def remove_multiple_spaces(text: str) -> str:
    return re.sub(PT_MULTIPLE_SPACES, " ", text).strip()


def remove_numbers(text: str) -> str:
    return remove_multiple_spaces(re.sub(PT_NUMBERS, "", text).strip())


def remove_people(text: str, model) -> str:
    people = ext.extract_people(text, model)
    return remove_multiple_spaces(
        " ".join([word for word in text.split() if word not in people]).strip()
    )


def remove_punctuation(text: str) -> str:
    return remove_multiple_spaces(
        "".join(
            [
                (c if (c not in punctuation and c not in ["…", "’"]) else " ")
                for c in text
            ]
        )
    )


def remove_single_quotes(text: str) -> str:
    return remove_multiple_spaces(text.replace("'", ""))


def remove_stackoverflow_snippets(text: str, length: int) -> str:
    pattern = r"(<code>).{".join(str(length)).join(r",}?(</code>)")
    text = re.sub(pattern, "", text)
    text = re.sub(r"(<code>)|(</code>)", "", text).strip()
    return remove_multiple_spaces(text)


def remove_stopwords(
    text: str, language: str = "english", custom_stopwords: List[str] = None
) -> str:
    custom_stopwords = custom_stopwords or []
    custom_stopwords = stopwords.words(language) + custom_stopwords
    stopw = map(str.lower, custom_stopwords)
    return remove_multiple_spaces(
        " ".join([word for word in text.split() if word.lower() not in stopw]).strip()
    )


def remove_twitter_hashtags(text: str) -> str:
    for tag in ext.extract_twitter_hashtags(text):
        text = text.replace(f"#{tag}", "")
    return remove_multiple_spaces(text.strip())


def remove_twitter_mentions(text: str) -> str:
    for tag in ext.extract_twitter_mentions(text):
        text = text.replace(f"@{tag}", "")

    return remove_multiple_spaces(text.strip())


def remove_urls(text: str) -> str:
    urls = ext.extract_urls(text)
    return remove_multiple_spaces(
        " ".join([word for word in text.split() if word not in urls]).strip()
    )
