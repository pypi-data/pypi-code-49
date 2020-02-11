"""Define various miscellaneous utility functions."""
from typing import Any


def get_nearest_by_numeric_key(data: dict, key: int) -> Any:
    """Return the dict element whose numeric key is closest to a target."""
    return data.get(key, data[min(data.keys(), key=lambda k: abs(k - key))])
