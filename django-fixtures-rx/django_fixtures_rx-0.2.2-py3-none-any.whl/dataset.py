from abc import abstractmethod, ABCMeta
from typing import Any, List, Tuple


class CommonDatasetMixin:
    dataset = None

    def prepare_dataset_entry(self, entry: Any) -> Tuple[list, dict]:
        return [entry], {}


class TupleDatasetMixin(CommonDatasetMixin):
    def prepare_dataset_entry(self, entry: tuple) -> Tuple[list, dict]:
        return [*entry], {}


class DictDatasetMixin(CommonDatasetMixin):
    def prepare_dataset_entry(self, entry: dict) -> Tuple[list, dict]:
        return [], entry


class GeneratedDatasetMixin(CommonDatasetMixin, metaclass=ABCMeta):
    @property
    def dataset(self) -> List[Any]:
        return self.generate_dataset() or []

    @abstractmethod
    def generate_dataset(self) -> List[Any]:
        pass
