from abc import ABCMeta, abstractmethod
from typing import Callable, Tuple

from nptyping import Array


class AdaptiveSignalProcesserABC(metaclass=ABCMeta):
    method: Callable
    shape: int
    mu: float
    w: Array
    domain: str
    lambda_: float

    @abstractmethod
    def __init__(
        self,
        model: str,
        shape: int,
        mu: float = 0.01,
        w_init: str = "unit",
        domain: str = "time",
        lambda_: float = 1.0,
    ):
        """
        Abstract Class for AdaptiveSignalProcesser

        Args:
            model (str): Algorithm of filter.
            shape (int): Length of filter (and input).
            mu (float, optional): Learning rate. Defaults to 0.01. It should be in range from 0 to 1.
            w_init (str, optional): Initializing method of coef-matrix in filter. Defaults to "unit". It should be "unit", "random" or "zeros".
            domain (str, optional[FOR USE IN THE FUTURE]): Domain for filtering. Defaults to "time".
            lambda_ (float, optional): Regularization term. Defaults to 1.0.
        """
        raise NotImplementedError

    def adopt(self, d: Array, x: Array) -> None:
        """
        Adopt filter

        Args:
            d (Array): Desired array.
            x (Array): Input array.
        """
        raise NotImplementedError

    def update(self, d: Array, x: Array) -> Array:
        """
        Update filter

        Args:
            d (Array): Desired array (as vector, one dimensional).
            x (Array): Input array (as matrix, two dimensional).
        'd' and 'x' should have same length.

        Return:
            w (Array): Filter coef-array.
        """
        raise NotImplementedError
