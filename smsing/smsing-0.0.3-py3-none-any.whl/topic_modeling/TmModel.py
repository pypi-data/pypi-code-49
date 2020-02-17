from . import topic_modeling_methods as tm
from typing import List


class TmModel:
    def __init__(self, model_id: int, model_path: str):
        self._model_id = model_id
        self._path = model_path

    def build_corpus(self, data: List[str], **kwargs):
        tm.build_corpus(
            self._model_id, self._path, data, **kwargs,
        )

