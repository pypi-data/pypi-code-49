import textwrap
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from ..base_context import BaseContext
from ..utils.templates import DEFAULT_TEMPLATE_VARIABLE_PREFIX, TemplateRenderer
from .base import BaseOperation
from .utils import TEMPLATE_VARIABLE_PREFIX_HELP

__all__ = ["Operation"]

CONTEXT_HELP = {
    "context_defs": textwrap.dedent(
        """
            Definition of variables to add to the context. Values can be defined using
            template variables; e.g.:

                context_defs:
                    greeting: "Hello {{ qwikstart.name }}!"
        """
    ),
    "template_variable_prefix": TEMPLATE_VARIABLE_PREFIX_HELP,
}


@dataclass(frozen=True)
class Context(BaseContext):
    context_defs: Dict[str, Any]
    template_variables: Dict[str, Any] = field(default_factory=dict)
    template_variable_prefix: str = DEFAULT_TEMPLATE_VARIABLE_PREFIX
    display_step_description: bool = False

    @classmethod
    def help(cls, field_name: str) -> Optional[str]:
        return CONTEXT_HELP.get(field_name)


class Operation(BaseOperation[Context, Dict[str, Any]]):
    """Operation to context variables to the operation context."""

    name: str = "define_context"

    def run(self, context: Context) -> Dict[str, Any]:
        renderer = TemplateRenderer.from_context(context)

        non_string_variables = {
            key: value
            for key, value in context.context_defs.items()
            if not isinstance(value, str)
        }
        renderer.update_template_variables(non_string_variables)

        string_variables = {}
        for key, value in context.context_defs.items():
            if isinstance(value, str):
                value = renderer.render_string(value)
                string_variables[key] = value
                # Ensure that templates can use the newly rendered variable.
                renderer.add_template_variable(key, value)

        return {**non_string_variables, **string_variables}
