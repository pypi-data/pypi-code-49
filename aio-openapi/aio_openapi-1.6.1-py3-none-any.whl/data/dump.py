from dataclasses import asdict, fields
from typing import Any, Dict, List, Optional, cast

from ..utils import iter_items, TypingInfo
from .fields import DUMP


def is_nothing(value: Any) -> bool:
    if value == 0 or value is False:
        return False
    return not value


def dump_dataclass(schema: type, data: Optional[Dict] = None) -> Dict:
    """Dump a dictionary of data with a given dataclass dump functions
    If the data is not given, the schema object is assumed to be
    an instance of a dataclass.
    """
    data = asdict(schema) if data is None else data
    cleaned = {}
    fields_ = {f.name: f for f in fields(schema)}
    for name, value in iter_items(data):
        if name not in fields_ or is_nothing(value):
            continue
        field = fields_[name]
        dump = field.metadata.get(DUMP)
        if dump:
            value = dump(value)
        cleaned[field.name] = value

    return cleaned


def dump_list(schema: Any, data: List) -> List[Dict]:
    """Validate a dictionary of data with a given dataclass
    """
    return [dump(schema, d) for d in data]


def dump_dict(schema: Any, data: Dict[str, Any]) -> List[Dict]:
    """Validate a dictionary of data with a given dataclass
    """
    return {name: dump(schema, d) for name, d in data.items()}


def dump(schema: Any, data: Any):
    type_info = TypingInfo.get(schema)
    if type_info.container is list:
        return dump_list(type_info.element, cast(List, data))
    elif type_info.container is dict:
        return dump_dict(type_info.element, cast(Dict, data))
    elif type_info.is_dataclass:
        return dump_dataclass(type_info.element, cast(Dict, data))
    else:
        return data
