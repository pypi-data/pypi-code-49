from abc import ABC, abstractmethod
from typing import Any

__author__ = 'Darryl Oatridge'


class AbstractModel(ABC):

    @abstractmethod
    def train(self, canonical: Any, **model_params) -> Any:
        """"""
        pass

    @abstractmethod
    def predict(self, canonical: Any, meta_model: Any, **predict_params) -> Any:
        """"""
        pass

    @property
    @abstractmethod
    def model_params(self) -> dict:
        """"""
        pass

    @property
    @abstractmethod
    def predict_params(self) -> dict:
        """"""
        pass
