from typing import Mapping, Type, Dict, TypeVar

E = TypeVar("E")


def entity_constructor(row: Mapping, entity: Type[E]) -> E:
    if hasattr(entity, "__meta__"):
        row = {
            k: f.to_python_value(row.get(k, None))
            for k, f in entity.__meta__.fields.items()
        }

    return entity(**row)


def entity_to_db_dict(entity: E) -> Dict:
    if hasattr(entity, "__meta__"):
        return {
            v.column_name: v.to_db_value(getattr(entity, k))
            for k, v in type(entity).__meta__.fields.items()
        }
    return {
        k: v for k, v in entity.__dict__ if not k.startswith("_") and not k.isupper()
    }
