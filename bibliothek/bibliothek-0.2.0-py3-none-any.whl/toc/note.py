from pathlib import Path
from typing import Any
from urllib.parse import quote

from .util import extract_front_matter


class Note:
    '''A markup file'''

    def __init__(self, fp: Path) -> None:
        self.fp = fp
        self.fm = extract_front_matter(fp)
        self.fm['Path'] = quote(str(fp))

    def __repr__(self) -> str:
        return f'Note({self["Path"]})'

    def __getitem__(self, key: str) -> Any:
        return self.fm[key]

# vim: set nospell:
