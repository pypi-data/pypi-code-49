import logging
import textwrap
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound
from termcolor import colored

from ..base_context import BaseContext
from ..utils.templates import DEFAULT_TEMPLATE_VARIABLE_PREFIX, TemplateRenderer
from .base import BaseOperation
from .utils import TEMPLATE_VARIABLE_PREFIX_HELP

__all__ = ["Operation"]

logger = logging.getLogger(__name__)

PYGMENTS_FORMATTER = TerminalFormatter()

CONTEXT_HELP = {
    "template_variable_prefix": TEMPLATE_VARIABLE_PREFIX_HELP,
    "highlight": textwrap.dedent(
        """
            Name of language used for syntax highlighting using `pygments` library.
            See https://pygments.org/docs/lexers/
        """
    ),
}


@dataclass(frozen=True)
class Context(BaseContext):
    message: str
    template_variables: Dict[str, Any] = field(default_factory=dict)
    template_variable_prefix: str = DEFAULT_TEMPLATE_VARIABLE_PREFIX
    display_step_description: bool = False
    highlight: str = ""

    @classmethod
    def help(cls, field_name: str) -> Optional[str]:
        return CONTEXT_HELP.get(field_name)


class Operation(BaseOperation[Context, None]):
    """Operation to echo a message to the console."""

    name: str = "echo"

    def run(self, context: Context) -> None:
        renderer = TemplateRenderer.from_context(context)
        renderer.add_template_filters(colored=colored)
        message = renderer.render_string(context.message)
        if context.highlight:
            try:
                lexer = get_lexer_by_name(context.highlight)
            except ClassNotFound:
                logger.warning(f"No highlighter found for {context.highlight!r}")
            else:
                print(highlight(message, lexer, PYGMENTS_FORMATTER))
                return
        print(message)
