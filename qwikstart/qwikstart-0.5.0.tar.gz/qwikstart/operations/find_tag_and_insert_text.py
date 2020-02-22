import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from ..base_context import BaseContext
from ..utils import ensure_path, indent
from .base import BaseOperation
from .find_tagged_line import TAG_HELP, find_tagged_line_in_file
from .insert_text import LINE_ENDING_HELP, TEXT_HELP, insert_text_in_file
from .utils import FILE_PATH_HELP

__all__ = ["Operation"]

CONTEXT_HELP = {
    "file_path": FILE_PATH_HELP,
    "tag": TAG_HELP,
    "text": TEXT_HELP,
    "line_ending": LINE_ENDING_HELP,
}


@dataclass(frozen=True)
class Context(BaseContext):
    file_path: Path
    tag: str
    text: str
    line_ending: str = os.linesep
    match_indent: bool = True

    @classmethod
    def help(cls, field_name: str) -> Optional[str]:
        return CONTEXT_HELP.get(field_name)


class Operation(BaseOperation[Context, None]):
    """Operation to find a tag and insert text below that tag.

    This is a simple combination of the `find_tagged_line` and `insert_text` operations.
    """

    name: str = "find_tag_and_insert_text"

    def run(self, context: Context) -> None:
        file_path = ensure_path(context.file_path)
        output = find_tagged_line_in_file(file_path, context.tag)
        text = self.get_text(context, output["column"])
        insert_text_in_file(file_path, output["line"], text)

    def get_text(self, context: Context, column: int) -> str:
        text = context.text
        if context.match_indent:
            text = indent(text, column)

        text += context.line_ending
        return text
