import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from ..base_context import BaseContext
from ..utils import ensure_path
from .base import BaseOperation
from .utils import FILE_PATH_HELP

__all__ = ["Operation"]

CONTEXT_HELP = {
    "file_path": FILE_PATH_HELP,
    "text": "Text that will be appended to `file_path`",
    "prefix": "Text added before appended `text`",
    "suffix": "Text added after appended `text`",
}


@dataclass(frozen=True)
class Context(BaseContext):
    file_path: Path
    text: str
    prefix: str = os.linesep
    suffix: str = ""

    @classmethod
    def help(cls, field_name: str) -> Optional[str]:
        return CONTEXT_HELP.get(field_name)


class Operation(BaseOperation[Context, None]):
    """Operation for appending text to a given file."""

    name: str = "append_text"

    def run(self, context: Context) -> None:
        file_path = ensure_path(context.file_path)

        with file_path.open("a") as f:
            f.write(self.get_text(context))

    def get_text(self, context: Context) -> str:
        return "".join([context.prefix, context.text, context.suffix])
