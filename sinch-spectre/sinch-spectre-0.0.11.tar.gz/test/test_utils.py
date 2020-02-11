import pytest
from spectre.generation import utils

@pytest.fixture
def operator_spec_path():
    return 'test/data/Operator.spec'

def test_read_entities(operator_spec_path):
    entities = utils.read_entities(operator_spec_path)
    assert len(entities) == 1
    assert entities[0].name == 'Operator'