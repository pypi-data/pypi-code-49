"""
Low-level input types using `prompt_toolkit` to request input.

Higher-level functionality should be put in `prompt` module.
"""
import abc
import logging
from typing import Any, Generic, Optional, TypeVar, cast

from prompt_toolkit import prompt as ptk_prompt
from prompt_toolkit.completion import Completer, PathCompleter
from prompt_toolkit.validation import Validator

logger = logging.getLogger(__name__)

T = TypeVar("T", covariant=True)


class InputType(Generic[T]):

    error_msg: str = "Input does not pass validation"
    completer: Optional[Completer] = None
    default_prefix: str = ": "

    def __init__(self, **kwargs: Any):
        if kwargs:
            logger.warning(
                "Unknown keyword arguments for %s: %s",
                self.__class__.__name__,
                ", ".join(kwargs.keys()),
            )

    @property
    def validator(self) -> Validator:
        return Validator.from_callable(self.is_valid, error_message=self.error_msg)

    @abc.abstractmethod
    def is_valid(self, text: str) -> bool:
        pass  # pragma: no cover

    def cast(self, input_text: str) -> T:
        return cast(T, input_text)

    def raw_prompt(
        self, message: str, suffix: Optional[str] = None, **prompt_kwargs: Any
    ) -> str:
        if suffix is None:
            suffix = self.default_prefix
        return ptk_prompt(  # type: ignore
            message + suffix,
            completer=self.completer,
            validator=self.validator,
            **prompt_kwargs,
        )

    def prompt(self, message: str, **prompt_kwargs: Any) -> T:
        value = self.raw_prompt(message, **prompt_kwargs)
        return self.cast(value)


class IntegerInput(InputType[int]):
    def is_valid(self, text: str) -> bool:
        try:
            self.cast(text)
        except ValueError:
            return False
        return True

    def cast(self, input_text: str) -> int:
        return int(input_text)

    def raw_prompt(
        self, message: str, suffix: Optional[str] = None, **prompt_kwargs: Any
    ) -> str:
        default = prompt_kwargs.get("default")
        if isinstance(default, int):
            prompt_kwargs["default"] = str(default)
        return super().raw_prompt(message, suffix=suffix, **prompt_kwargs)


class NumberRange(IntegerInput):
    def __init__(self, min_value: int, max_value: int, **kwargs: Any):
        super().__init__(**kwargs)
        self.min = min_value
        self.max = max_value
        self.error_msg = f"This input must be number between {self.min} and {self.max}"

    def is_valid(self, text: str) -> bool:
        try:
            number = self.cast(text)
        except ValueError:
            return False
        return self.min <= number <= self.max


class StringInput(InputType[str]):
    error_msg: str = "Input cannot be empty"

    def __init__(self, allow_empty: bool = False, **kwargs: Any):
        super().__init__(**kwargs)
        self.allow_empty = allow_empty

    def is_valid(self, text: str) -> bool:
        return bool(text.strip() or self.allow_empty)


class PathInput(StringInput):
    completer = PathCompleter()


class BoolInput(InputType[bool]):
    error_msg: str = "Response must be 'y' or 'n'"
    default_prefix: str = " (y/n): "

    def raw_prompt(
        self, message: str, suffix: Optional[str] = None, **prompt_kwargs: Any
    ) -> str:
        default = prompt_kwargs.get("default")
        if isinstance(default, bool):
            prompt_kwargs["default"] = "y" if default else "n"
        return super().raw_prompt(message, suffix=suffix, **prompt_kwargs)

    def is_valid(self, text: str) -> bool:
        return text.lower() in ("y", "n")

    def cast(self, input_text: str) -> bool:
        return input_text.lower() == "y"
