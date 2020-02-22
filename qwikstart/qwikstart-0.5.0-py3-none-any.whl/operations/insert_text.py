import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from ..base_context import BaseContext
from ..utils import ensure_path, indent
from .base import BaseOperation
from .utils import FILE_PATH_HELP

__all__ = ["Operation"]

TEXT_HELP = "Text that will be inserted."
LINE_ENDING_HELP = "Text appended to the end of inserted text."
CONTEXT_HELP = {
    "file_path": FILE_PATH_HELP,
    "text": TEXT_HELP,
    "line": "Line number where text will be inserted.",
    "column": "Column where the text will be inserted.",
    "line_ending": LINE_ENDING_HELP,
}


@dataclass(frozen=True)
class Context(BaseContext):
    file_path: Path
    text: str
    line: int
    column: int
    line_ending: str = os.linesep
    match_indent: bool = True

    @classmethod
    def help(cls, field_name: str) -> Optional[str]:
        return CONTEXT_HELP.get(field_name)


class Operation(BaseOperation[Context, None]):
    """Operation inserting text on a given line"""

    name: str = "insert_text"

    def run(self, context: Context) -> None:
        file_path = ensure_path(context.file_path)
        text = self.get_text(context)
        insert_text_in_file(file_path, context.line, text)

    def get_text(self, context: Context) -> str:
        text = context.text
        if context.match_indent:
            text = indent(text, context.column)

        text += context.line_ending
        return text


def insert_text_in_file(file_path: Path, line_number: int, text: str) -> None:
    with file_path.open() as f:
        contents = f.readlines()

    contents.insert(line_number, text)

    with file_path.open("w") as f:
        f.writelines(contents)
