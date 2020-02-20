__version__ = "2.0.0rc1"

from . import errors
from .client import CraftAIClient as Client
from .interpreter import Interpreter
from .time import Time
from .formatters import format_property, format_decision_rules
from .reducer import reduce_decision_rules

# Defining what will be imported when doing `from craft_ai import *`

__all__ = [
    "Client",
    "errors",
    "Interpreter",
    "Time",
    "format_property",
    "format_decision_rules",
    "reduce_decision_rules",
]
