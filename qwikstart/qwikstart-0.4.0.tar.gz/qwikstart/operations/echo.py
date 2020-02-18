from dataclasses import dataclass, field
from typing import Any, Dict

from termcolor import colored

from ..base_context import BaseContext
from ..utils.templates import DEFAULT_TEMPLATE_VARIABLE_PREFIX, TemplateRenderer
from .base import BaseOperation

__all__ = ["Operation"]


@dataclass(frozen=True)
class Context(BaseContext):
    message: str
    template_variables: Dict[str, Any] = field(default_factory=dict)
    template_variable_prefix: str = DEFAULT_TEMPLATE_VARIABLE_PREFIX


class Operation(BaseOperation[Context, None]):
    """Operation to echo a message to the console."""

    name: str = "echo"

    def run(self, context: Context) -> None:
        renderer = TemplateRenderer.from_context(context)
        renderer.add_template_filters(colored=colored)
        print(renderer.render_string(context.message))
