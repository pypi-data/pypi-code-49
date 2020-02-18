import functools
from typing import Dict, List, Tuple

from . import preprocessing as prep
from .preprocessing.errors import ModelNotProvidedException
from threading import Thread


class Preprocesser:
    def __init__(self, *steps, **params):
        self._steps = steps
        self._params = params or {}

    def process_steps(self, data: List[str], workers: int = 1) -> List[str]:
        threads = []

        self._data_chunks = {i: [] for i in range(workers)}

        for worker in range(workers):
            first_doc = int(len(data) * worker / workers)
            last_doc = int(len(data) * (worker + 1) / workers)
            chunk = data[first_doc:last_doc]
            t = Thread(
                name=f"thread_{worker}", target=self._process_chunk, args=[1, chunk]
            )
            threads.append(t)
            t.start()

        for thread in threads:
            thread.join()

        processed_data = []

        for value in self._data_chunks.values():
            processed_data.extend(value)

        return processed_data

    def _process_chunk(self, worker_id, data_chunk: List[str]):
        params = self._params or {}

        for step in self._steps:
            step_params = {
                param.split("__")[1]: value
                for param, value in params.items()
                if param.startswith(f"{step.__name__}__")
            }
            for i, text in enumerate(data_chunk):
                try:
                    data_chunk[i] = prep.remove_multiple_spaces(
                        step(text, **step_params)
                    ).strip()
                except Exception as e:
                    if (
                        e.args[0].split(")")[1].strip()
                        == "missing 1 required positional argument: 'model'"
                    ):
                        raise ModelNotProvidedException
                    else:
                        raise e

        self._data_chunks[worker_id] = data_chunk

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
