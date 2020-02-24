from collections import defaultdict
from functools import reduce
from pathlib import Path
from typing import Any, Dict, Optional

from funcy import compose, update_in
import yaml


def compile_schema(spec_dir: Optional[str] = None) -> Dict[str, Any]:
    """Load schema from filesystem structure, determined by ``spec_dir`` attribute.

    :param spec_dir: root directory relative to the schema
    :return: swagger schema compatible with Connexion framework
    """
    defaults = _compile(Path(__file__).parent / "schemas")  # type: ignore

    if not spec_dir:
        return defaults

    applevel = _compile(spec_dir)

    def merge_values(a, b):
        return b if not (isinstance(a, dict) and isinstance(b, dict)) else {**a, **b}

    common = {k: merge_values(defaults[k], applevel[k]) for k in set(defaults) & set(applevel)}

    return _filter_null_keys({**defaults, **applevel, **common})


def _compile(spec_dir: str) -> Dict[str, Any]:
    root = Path(spec_dir)

    if not (root.exists() and root.is_dir()):
        raise ValueError(f"Directory {root} does not exist.")

    def load_spec(path):
        """Load partial schema spec from a *.yml file.

        :param path: A filesystem path
        :return: Return tuple of two items:
                 1) relative filesystem path parts serving as a key path for a nested dictionary
                 2) partial schema spec loaded from a *.yml file
        """
        with path.open() as f:
            spec = yaml.safe_load(f)

        return path.relative_to(root).parent.parts, spec  # type: ignore

    def update_value(acc, item):
        path, spec = item
        return update_in(acc, path, lambda val: {**val, **spec}, default={})

    return compose(
        lambda specs: reduce(update_value, specs, {}),
        # ↑ Build the dictionary
        lambda paths: map(load_spec, paths),
        # ↑ Load specs from fs paths
    )(root.glob("**/*.yml"))


def _filter_null_keys(d: Dict[str, Any]) -> Dict[str, Any]:
    """Recursively remove all keys from a dictionary that have None value.

    :param d: input dictionary
    :return: output dictionary with null keys removed
    """
    target: Dict[str, Any] = defaultdict(dict)

    for key, value in d.items():
        if isinstance(value, dict):
            target[key] = _filter_null_keys(value)
        elif value:
            target[key] = value

    return target
