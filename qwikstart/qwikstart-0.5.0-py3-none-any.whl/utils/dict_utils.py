import copy
from typing import Any, Dict, Mapping, Tuple, cast


def merge_nested_dicts(
    default: Mapping[str, Any], overwrite: Mapping[str, Any]
) -> Dict[str, Any]:
    """Return new dictionary from the combination of `default` and `overwrite`.

    Dict values that are dictionaries themselves will be updated, whilst preserving
    existing keys.

    Adapted from `cookiecutter.config.merge_configs`.
    """
    new_dict: Dict[str, Any] = copy.deepcopy(cast(Dict[str, Any], default))

    for k, v in overwrite.items():
        merge_needed = isinstance(v, dict) and k in default
        new_dict[k] = merge_nested_dicts(default[k], v) if merge_needed else v

    return new_dict


def get_nested_dict_value(
    nested_dict: Dict[str, Any], nested_key: str, separator: str = "."
) -> Any:
    final_key, sub_dict, = _get_final_nested_dict_and_key(
        nested_dict, nested_key, separator=separator
    )
    return sub_dict[final_key]


def pop_nested_dict_value(
    nested_dict: Dict[str, Any], nested_key: str, separator: str = "."
) -> Any:
    final_key, sub_dict, = _get_final_nested_dict_and_key(
        nested_dict, nested_key, separator=separator
    )
    return sub_dict.pop(final_key)


def set_nested_dict_value(
    nested_dict: Dict[str, Any], nested_key: str, value: Any, separator: str = "."
) -> None:
    sub_dict = nested_dict
    *sub_keys, final_key = nested_key.split(separator)
    for key in sub_keys:
        if key not in sub_dict:
            sub_dict[key] = {}

        sub_dict = sub_dict[key]
        if not isinstance(sub_dict, dict):
            msg = f"Expected key {key!r} to contain dict but given {sub_dict}"
            raise ValueError(msg)

    sub_dict[final_key] = value


def remap_dict(
    original_dict: Mapping[str, Any],
    key_mapping: Mapping[str, str],
    nested_key_separator: str = ".",
) -> Dict[str, Any]:
    """Return dict with any keys in `key_mapping` renamed.

    Args:
        original_dict: Dictionary with keys to be renamed.
        key_mapping: Dictionary mapping keys in `original_dict` to new keys.
            Any keys not in `key_mapping` are returned unchanged.
        nested_key_separator: Separator used in keys in `key_mapping` to specify nested
            dictionaries.
    """
    new_dict = copy.deepcopy(cast(Dict[str, Any], original_dict))
    for original_key, new_key in key_mapping.items():
        if nested_key_separator in original_key:
            value = pop_nested_dict_value(new_dict, original_key)
        elif original_key in new_dict:
            value = new_dict.pop(original_key)
        else:
            continue  # pragma: no cover

        if nested_key_separator in new_key:
            set_nested_dict_value(new_dict, new_key, value)
        else:
            new_dict[new_key] = value
    return new_dict


def _get_final_nested_dict_and_key(
    nested_dict: Dict[str, Any], nested_key: str, separator: str = "."
) -> Tuple[str, Dict[str, Any]]:
    sub_dict = nested_dict
    *sub_keys, final_key = nested_key.split(separator)
    for key in sub_keys:
        if key not in sub_dict:
            raise KeyError(f"Nested key {nested_key!r} not found in {nested_dict}")

        sub_dict = sub_dict[key]
        if not isinstance(sub_dict, dict):
            msg = f"Expected key {key!r} to contain dict but given {sub_dict}"
            raise ValueError(msg)

    if final_key not in sub_dict:
        raise KeyError(f"Nested key {nested_key!r} not found in {nested_dict}")

    return final_key, sub_dict
