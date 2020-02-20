__version__ = "2.0.0rc2"

from . import errors
from .client import CraftAIClient as Client
from .interpreter import Interpreter
from .time import Time
from .formatters import format_property, format_decision_rules
from .reducer import reduce_decision_rules
from .tree_utils import collect_paths_from_tree, compute_tree_decision_paths_neighbors

# Defining what will be imported when doing `from craft_ai import *`

__all__ = [
    "Client",
    "errors",
    "Interpreter",
    "Time",
    "format_property",
    "format_decision_rules",
    "reduce_decision_rules",
    "collect_paths_from_tree",
    "compute_tree_decision_paths_neighbors",
]
