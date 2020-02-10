import re
from typing import List

from ttp import ttp

PT_URL = re.compile(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+")


def extract_people(text: str, model) -> List[str]:
    return [
        token.text for token in model(text) if token.ent_type_ == "PER" and token.text
    ]


def extract_stackoverflow_snippets(text: str, length: int) -> List[str]:
    """Extra el código que se encuentra dentro de un comentario de stackoverflow"""
    return re.findall(r"(<code>).{".join(str(length)).join(r",}?(</code>)"), text)


def extract_twitter_hashtags(text: str) -> List[str]:
    return ttp.Parser().parse(text).tags


def extract_twitter_mentions(text: str) -> List[str]:
    return ttp.Parser().parse(text).users


def extract_urls(text: str) -> List[str]:
    return re.findall(PT_URL, text)
