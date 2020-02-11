"""
Tests for the graphql_client library
"""

from datetime import datetime
from typing import List
from dataclasses import dataclass

from pydantic.dataclasses import dataclass as pydantic_dataclass
import pytest

from gqlclient import GraphQLClient
from gqlclient.exceptions import ModelException


# Dataclass defined test data
@dataclass
class DataclassParameters:
    str_param: str
    int_param: int
    float_param: float
    str_array_param: List[str]
    num_array_param: List[int]
    bool_param: bool
    date_param: datetime
    optional_param: int = None


@dataclass
class DataclassResponseChild:
    child_param_1: str
    child_param_2: str


@dataclass
class DataclassResponseParent:
    parent_param_1: str
    parent_param_2: str
    child_object: DataclassResponseChild


@dataclass
class DataclassResponseParentWithList:
    parent_param_1: str
    parent_param_2: str
    child_object: List[DataclassResponseChild]


# Pydantic dataclass defined test data
@pydantic_dataclass
class PydanticDataclassParameters:
    str_param: str
    int_param: int
    float_param: float
    str_array_param: List[str]
    num_array_param: List[int]
    bool_param: bool
    date_param: datetime
    optional_param: int = None


@pydantic_dataclass
class PydanticDataclassResponseChild:
    child_param_1: str
    child_param_2: str


@pydantic_dataclass
class PydanticDataclassResponseParent:
    parent_param_1: str
    parent_param_2: str
    child_object: PydanticDataclassResponseChild


class BadModel:
    def __init__(self):
        self.str_param = ("A",)
        self.int_param = (1,)
        self.float_param = (1.1,)
        self.str_array_param = (["A", "B"],)
        self.num_array_param = ([1, 2],)
        self.date_param = datetime.strptime("2010-03-25T14:08:00", "%Y-%m-%dT%H:%M:%S")


query_base = "query_base"
mutation_base = "mutation_base"

dataclass_parameters = DataclassParameters(
    str_param="A",
    int_param=1,
    float_param=1.1,
    str_array_param=["A", "B"],
    num_array_param=[1, 2],
    bool_param=False,
    date_param=datetime.strptime("2010-03-25T14:08:00", "%Y-%m-%dT%H:%M:%S"),
)

pydantic_dataclass_parameters = PydanticDataclassParameters(
    str_param="A",
    int_param=1,
    float_param=1.1,
    str_array_param=["A", "B"],
    num_array_param=[1, 2],
    bool_param=False,
    date_param=datetime.strptime("2010-03-25T14:08:00", "%Y-%m-%dT%H:%M:%S"),
)

bad_model = BadModel()

# Graphql Client to test
@pytest.fixture(scope="module")
def client():
    return GraphQLClient(gql_uri="http://localhost:5000/graphql")


@pytest.mark.parametrize(
    "query_base, parameters, response_cls",
    [
        (query_base, dataclass_parameters, DataclassResponseParent),
        (query_base, pydantic_dataclass_parameters, PydanticDataclassResponseParent),
        (query_base, dataclass_parameters, DataclassResponseParentWithList),
    ],
)
def test_query_string_with_parameters(client, query_base, parameters, response_cls):
    """
    Test of query string structure when parameter model is included

    :param client: Graphql Client instance

    :param query_base: Name of the query endpoint

    :param parameters: Instance of a dataclass containing the query parameter names and values

    :param response_cls: Dataclass containing the attributes of the graphql response

    :return: None
    """
    test_query = client.get_query(
        query_base=query_base, query_parameters=parameters, query_response_cls=response_cls
    )
    expected_result = {
        "query": '{query_base(str_param: "A", '
        "int_param: 1, "
        "float_param: 1.1, "
        'str_array_param: ["A", "B"], '
        "num_array_param: [1, 2], "
        "bool_param: false, "
        'date_param: "2010-03-25T14:08:00")'
        "{parent_param_1, parent_param_2, "
        "child_object { child_param_1 child_param_2 }"
        "} }"
    }
    assert test_query == expected_result


@pytest.mark.parametrize(
    "query_base, response_cls",
    [(query_base, DataclassResponseParent), (query_base, PydanticDataclassResponseParent)],
)
def test_query_string_without_parameters(client, query_base, response_cls):
    """
    Test of query string structure when parameter model is NOT included

    :param client: Graphql Client instance

    :param query_base: Name of the query endpoint

    :param response_cls: Dataclass containing the attributes of the graphql response

    :return: None
    """
    test_query = client.get_query(query_base=query_base, query_response_cls=response_cls)
    expected_result = {
        "query": "{query_base"
        "{parent_param_1, parent_param_2, "
        "child_object { child_param_1 child_param_2 }"
        "} }"
    }

    assert test_query == expected_result


