from typing import Sequence
from BTrees.OOBTree import OOBTree


def get_result_subpath(root, cache_path: Sequence[str], create_oobtree: bool = False):
    result_path = root
    for part in cache_path[:-1]:
        try:
            result_path = result_path[part]
        except KeyError as e:
            if create_oobtree:
                # Creates collections on the way to getting nested key
                result_path[part] = OOBTree()
                result_path = result_path[part]
            else:
                raise e
    return result_path