"""
Input prompts to request data from users.
"""
import os
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Type

from qwikstart import utils
from qwikstart.exceptions import UserFacingError

from . import input_types


@dataclass
class PromptSpec:
    """Data class used to specify input prompts."""

    name: str
    default: Optional[Any] = None
    choices: Optional[List[Any]] = None
    input_type: Type[input_types.InputType[Any]] = input_types.StringInput
    input_config: Dict[str, Any] = field(default_factory=dict)


def create_prompt_spec(**prompt_kwargs: Any) -> PromptSpec:
    """Return PromptSpec instance from attributes in dictionary.

    This raises a UserFacingError if the PromptSpec is incorrectly defined.
    """
    # FIXME: Remove in v0.5; Support default_value for backwards compatibility
    if "default_value" in prompt_kwargs:
        prompt_kwargs["default"] = prompt_kwargs.pop("default_value")

    name = prompt_kwargs.get("name")
    if not name:
        msg = f"PromptSpec definition has no 'name': {prompt_kwargs}"
        raise UserFacingError(msg)

    param_type = get_param_type(**prompt_kwargs)
    # Remove "type" (used by `get_param_type`) to avoid unknown key error:
    prompt_kwargs.pop("type", None)
    try:
        return PromptSpec(input_type=param_type, **prompt_kwargs)
    except TypeError as error:
        known_keys = utils.get_dataclass_keys(PromptSpec)
        unknown_keys = set(prompt_kwargs.keys()).difference(known_keys)
        if unknown_keys:
            msg = f"PromptSpec definition for {name!r} has unknown keys: {unknown_keys}"
            raise UserFacingError(msg) from error
        raise


_PROMPT_TYPE_MAPPING = {
    "bool": input_types.BoolInput,
    bool: input_types.BoolInput,
    "int": input_types.IntegerInput,
    int: input_types.IntegerInput,
    "path": input_types.PathInput,
}


def get_param_type(**prompt_kwargs: Any) -> Type[input_types.InputType[Any]]:
    name = prompt_kwargs["name"]
    explicit_type = prompt_kwargs.get("type")
    if explicit_type:
        if isinstance(explicit_type, str):
            explicit_type = explicit_type.lower()
        if explicit_type not in _PROMPT_TYPE_MAPPING:
            raise UserFacingError(f"Unknown type {explicit_type!r} for prompt {name}")
        return _PROMPT_TYPE_MAPPING[explicit_type]

    default_type = type(prompt_kwargs.get("default"))
    if default_type in _PROMPT_TYPE_MAPPING:
        return _PROMPT_TYPE_MAPPING[default_type]

    return input_types.StringInput


def read_user_variable(prompt_spec: PromptSpec) -> Any:
    """Prompt user for variable and return the entered value or given default.

    Adapted from `cookiecutter.prompt`
    (see https://github.com/cookiecutter/cookiecutter).

    For more info, see https://click.palletsprojects.com/en/7.x/api/#click.prompt
    """
    if prompt_spec.choices:
        return read_user_choice(prompt_spec)

    input_type = prompt_spec.input_type(**prompt_spec.input_config)
    # Cannot pass `default=None` in some cases due to autocompletion.
    if prompt_spec.default is None:
        return input_type.prompt(prompt_spec.name)
    return input_type.prompt(prompt_spec.name, default=prompt_spec.default)


def read_user_choice(prompt_spec: PromptSpec) -> Any:
    """Prompt user to choose from several options for the given variable.

    The first item will be returned if no input provided.

    Adapted from `cookiecutter.prompt`
    (see https://github.com/cookiecutter/cookiecutter).
    """
    choices = prompt_spec.choices
    if not isinstance(choices, list):
        msg = f"Choices for prompt must be list but given {type(choices)}: {choices!r}"
        raise UserFacingError(msg)

    if not choices:
        raise UserFacingError("Choices for prompt cannot be empty")

    choice_map = {"{}".format(i): value for i, value in enumerate(choices, 1)}
    numeric_choices = choice_map.keys()

    choice_lines = ["{} - {}".format(*c) for c in choice_map.items()]
    display = os.linesep.join(
        (
            "Select {}:".format(prompt_spec.name),
            os.linesep.join(choice_lines),
            "Choose from {}".format(", ".join(numeric_choices)),
        )
    )

    input_type = input_types.NumberRange(1, len(choices))
    user_choice = input_type.raw_prompt(display)
    return choice_map[user_choice]
