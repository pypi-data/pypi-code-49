import functools
from typing import Dict, List

from . import preprocessing as prep


class Preprocesser:
    def __init__(self, *steps, **params):
        self._steps = steps
        self._params = params or {}

    def process_steps(self, data: List[str]) -> List[str]:
        params = self._params or {}
        for step in self._steps:
            step_params = {
                param.split("__")[1]: value
                for param, value in params.items()
                if param.startswith(f"{step.__name__}__")
            }
            for i, text in enumerate(data):
                data[i] = step(text, **step_params)

        return data
