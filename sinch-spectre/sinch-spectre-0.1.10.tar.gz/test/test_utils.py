import pytest
from spectre.generation import utils

@pytest.fixture
def operator_spec_path():
    return 'test/data/Operator.spec'

def test_read_entities(operator_spec_path):
    entities = utils.read_entities(operator_spec_path)
    assert len(entities) == 1
    assert entities[0].name == 'Operator'


def test_to_pascal():
    assert utils.to_pascal('a_var_in_snake_case') == 'AVarInSnakeCase'
    assert utils.to_pascal('myTestVar') == 'MyTestVar'
    assert utils.to_pascal('MyTestVar') == 'MyTestVar'
    assert utils.to_pascal('id') == 'Id'
    assert utils.to_pascal('i') == 'I'
    assert utils.to_pascal('') == ''

def test_is_camel():
    assert utils.is_camel('') == False
    assert utils.is_camel('i') == True
    assert utils.is_camel('I') == False
    assert utils.is_camel('ID') == False
    assert utils.is_camel('id') == True
    assert utils.is_camel('aCamelCaseVar') == True
    assert utils.is_camel('aCCVar') == True
    assert utils.is_camel('APCVar') == False
    assert utils.is_camel('APascalCaseVar') == False
    assert utils.is_camel('a_snake_case_var') == False

def test_is_pascal():
    assert utils.is_pascal('') == False
    assert utils.is_pascal('i') == False
    assert utils.is_pascal('I') == True
    assert utils.is_pascal('i') == False
    assert utils.is_pascal('ID') == True
    assert utils.is_pascal('Id') == True
    assert utils.is_pascal('id') == False
    assert utils.is_pascal('aCamelCaseVar') == False
    assert utils.is_pascal('APascalCaseVar') == True
    assert utils.is_pascal('a_snake_case_var') == False
    assert utils.is_pascal('APCVarWithAcronym') == True
    assert utils.is_pascal('aCCVarWithAcronym') == False

def test_is_snake():
    assert utils.is_snake('i') == True
    assert utils.is_snake('I') == False
    assert utils.is_snake('ID') == False
    assert utils.is_snake('id') == True
    assert utils.is_snake('a_snake_case_var') == True
    assert utils.is_snake('NOT_a_Snake_case_var') == False

def test_to_camel():
    assert utils.to_camel('a_var_in_snake_case') == 'aVarInSnakeCase'
    assert utils.to_camel('myTestVar') == 'myTestVar'
    assert utils.to_camel('MyTestVar') == 'myTestVar'
    assert utils.to_camel('id') == 'id'
    assert utils.to_camel('i') == 'i'
    assert utils.to_camel('') == ''