@pytest.mark.parametrize(
    "mutation_base, parameters, response_cls",
    [
        (mutation_base, dataclass_parameters, DataclassResponseParent),
        (mutation_base, pydantic_dataclass_parameters, PydanticDataclassResponseParent),
    ],
)
def test_mutation_string_with_response(client, mutation_base, parameters, response_cls):
    """
    Test of mutation string structure when response model is included

    :param client: Graphql Client instance

    :param mutation_base: Name of the mutation endpoint

    :param parameters: Instance of a dataclass containing the mutation parameter names and values

    :param response_cls: Dataclass containing the attributes of the graphql response

    :return: None
    """
    test_mutation = client.get_mutation(
        mutation_base=mutation_base,
        mutation_response_cls=response_cls,
        mutation_parameters=parameters,
    )
    expected_result = {
        "query": "mutation mutation_base "
        '{mutation_base(str_param: "A", '
        "int_param: 1, "
        "float_param: 1.1, "
        'str_array_param: ["A", "B"], '
        "num_array_param: [1, 2], "
        "bool_param: false, "
        'date_param: "2010-03-25T14:08:00")'
        "{ok, "
        "parent_param_1, parent_param_2, child_object "
        "{ child_param_1 child_param_2 }} }",
        "operationName": "mutation_base",
    }

    assert test_mutation == expected_result


@pytest.mark.parametrize(
    "mutation_base, parameters",
    [(mutation_base, dataclass_parameters), (mutation_base, pydantic_dataclass_parameters)],
)
def test_mutation_string_without_response(client, mutation_base, parameters):
    """
    Test of mutation string structure when response model is NOT included

    :param client: Graphql Client instance

    :param mutation_base: Name of the mutation endpoint

    :param parameters: Instance of a dataclass containing the mutation parameter names and values

    :return: None
    """
    test_mutation = client.get_mutation(mutation_base=mutation_base, mutation_parameters=parameters)
    expected_result = {
        "query": "mutation mutation_base "
        '{mutation_base(str_param: "A", '
        "int_param: 1, float_param: 1.1, "
        'str_array_param: ["A", "B"], '
        "num_array_param: [1, 2], "
        "bool_param: false, "
        'date_param: "2010-03-25T14:08:00"){ok} }',
        "operationName": "mutation_base",
    }

    assert test_mutation == expected_result


@pytest.mark.parametrize(
    "response_model_cls, parameter_model", [(BadModel, None), (DataclassResponseParent, bad_model)]
)
def test_bad_model(client, response_model_cls, parameter_model):
    """
    Test of a non-dataclass object causing a ValueError

    :param client: Graphql Client instance

    :param response_model_cls: Object representing the graphql response

    :param parameter_model: Object representing the graphql parameters

    :return: None
    """

    with pytest.raises(ModelException):
        client.get_query(query_base, response_model_cls, parameter_model)


def test_query_with_empty_parameters(client):
    """
    Test query with a parameter object with all None attribute values

    :param client: Graphql Client instance

    :return:
    """

    empty_dataclass_parameters = DataclassParameters(
        str_param=None,
        int_param=None,
        float_param=None,
        str_array_param=None,
        num_array_param=None,
        bool_param=None,
        date_param=None,
    )

    test_query = client.get_query(
        query_base=query_base,
        query_parameters=empty_dataclass_parameters,
        query_response_cls=DataclassResponseParent,
    )
    expected_result = {
        "query": "{query_base"
        "{parent_param_1, parent_param_2, "
        "child_object { child_param_1 child_param_2 }"
        "} }"
    }

    assert test_query == expected_result


def test_three_layered_response(client):
    @dataclass
    class Grandchild:
        gchild_name: str

    @dataclass
    class Child:
        child_name: str
        grandchild: Grandchild

    @dataclass
    class Parent:
        parent_name: str
        child: Child

    test_query = client.get_query("threeLayerTest", Parent)

    expected_query = {
        "query": "{threeLayerTest"
        "{parent_name, "
        "child { child_name,  grandchild { gchild_name } }"
        "} }"
    }
