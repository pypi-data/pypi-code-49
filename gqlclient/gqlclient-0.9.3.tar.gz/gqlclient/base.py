"""
Base class to support the creation of graphql queries and mutations.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
import datetime
import json
import logging
from typing import Any, Callable, Dict, Optional, Union

from gqlclient.exceptions import GraphQLException, ModelException

try:
    from typing import get_origin  # get_origin is available in 3.8+
except ImportError:
    from typing import _GenericAlias, Generic

    def get_origin(tp):
        """
        This function is copied directly without modification from the CPython 3.8.0
        source code and is Licensed under PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2

        Get the unsubscripted version of a type.
        This supports generic types, Callable, Tuple, Union, Literal, Final and ClassVar.
        Return None for unsupported types. Examples::
            get_origin(Literal[42]) is Literal
            get_origin(int) is None
            get_origin(ClassVar[int]) is ClassVar
            get_origin(Generic) is Generic
            get_origin(Generic[T]) is Generic
            get_origin(Union[T, int]) is Union
            get_origin(List[Tuple[T, T]][int]) == list
        """
        if isinstance(tp, _GenericAlias):
            return tp.__origin__
        if tp is Generic:
            return Generic
        return None


from gqlclient.response_encoders import dataclass_encoder


__all__ = ["GraphQLClientBase"]


logger = logging.getLogger(__name__)


class DatetimeEncoder(json.JSONEncoder):
    """
    A JSON encoder which encodes datetimes as iso formatted strings.
    """

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat("T")
        return super().default(obj)


@dataclass
class DefaultParameters:
    """
    Default parameter object that will pass dataclass type checking
    """


class GraphQLClientBase(ABC):
    """
    Abstract class for formatting and executing GraphQL queries and mutations

    :param gql_uri: Fully qualified URI for the graphQL endpoint.
    """

    def __init__(
        self,
        gql_uri: str,
        default_response_encoder: Optional[Callable[[str, dict, type], Any]] = dataclass_encoder,
    ):
        """
        Base constructor for the Graphql client
        :param gql_uri: URI for the graphql endpoint
        :param default_response_encoder: Optional default encoder for graphql responses.  e.g. dataclass_encoder
        """
        self.gql_uri = gql_uri
        self.default_response_encoder = default_response_encoder

    @staticmethod
    def _graphql_response_from_model(model_cls: type) -> str:
        """
        Generate a GraphQL Response query from the class for the response.

        :param model_cls: Dataclass type representing the desired response object from the graphql endpoint.

        :return: Portion of a graphql query which specifies the response object.
        """
        if not hasattr(model_cls, "__dataclass_fields__"):
            raise ModelException("Response model must be a dataclass")

        def parse_field(field):
            origin = get_origin(field.type)
            if origin is not None and issubclass(
                origin, list
            ):  # Treat lists of dataclasses like a dataclass
                field_type = field.type.__args__[0]
            else:
                field_type = field.type
            if hasattr(field_type, "__dataclass_fields__"):
                return (
                    field.name,
                    [parse_field(sfield) for sfield in field_type.__dataclass_fields__.values()],
                )
            else:
                return field.name

        def unpack(name: list):
            if not isinstance(name, tuple):
                return name
            return f"{name[0]} {{ {' '.join([unpack(n) for n in name[1]])} }}"

        names = [parse_field(f) for f in model_cls.__dataclass_fields__.values()]
        names = [unpack(name) for name in names]
        return ", ".join(names)

    @staticmethod
    def _graphql_query_parameters_from_model(model: object) -> str:
        """
        Generate a GraphQL query parameters from the class for the query.

        :param model: Dataclass instance representing the query parameters and actual search values (min 1)python

        :return: Portion of a graphql query which specifies the query parameters
        """

        if not hasattr(model, "__dataclass_fields__"):
            raise ModelException("Parameter model must be a dataclass")

        # Only create query parameters for those with values using graphql syntax mask for the query parameters
        parameters = ", ".join(
            [
                f"{field.name}: {json.dumps(getattr(model, field.name), cls=DatetimeEncoder)}"
                for field in model.__dataclass_fields__.values()
                if getattr(model, field.name) is not None
            ]
        )
        return parameters

    def get_query(
        self,
        query_base: str,
        query_response_cls: type,
        query_parameters: Optional[object] = DefaultParameters,
    ) -> Dict[str, str]:
        """
        Create a GraphQL formatted query string.

        :param query_base: Name of the root type to be queried
        :param query_response_cls: A dataclass model class representing the structure of the response object
        with attributes  corresponding to the Graphql type and attribute names
        :param query_parameters: Optional. Instance of a dataclass model containing attributes corresponding
        to parameter names and values corresponding to the parameter value.

        :return: Dictionary that can be passed as json to the GraphQL API endpoint
        """

        # Construct graphql query
        gql_query = query_base
        parameters = self._graphql_query_parameters_from_model(query_parameters)
        if parameters:
            gql_query += f"({parameters})"

        gql_query += f"{{{self._graphql_response_from_model(query_response_cls)}}}"
        return {"query": f"{{{gql_query} }}"}

    def get_mutation(
        self,
        mutation_base: str,
        mutation_parameters: object,
        mutation_response_cls: Optional[type] = None,
    ) -> Dict[str, str]:
        """
        Create a GraphQL formatted mutation string.

        :param mutation_base: Name of the root type to be mutated
        :param mutation_parameters: Instance of a dataclass model containing attributes corresponding to
        parameter names and values corresponding to the parameter value.
        :param mutation_response_cls: Optional. A dataclass model class representing the structure of the
        response object with attributes corresponding to the Graphql type and attribute names.

        :return: Dictionary that can be passed as json to the GraphQL API endpoint
        """

        # Construct graphql mutation
        gql_mutation = (
            f"mutation {mutation_base} {{{mutation_base}"
            f"({self._graphql_query_parameters_from_model(mutation_parameters)}){{ok"
        )
        if mutation_response_cls:
            gql_mutation += f", {self._graphql_response_from_model(mutation_response_cls)}"
        gql_mutation += "}"

        return {"query": f"{gql_mutation} }}", "operationName": mutation_base}

    @abstractmethod
    def execute_gql_call(self, query: dict) -> dict:
        """
        Executes a GraphQL query or mutation.

        :param query: Dictionary formatted graphql query

        :return: Dictionary containing the response from the GraphQL endpoint
        """

    def _format_response(
        self, query_base: str, response_cls, result: dict, response_encoder: Union[Callable, None]
    ):
        """
        Helper function to format the graphql response using a provided encoder
        :param result: Graphql Response to format
        :param response_encoder: Encoder to use in formatting
        :return:
        """
        if response_encoder is None:  # Use the default encoder from the instance
            response_encoder = self.default_response_encoder
        if "errors" in result:
            raise GraphQLException(errors=result["errors"])
        if response_encoder is None:
            return result["data"]  # dict return
        else:
            return response_encoder(query_base, result["data"], response_cls)

    def execute_gql_query(
        self,
        query_base: str,
        query_response_cls: type,
        query_parameters: Optional[object] = DefaultParameters,
        response_encoder: Optional[Callable[[str, dict, type], Any]] = None,
    ) -> Any:
        """
        Executes a graphql query based upon input dataclass models.

        :param query_base: Name of the root type to be queried
        :param query_parameters: Optional. Instance of a dataclass model containing attributes corresponding to
        parameter names and values corresponding to the parameter value.
        :param query_response_cls: A dataclass model class representing the structure of the response
        object with attributes corresponding to the Graphql type and attribute names
        :param response_encoder: A callable which takes a dict graphql response and returns a reformatted type

        :return: The response formatted by the specified response_encoder.  Default is dict if no encoder is specified
        """
        query = self.get_query(query_base, query_response_cls, query_parameters)
        result = self.execute_gql_call(query)
        return self._format_response(query_base, query_response_cls, result, response_encoder)

    def execute_gql_mutation(
        self,
        mutation_base: str,
        mutation_parameters: object,
        mutation_response_cls: Optional[type] = None,
        response_encoder: Optional[Callable[[str, dict, type], Any]] = None,
    ) -> Any:
        """
        Executes a graphql mutation based upon input dataclass models.

        :param mutation_base: Name of the root type to be mutated
        :param mutation_parameters: Instance of a dataclass model containing attributes corresponding to
        parameter names and values corresponding to the parameter value.
        :param mutation_response_cls: Optional. A dataclass model class representing the structure of the
        response object with attributes corresponding to the Graphql type and attribute names.
        :param response_encoder: A callable which takes the following arguments:
            str for the base type call e.g. query_base or mutation_base
            dict for the data returned in under the 'data' key
            type for the dataclass that structured the response

        :return: The response formatted by the specified response_encoder.  Default is dict if no encoder is specified
        """
        mutation = self.get_mutation(mutation_base, mutation_parameters, mutation_response_cls)
        result = self.execute_gql_call(mutation)
        return self._format_response(mutation_base, mutation_response_cls, result, response_encoder)

    def __str__(self):
        return f"GraphQLClient(gql_uri={self.gql_uri}, default_response_encoder={self.default_response_encoder})"

    def __repr__(self):
        return str(self)
