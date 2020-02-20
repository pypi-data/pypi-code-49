from typing import List, Callable, Optional, Union, Type

import yaml
from apispec import BasePlugin, APISpec
from starlette.applications import Starlette
from starlette.schemas import BaseSchemaGenerator, EndpointInfo


def extract_status_code(
    status_code_or_exception: Union[int, Type[Exception]], handler_component: dict
) -> (Optional[int], dict):
    """
    Extract the status code from the status code if provided as key.
    Otherwise try to extract it from the handler_component as the single key of the dictionary
    """
    if isinstance(status_code_or_exception, int):
        return status_code_or_exception, handler_component

    if len(handler_component) == 1:
        first_key = list(handler_component)[0]
        if isinstance(first_key, int):
            return first_key, handler_component[first_key]

    return None, None


class StarlettePlugin(BasePlugin):
    """
    All registered Starlette exception handlers will be documented as possible responses if:
        * The exception handler contains a YAML docstring describing the content of the response.
        * A status code is provided, either as the key when registering the exception handler or as the single key
        in the YAML docstring of the handler.
    """

    def __init__(self, app: Starlette):
        self.operations = {}
        self.generator = BaseSchemaGenerator()
        self.app = app

    def init_spec(self, spec: APISpec):
        # TODO Document error 500

        # Document all responses that can occur in case of an error
        for status_code_or_exception, handler in self.app.exception_handlers.items():
            handler_component = self.generator.parse_docstring(handler)
            status_code, handler_component = extract_status_code(
                status_code_or_exception, handler_component
            )
            if status_code and handler_component:
                spec.components.schema(
                    name=f"Error{status_code}", component=handler_component
                )
                spec.components.response(
                    status_code,
                    {"schema": {"$ref": f"#/definitions/Error{status_code}"}},
                )

    def endpoints(self) -> List[EndpointInfo]:
        return self.generator.get_endpoints(self.app.routes)

    def path_helper(
        self,
        path=None,
        operations=None,
        parameters=None,
        endpoint: EndpointInfo = None,
        **kwargs,
    ):
        # TODO Handle consumes and produces
        if endpoint is None:
            # Save operations to merge it when processing endpoints
            if operations and path:
                for method, operation in operations.items():
                    previous_operation = self.operations.setdefault(
                        path, {}
                    ).setdefault(method, {})
                    merge_dict(previous_operation, operation)
            return

        default_operation = {
            "operationId": f"{endpoint.http_method.lower()}_{endpoint.func.__name__}"
        }

        summary = self._summary(endpoint.func)
        if summary:
            default_operation["summary"] = summary

        # Allow to override auto generated documentation
        default_operation.update(self.generator.parse_docstring(endpoint.func))
        operations[endpoint.http_method] = default_operation
        merge_dict(
            default_operation,
            self.operations.get(path, {}).get(endpoint.http_method.lower(), {}),
        )

    def _summary(self, func_or_method: Callable) -> Optional[str]:
        """
        Given a function, parse the docstring and return it as a string if this is not YAML.
        """
        docstring = func_or_method.__doc__
        if not docstring:
            return

        # We support having regular docstrings before the schema
        # definition. Here we return just the schema part from
        # the docstring.
        docstring = docstring.split("---")[0]

        parsed = yaml.safe_load(docstring)

        if isinstance(parsed, dict):
            return

        return parsed


def merge_dict(previous: dict, new: dict):
    for previous_key, previous_value in previous.items():
        if isinstance(previous_value, dict):
            previous_value.update(new.pop(previous_key, {}))
    previous.update(new)
