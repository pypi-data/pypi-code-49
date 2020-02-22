import logging
import subprocess
from dataclasses import dataclass, field
from typing import Any, Dict, List, Union

from ..base_context import BaseContext
from ..utils.templates import DEFAULT_TEMPLATE_VARIABLE_PREFIX, TemplateRenderer
from .base import BaseOperation

__all__ = ["Operation"]

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Context(BaseContext):
    cmd: Union[List[str], str]
    template_variables: Dict[str, Any] = field(default_factory=dict)
    template_variable_prefix: str = DEFAULT_TEMPLATE_VARIABLE_PREFIX


class Operation(BaseOperation[Context, None]):
    """Operation to run an arbitrary shell command."""

    name: str = "shell"

    def run(self, context: Context) -> None:
        renderer = TemplateRenderer.from_context(context)
        if isinstance(context.cmd, list):
            cmd = [renderer.render_string(arg) for arg in context.cmd]
        else:
            # FIXME: Ignore mypy complaint caused by `cmd` assignment to list above.
            cmd = renderer.render_string(context.cmd)  # type: ignore

        logger.info(f"Running command: {cmd}")

        response = subprocess.run(
            cmd,
            shell=isinstance(cmd, str),
            # FIXME: Once Python 3.6 support is dropped use capture_output=True
            # instead of stdout/stderr and text instead of universal_newlines
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        response.check_returncode()

        logger.info(response.stdout)
