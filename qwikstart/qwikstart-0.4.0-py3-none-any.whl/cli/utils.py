import dataclasses
import os.path as pth
import textwrap
from pathlib import Path
from typing import Any, List, Optional

from jinja2 import Environment, FileSystemLoader
from termcolor import colored

from ..parser import get_operations_mapping

__all__ = ["get_operation_help", "OperationHelp"]


def get_template_environment() -> Environment:
    LOCAL_DIR = pth.dirname(pth.abspath(__file__))
    templates_dir = str(Path(LOCAL_DIR, "templates"))
    env = Environment(loader=FileSystemLoader([templates_dir]))
    env.filters["colored"] = colored
    env.filters["indent"] = indent
    return env


def indent(text: str, level: int = 1) -> str:
    prefix = "    " * level
    return textwrap.indent(text, prefix)


@dataclasses.dataclass(frozen=True)
class ContextVar:
    name: str
    annotation: Any
    default: Any = dataclasses.MISSING
    description: Optional[str] = ""

    @property
    def is_required(self) -> bool:
        return self.default is dataclasses.MISSING


@dataclasses.dataclass(frozen=True)
class OperationHelp:
    name: str
    docstring: Optional[str]
    required_context: List[ContextVar]
    optional_context: List[ContextVar]


def get_operation_help(op_name: str) -> OperationHelp:
    op_mapping = get_operations_mapping()
    operation = op_mapping[op_name]

    context_class = operation.get_context_class()
    required_context = []
    optional_context = []
    # FIXME: Ignore mypy error when accessing __dataclass_fields__.
    # See https://github.com/python/mypy/issues/6568
    for field in context_class.__dataclass_fields__.values():  # type:ignore
        if field.name != "execution_context":
            context_var = ContextVar(
                name=field.name,
                annotation=field.type,
                default=_get_default(field),
                description=context_class.help(field.name),
            )
            if context_var.is_required:
                required_context.append(context_var)
            else:
                optional_context.append(context_var)

    return OperationHelp(
        name=op_name,
        docstring=operation.__doc__,
        required_context=required_context,
        optional_context=optional_context,
    )


# FIXME: Ignore typing error for Field without type parameters.
# Using `Field` mypy error: Missing type parameters for generic type "Field"
# Using `Field[Any]` runtime error: TypeError: 'type' object is not subscriptable
def _get_default(field: dataclasses.Field) -> Any:  # type:ignore
    return (
        field.default
        if field.default is not dataclasses.MISSING
        # FIXME: Ignore mypy error when accessing callable attribute.
        # See https://github.com/python/mypy/issues/6910
        else field.default_factory  # type:ignore
    )
