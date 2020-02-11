from dataclasses import dataclass
from typing import Any
from typing import Callable
from typing import Type

from watermill.expressions import Expression
from watermill.stream_types import StreamType


@dataclass
class Window:
    cls: Type[StreamType]
    window_func: Callable[[dict], Any]


def window(
        cls=Type[StreamType],
        window_expression=Expression
):
    def _window_func(element: dict):
        return window_expression(element)

    return Window(
        cls=cls,
        window_func = _window_func
    )
