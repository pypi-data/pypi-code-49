import logging
import shutil
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Optional, Union

from ..base_context import BaseContext
from ..utils import ensure_path
from ..utils.templates import DEFAULT_TEMPLATE_VARIABLE_PREFIX, TemplateRenderer
from .base import BaseOperation

__all__ = ["Operation"]

logger = logging.getLogger(__name__)

CONTEXT_HELP = {
    "target_path": textwrap.dedent(
        """
            File path where rendered template will be saved. This will be relative to
            the `target_dir` (default '.') specified in the execution context.
        """
    )
}


@dataclass(frozen=True)
class Context(BaseContext):
    target_path: Union[Path, str]
    template_path: str
    template_variables: Dict[str, Any] = field(default_factory=dict)
    template_variable_prefix: str = DEFAULT_TEMPLATE_VARIABLE_PREFIX

    @classmethod
    def help(cls, field_name: str) -> Optional[str]:
        return CONTEXT_HELP.get(field_name)


class Operation(BaseOperation[Context, None]):
    """Operation to add a file to a project."""

    name: str = "add_file"

    def run(self, context: Context) -> None:
        renderer = TemplateRenderer.from_context(context)
        with ensure_path(context.target_path).open("w") as f:
            f.write(renderer.render(context.template_path))

        # Copy file mode (i.e. permissions) of template to target file.
        resolved_template_path = renderer.resolve_template_path(context.template_path)
        shutil.copymode(resolved_template_path, context.target_path)

        logger.info(f"Wrote file to {context.target_path}")
