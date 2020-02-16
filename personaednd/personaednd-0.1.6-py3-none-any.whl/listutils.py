from random import choice


def add(iterable: list, value: (float, int, str)) -> list:
    """Adds a value into iterable."""
    iterable.append(value)
    iterable.sort()
    return iterable


def merge(original_list: list, merged_list_values: (list, tuple)) -> list:
    """Merges individual unique merged_list_values into original_list."""
    for value in merged_list_values:
        if value not in original_list:
            original_list.append(value)
    return original_list


def pick(iterable: list) -> (bool, float, int, str):
    """Chooses random value from list then removes it."""
    try:
        if not isinstance(iterable, list):
            raise TypeError
        if len(iterable) is 0:
            raise ValueError
        selection = choice(iterable)
        iterable.remove(selection)
        return selection
    except (TypeError, ValueError):
        return False


def purge(original_list: list, purged_list_values: (list, tuple)) -> list:
    """Purges individual unique purged_list_values from original_list."""
    for value in purged_list_values:
        if value in original_list:
            original_list.remove(value)
    return original_list
