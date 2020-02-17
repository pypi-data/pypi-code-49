import re
from typing import Callable


def delete_by_regex(delete_regex: str) -> Callable[[str], str]:
    """implement replacement with regex"""
    compiled_regex = re.compile(delete_regex)

    def remove(text: str) -> str:
        out = compiled_regex.sub("", text)
        return out

    return remove


def replace_by_dict(dic) -> Callable[[str], str]:
    """implement replacement with dictionary"""

    def _replace(text: str) -> str:
        out = text.translate(str.maketrans(dic))
        return out

    return _replace
