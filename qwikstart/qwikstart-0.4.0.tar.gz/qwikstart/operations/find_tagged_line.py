from dataclasses import dataclass
from pathlib import Path

from typing_extensions import TypedDict

from ..base_context import BaseContext
from ..exceptions import OperationError
from .base import BaseOperation

__all__ = ["Context", "Operation", "Output"]


@dataclass(frozen=True)
class Context(BaseContext):
    file_path: Path
    tag: str


class Output(TypedDict):
    line: int
    column: int


class Operation(BaseOperation[Context, Output]):
    """Operation inserting text on a given line"""

    name: str = "find_tagged_line"

    def run(self, context: Context) -> Output:
        tag = context.tag
        with context.file_path.open() as f:
            for line_number, line in enumerate(f, 1):
                if tag in line:
                    column = line.find(tag)
                    return Output(line=line_number, column=column)
            else:
                raise OperationError("Failed to find line tagged with {}")
