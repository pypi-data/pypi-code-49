from dataclasses import dataclass
from typing import Any, Dict, Sequence

from .operations import BaseOperation

__all__ = ["Task"]


@dataclass
class Task:
    """A series of operations to complete an qwikstart task."""

    # FIXME: Allow subclasses of BaseOperation and specify type parameters.
    operations: Sequence[BaseOperation]  # type:ignore
    context: Dict[str, Any]

    def execute(self) -> Dict[str, Any]:
        context = self.context
        for operation in self.operations:
            context = operation.execute(context)
        return context
