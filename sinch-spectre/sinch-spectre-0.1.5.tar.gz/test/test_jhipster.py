import pytest
from spectre.model import Entity, SpectreType, Field
from builtins import any
from spectre.generation import jhipster
from spectre.config import Config

@pytest.fixture
def sample_fields():
    fields = [
        Field(name='stringField', type=SpectreType.STRING, description='A required field', required=True, default='default str val', example='AnExampleValue'),
        Field(name='id', type=SpectreType.UUID),
        Field(name='fooInt', type=SpectreType.INT),
        Field(name='barTimestamp', type=SpectreType.DATETIME),
    ]
    return fields

@pytest.fixture
def entity(sample_fields):
    return Entity('TestEntity', 'An entity used for testing jhipster generation', sample_fields)

@pytest.fixture
def config():
    output = Config()
    output.namespace = 'spectre.java.test'
    output.java_options = {
        'spring_data': True,
        'spring_web': True,
    }
    return output

def string_in_collection(string, collection):
    return any(string in str for str in collection)

def test_generate_entity(entity, config):
    output = jhipster.generate_entity(entity)
    assert string_in_collection('entity TestEntity {', output)
    assert string_in_collection('stringField String', output)
    assert string_in_collection('id UUID', output)
    assert string_in_collection('fooInt Integer', output)
    assert string_in_collection('barTimestamp Instant', output)