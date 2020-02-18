import collections
from typing import Any, Dict, NamedTuple, Optional, Tuple, Type, Union, cast

from .. import utils
from ..exceptions import TaskParserError
from ..operations import BaseOperation, GenericOperation

__all__ = ["OperationDefinition", "parse_operation"]


OperationMapping = Dict[str, Type[GenericOperation]]
UnparsedOperation = Union[str, Dict[str, Dict[str, Any]], Tuple[str, Dict[str, Any]]]
RESERVED_WORDS_OPERATION_CONFIG = {"local_context", "input_mapping", "output_mapping"}


def get_operations_mapping() -> OperationMapping:
    """Return mapping of known operation names to their respective operation classes."""
    # FIXME: Each subclass of BaseOperation generates two subclasses: The actual
    # subclass AND the `BaseOperation[TContext, TOutput]` used as superclass. Ignore
    # operations without names to avoid these classes.
    operations = [op for op in BaseOperation.__subclasses__() if hasattr(op, "name")]
    op_mapping = {op.name: op for op in operations}

    # Add any operations that have aliases to our mapping:
    for op in operations:
        if op.aliases:
            for name in op.aliases:
                op_mapping.setdefault(name, op)

    # FIXME: Cast to avoid mypy error due to use of Type with abstract baseclass
    # See https://github.com/python/mypy/issues/4717
    return cast(OperationMapping, op_mapping)


class OperationDefinition(NamedTuple):
    name: str
    config: Dict[str, Any]

    @property
    def parsed_config(self) -> Dict[str, Any]:
        """Return operation configuration parsed from raw config input.

        Any configuration that is not a reserved word will be added to the
        `local_context` passed to the operation initializer.
        """
        local_context = self.config.get("local_context", {})
        input_mapping = self.config.get("input_mapping")
        output_mapping = self.config.get("output_mapping")
        local_context.update(
            {
                key: value
                for key, value in self.config.items()
                if key not in RESERVED_WORDS_OPERATION_CONFIG
            }
        )
        return {
            "local_context": local_context,
            "input_mapping": input_mapping,
            "output_mapping": output_mapping,
        }


def parse_operation(
    op_def: UnparsedOperation,
    known_operations: Optional[Dict[str, Type[GenericOperation]]] = None,
) -> GenericOperation:
    if known_operations is None:
        known_operations = get_operations_mapping()

    op_def = normalize_op_definition(op_def)

    if op_def.name not in known_operations:
        raise TaskParserError(f"Could not find operation named '{op_def.name}'")

    operation_class = known_operations[op_def.name]
    return operation_class(**op_def.parsed_config)


def normalize_op_definition(op_def: UnparsedOperation) -> OperationDefinition:
    if isinstance(op_def, str):
        return OperationDefinition(name=op_def, config={})
    elif isinstance(op_def, collections.abc.Mapping):
        if len(op_def) != 1:
            raise TaskParserError(
                "Operation definition with dict should only have a single key"
                f", but given {op_def}"
            )
        op_name = utils.first(op_def.keys())
        return OperationDefinition(name=op_name, config=op_def[op_name])
    elif isinstance(op_def, collections.abc.Sequence):
        if len(op_def) != 2:
            raise TaskParserError(
                "Operation definition with sequence should only have two items"
                f", but given {op_def}"
            )
        return OperationDefinition(*op_def)
    raise TaskParserError(f"Could not parse operation definition: {op_def}")
