import logging
import textwrap
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Type

from ..base_context import BaseContext, DictContext, TContext
from ..utils.prompt import create_prompt_spec, read_user_variable
from ..utils.templates import DEFAULT_TEMPLATE_VARIABLE_PREFIX, TemplateRenderer
from .base import BaseOperation

__all__ = ["Operation"]

logger = logging.getLogger(__name__)

DEFAULT_INTRO = "Please enter the following information:"

CONTEXT_HELP = {
    "inputs": textwrap.dedent(
        """
            List of dictionaries describing prompts for user inputs.
            Dictionary have the following keys:
                - name: The name of the variable being defined.
                - default: Optional default value of variable. Note that this
                  can be defined as a template string, with variables defined in
                  previous prompts or from template variables in the context; e.g.:

                    - name: "name"
                      default: "World"
                    - name: "message"
                      default: "Hello {{ name }}!"
        """
    )
}

# Output will be dict with single key, `Context.output_dict_name`, and dict
# value w/ keys defined by `Context.prompts` mapping to user responses.
Output = Dict[str, Dict[str, Any]]


@dataclass(frozen=True)
class Context(BaseContext):
    inputs: List[Dict[str, Any]]
    output_dict_name: str = "template_variables"
    introduction: str = DEFAULT_INTRO
    template_variables: Dict[str, Any] = field(default_factory=dict)
    template_variable_prefix: str = DEFAULT_TEMPLATE_VARIABLE_PREFIX

    @classmethod
    def help(cls, field_name: str) -> Optional[str]:
        return CONTEXT_HELP.get(field_name)

    @classmethod
    def from_dict(cls: Type[TContext], field_dict: DictContext) -> TContext:
        # FIXME: Remove in v0.5; Support "prompts" for backwards compatibility
        if "prompts" in field_dict:
            field_dict = {
                "inputs": field_dict["prompts"],
                **{k: v for k, v in field_dict.items() if k != "prompts"},
            }
        return super().from_dict(field_dict)  # type: ignore


class Operation(BaseOperation[Context, Output]):
    """Operation to prompt user for inputs."""

    name = "prompt"
    aliases = ["prompt_user"]

    def run(self, context: Context) -> Output:

        introduction = context.introduction
        logger.info(introduction)

        renderer = TemplateRenderer.from_context(context)
        user_responses = {}
        for input_description in context.inputs:
            prompt_spec = create_prompt_spec(**input_description)

            if isinstance(prompt_spec.default, str):
                prompt_spec.default = renderer.render_string(prompt_spec.default)

            response = read_user_variable(prompt_spec)
            user_responses[prompt_spec.name] = response
            # Ensure that templates used for defaults can use the new variable.
            renderer.add_template_variable(prompt_spec.name, response)

        output_name = context.output_dict_name
        logger.debug(f"Responses recorded to {output_name}:")
        logger.debug(
            "\t"
            + "\n\t".join(f"{key}: {value!r}" for key, value in user_responses.items())
        )

        return {output_name: user_responses}
