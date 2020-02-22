import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from ..base_context import BaseContext
from ..utils import ensure_path
from .base import BaseOperation
from .utils import FILE_PATH_HELP

__all__ = ["Context", "Operation"]

CONTEXT_HELP = {
    "file_path": FILE_PATH_HELP,
    "search": "Text to search for in file.",
    "replace": "Text used to replace text matching `search`.",
    "use_regex": "Use `re.sub` instead of `str.replace`.",
}


@dataclass(frozen=True)
class Context(BaseContext):
    file_path: Path
    search: str
    replace: str
    use_regex: bool = False

    @classmethod
    def help(cls, field_name: str) -> Optional[str]:
        return CONTEXT_HELP.get(field_name)


class Operation(BaseOperation[Context, None]):
    """Operation for searching for text and replacing it with new text."""

    name: str = "search_and_replace"

    def run(self, context: Context) -> None:
        file_path = ensure_path(context.file_path)

        with file_path.open() as f:
            content_before = f.read()

        replace = search_and_replace_rx if context.use_regex else search_and_replace
        content_after = replace(context.search, context.replace, content_before)

        with file_path.open("w") as f:
            f.write(content_after)


def search_and_replace(search_text: str, replace_text: str, content: str) -> str:
    return content.replace(search_text, replace_text)


def search_and_replace_rx(search_text: str, replace_text: str, content: str) -> str:
    return re.sub(search_text, replace_text, content)
