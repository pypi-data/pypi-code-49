from typing import Any
from typing import Callable


class Expression:
    def __init__(self, expression_func: Callable):
        self._expression_func = expression_func

    def __call__(self, element: dict):
        return self._expression_func(element)

    def __floordiv__(self, other: int):
        return true_div_expression(self._expression_func, other)

    def __add__(self, other):
        return add_expression(self._expression_func, other)

    def __sub__(self, other):
        return add_expression(self._expression_func, -other)

    def __mul__(self, other):
        return mul_expression(self._expression_func, other)

    def __mod__(self, other):
        return mod_expression(self._expression_func, other)

    def __getitem__(self, item):
        return get_item_expression(self._expression_func, item)


def get_item_expression(expression_func: Callable[[dict], Any], other: str) -> Expression:
    def _get_item_expression(element: dict):
        return expression_func(element)[other]
    return Expression(_get_item_expression)


def get_field(field_name: str) -> Expression:
    def _get_field(element: dict):
        return element[field_name]
    return Expression(_get_field)


def function_call(func: Callable) -> Expression:
    def _function_call(element: dict):
        return func(element)
    return Expression(_function_call)


def const_expression(constant: Any) -> Expression:
    return Expression(lambda *_: constant)


def evaluate_right(other, element):
    return other(element) if isinstance(other, Expression) else other


def true_div_expression(expression_func: Callable[[dict], Any], other) -> Expression:
    def _true_div_expression(element: dict):
        return expression_func(element) // evaluate_right(other, element)
    return Expression(_true_div_expression)


def mod_expression(expression_func: Callable[[dict], Any], other) -> Expression:
    def _mod_expression(element: dict):
        return expression_func(element) % evaluate_right(other, element)
    return Expression(_mod_expression)


def mul_expression(expression_func: Callable[[dict], Any], other) -> Expression:
    def _mul_expression(element: dict):
        return expression_func(element) * evaluate_right(other, element)
    return Expression(_mul_expression)


def add_expression(expression_func, other) -> Expression:
    def _add_expression(element: dict):
        return expression_func(element) + evaluate_right(other, element)
    return Expression(_add_expression)
