import functools
from typing import Dict, List, Tuple

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
                data[i] = prep.remove_multiple_spaces(step(text, **step_params)).strip()

        return data

    @staticmethod
    def pack_data(ids: List[int], docs: List[str]) -> Dict:
        """Converts two lists of ids and docs into a dictionary"""
        return {
            text_id: {"id": text_id, "text": value} for text_id, value in zip(ids, docs)
        }

    @staticmethod
    def unpack_data(data: Dict) -> Tuple[List[int], List[str]]:
        """Returns a list of ids and a list of docs from a dictionary"""
        ids = [int(text_id) for text_id in data.keys()]
        docs = [value["text"] for value in data.values()]

        return ids, docs
