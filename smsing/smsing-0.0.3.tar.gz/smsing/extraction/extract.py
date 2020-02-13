import re
from typing import List


PT_URL = re.compile(
    r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s\"]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s\"]{2,})"
)
PT_MENTIONS = re.compile(r"((?<=\W)\@[a-zA-Z0-9_]+\b|^\@[a-zA-Z0-9_]+\b)")
PT_HASHTAGS = re.compile(
    r"((?<=\W)\#[a-zA-Z0-9áéíóüöïäë]+\b|^\#[a-zA-Z0-9áéíóüöïäë]+\b)"
)


def extract_people(text: str, model) -> List[str]:
    return [
        token.text for token in model(text) if token.ent_type_ == "PER" and token.text
    ]


def extract_stackoverflow_snippets(text: str, length: int = 0) -> List[str]:
    """Extrae el código que se encuentra dentro de un comentario de stackoverflow"""
    return re.findall(r"(?<=<code>).{" + str(length) + r",}?(?=</code>)", text)


def extract_twitter_hashtags(text: str) -> List[str]:
    return re.findall(PT_HASHTAGS, text)


def extract_twitter_mentions(text: str) -> List[str]:
    return re.findall(PT_MENTIONS, text)


def extract_urls(text: str) -> List[str]:
    return re.findall(PT_URL, text)
