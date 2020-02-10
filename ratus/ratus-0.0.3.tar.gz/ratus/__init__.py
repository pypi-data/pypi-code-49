"""
ratus - A simple expression language.

ratus is a simple expression language intended to be used to easily and safely
extend applications in a controllable way. It provides the following features:

- Callable functions

  - These can be injected when evaluating the expression but they cannot be
    defined within the expression language
  - ``if`` is provided by default but can be overridden if you really want to

- Simple math operations, more advanced functions can be implemented as
  functions

  - Addition (``+``)
  - Subtractions (``-``)
  - Multiplication (``*``)
  - Division (``/``)

- Comparison operators

  - Equal (``=``)
  - Not equal (``!=``)
  - Greater than (``>``)
  - Greater than or equal (``>=``)
  - Less than (``<``)
  - Less than or equal (``<=``)

- Literals

  - String (double and single quotes)
  - Integer (positive and negative)
  - Float (positive and negative)
"""
from typing import Any, Callable, Dict, Optional

from ratus.execer import Executor
from ratus.parse import Parser
from ratus.token import Tokeniser

__version__ = "0.0.1"

__all__ = ["Evaluator", "token", "parse", "execer"]


class Evaluator:
    "Expression evaluator."

    def __init__(
        self, injected_functions: Optional[Dict[str, Callable[..., Any]]] = None
    ) -> None:
        self.tokeniser = Tokeniser()
        self.parser = Parser()
        self.executor = Executor(injected_functions)

    def evaluate(self, source: str) -> Any:
        """Evaluate an input as a ratus expression."""
        tokens = self.tokeniser.tokenise(source)

        expression = self.parser.parse(tokens)

        return self.executor.execute(expression)
