import logging
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from typing_extensions import TypedDict

from .. import base_context
from ..exceptions import TaskParserError
from ..tasks import Task
from .operations import (
    UnparsedOperation,
    get_operations_mapping,
    parse_operation,
    parse_operation_from_step,
)

logger = logging.getLogger(__name__)

OperationsList = Union[List[UnparsedOperation], Dict[str, UnparsedOperation]]


class TaskSpec(TypedDict, total=False):
    context: Dict[str, Any]
    steps: Dict[str, Dict[str, Any]]
    # FIXME: `operations` should be deprecated in favor of `steps`
    operations: OperationsList


def parse_task(task_spec: TaskSpec, source_path: Optional[Path] = None) -> Task:
    """Return task parsed from a task specification dictionary."""
    normalize_context(task_spec, source_path)

    known_operations = get_operations_mapping()

    if task_spec.get("steps"):
        if task_spec.get("operations"):
            logger.warning(
                "Found both `steps` and `operations` in task specification. "
                "Only `steps` will be read."
            )
        operations = [
            parse_operation_from_step(
                {"description": op_desc, **op_def}, known_operations
            )
            for op_desc, op_def in task_spec["steps"].items()
        ]
    elif task_spec.get("operations"):
        logger.info(
            "Note that `operations` in task specification is deprecated. "
            "Use `steps` instead."
        )
        operations = [
            parse_operation(op_def, known_operations)
            for op_def in normalize_operations_list(task_spec["operations"])
        ]
    else:
        raise TaskParserError("Task specification file does not define `steps`.")

    return Task(context=task_spec["context"], operations=operations)


def normalize_operations_list(operations_list: OperationsList) -> List[Dict[str, Any]]:
    """"""
    if isinstance(operations_list, list):
        return operations_list  # type: ignore
    return [{op_name: op_config} for op_name, op_config in operations_list.items()]


def normalize_context(task_spec: TaskSpec, source_path: Optional[Path] = None) -> None:
    task_spec.setdefault("context", {})
    source_dir = source_path.parent if source_path else Path(".")
    task_spec["context"].setdefault(
        "execution_context",
        base_context.ExecutionContext(source_dir=source_dir, target_dir=Path(".")),
    )
