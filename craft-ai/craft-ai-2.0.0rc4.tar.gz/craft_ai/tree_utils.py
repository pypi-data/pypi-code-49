from copy import copy
from .errors import CraftAiError


def _update_paths(paths, idx):
    """ add new path build on idx to all paths """
    if paths:
        return paths + ["{}-{}".format(paths[-1], idx)]
    return [str(idx)]


def _paths(tree, paths=None):
    """ return a raw list of all paths in a tree """
    if paths is None:
        paths = ["0"]
    if "children" in tree:
        current_paths = copy(paths)
        for i, child in enumerate(tree["children"]):
            paths.extend(_paths(child, _update_paths(current_paths, i)))
        return paths
    return paths


def _get_paths(tree):
    """ return a set of all paths in a tree """
    return set(_paths(tree))


def _is_neighbour(path0, path1):
    """
        Boolean function. A neighbour has exactly the same path excepted for the last node
    """
    return path0[:-1] == path1[:-1] and path0 != path1


def _get_neighbours(paths, decision_path):
    """
    Collect all neighbours paths of the given decision path
    param: paths: paths aggregator
    param: decision_path: decision path to get neighbours from
    """
    split = decision_path.split("-")
    neighbours = []
    for step in range(1, len(split) + 1):
        for path in paths:
            if _is_neighbour(path, "-".join(split[:step])):
                neighbours.append(path)
    return neighbours


def _extract_tree(tree):
    if not isinstance(tree, dict):
        raise CraftAiError(
            """Invalid input given. The tree should be a dict, """
            """but a {} has been received.""".format(type(tree))
        )
    if "trees" in tree:
        target = list(tree["trees"])[0]
        tree = tree["trees"][target]
    return tree


def collect_paths_from_tree(tree):
    """ return a set of all decision paths in a craft_ai tree """
    return _get_paths(_extract_tree(tree))


def compute_tree_decision_paths_neighbors(
    tree, decision_path, max_depth=None, include_self=False
):
    """
    collect all neighbors decision paths of the given decision path
    param: tree: craft_ai tree or simple tree
    param: decision_path: string tree path eg. "0-2-1"
    param: max_depth: positive int filter neighbours on their depth
    param: include_self: boolean. include the given decision_path to the neighbours.
    """
    paths = _get_paths(_extract_tree(tree))
    if decision_path not in paths:
        raise CraftAiError(
            """Invalid decision path given. """
            """{} not found in tree""".format(decision_path)
        )

    dp_depth = len(decision_path.split("-"))
    neighbours = _get_neighbours(paths, decision_path)
    if max_depth is None:
        max_depth = dp_depth
    if max_depth < 0:
        raise CraftAiError(
            """Invalid max depth given: {} should be None or a positive integer """.format(
                max_depth
            )
        )
    filtered = [n for n in neighbours if len(n.split("-")) <= max_depth]
    if include_self:
        filtered.append(decision_path)
    return filtered
