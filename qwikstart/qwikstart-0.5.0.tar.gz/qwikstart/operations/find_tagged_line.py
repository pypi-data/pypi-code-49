import textwrap
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from typing_extensions import TypedDict

from ..base_context import BaseContext
from ..exceptions import OperationError
from ..utils import ensure_path
from .base import BaseOperation
from .utils import FILE_PATH_HELP

__all__ = ["Context", "Operation", "Output"]

TAG_HELP = textwrap.dedent(
    """
        Text used as a placeholder for detecting where to insert text. For example:

            # qwikstart: inject-line-below
    """
)
CONTEXT_HELP = {"file_path": FILE_PATH_HELP, "tag": TAG_HELP}


@dataclass(frozen=True)
class Context(BaseContext):
    file_path: Path
    tag: str

    @classmethod
    def help(cls, field_name: str) -> Optional[str]:
        return CONTEXT_HELP.get(field_name)


class Output(TypedDict):
    line: int
    column: int


class Operation(BaseOperation[Context, Output]):
    """Operation inserting text on a given line"""

    name: str = "find_tagged_line"

    def run(self, context: Context) -> Output:
        file_path = ensure_path(context.file_path)
        return find_tagged_line_in_file(file_path, context.tag)


def find_tagged_line_in_file(file_path: Path, tag: str) -> Output:
    with file_path.open() as f:
        for line_number, line in enumerate(f, 1):
            if tag in line:
                column = line.find(tag)
                return Output(line=line_number, column=column)
        else:
            msg = f"Failed to find line in {file_path} tagged with {tag!r}"
            raise OperationError(msg)
