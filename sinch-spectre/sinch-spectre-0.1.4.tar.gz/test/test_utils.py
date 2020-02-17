import pytest
from spectre.generation import utils

@pytest.fixture
def operator_spec_path():
    return 'test/data/Operator.spec'

def test_read_entities(operator_spec_path):
    entities = utils.read_entities(operator_spec_path)
    assert len(entities) == 1
    assert entities[0].name == 'Operator'

@pytest.fixture
def snake_case():
    return [
        'var_in_snake_case',
        'Var_In_Snake_Case',
        'vaR_IN_snaKe_caSE'
    ]

def test_to_pascal(snake_case):
    for var in snake_case:
        pass