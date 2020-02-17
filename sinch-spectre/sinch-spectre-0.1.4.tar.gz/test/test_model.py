import pytest, json
from spectre.model import Entity, SpectreType, Field, BadInputException
from spectre.generation import java
from spectre.config import Config

@pytest.fixture
def sample_fields():
    fields = [
        Field(name='string_field', type=SpectreType.STRING, description='A required field', required=True, default='default str val', example='AnExampleValue'),
        Field(name='id', type=SpectreType.UUID),
        Field(name='foo_int', type=SpectreType.INT),
        Field(name='important_date', type=SpectreType.DATETIME),
    ]
    return fields

@pytest.fixture
def entity(sample_fields):
    return Entity('test_entity', 'An entity used for testing the model', sample_fields)

@pytest.fixture
def config():
    output = Config()
    output.namespace = 'spectre.java.test'
    output.java_options = {
        'spring_data': True,
        'spring_web': True,
    }
    return output

def test_from_dict():
    json_str = '''
{
    "description": "An entity used for testing the model",
    "fields": [
        {
            "name": "string_field",
            "description": "A required field",
            "required": true,
            "default": "default str val",
            "example": "this better work",
            "type": "string"
        },
        {
            "name": "id",
            "type": "uuid"
        },
        {
            "name": "foo_int",
            "type": "int"
        },
        {
            "name": "important_date",
            "type": "datetime"
        }
    ]
}
'''
    json_dict = json.loads(json_str)
    ent = Entity.from_dict('test_entity', json_dict)
    assert ent.name == 'test_entity'
    assert len(ent.fields) == 4
    assert ent.fields[0].name == "string_field"
    assert ent.fields[0].description == "A required field"
    assert ent.fields[0].required == True
    assert ent.fields[0].default == "default str val"
    assert ent.fields[0].example == "this better work"
    assert ent.fields[0].type is SpectreType.STRING
    assert ent.fields[3].type == SpectreType.DATETIME
    print('lol')

def test_validation():
    json_str = '''
{
    "description": "An entity used for testing the model",
    "fields": [
        {
            "name": "string_field",
            "description": 1,
            "type": "string"
        }
    ]
}
'''
    json_dict = json.loads(json_str)
    with pytest.raises(BadInputException):
        ent = Entity.from_dict('test_entity', json_dict)

def test_type_validation():
    json_str = '''
{
    "description": "An entity used for testing the model",
    "fields": [
        {
            "name": "string_field",
            "type": "this is not a type"
        }
    ]
}
'''
    json_dict = json.loads(json_str)
    with pytest.raises(BadInputException):
        ent = Entity.from_dict('test_entity', json_dict)
        pass


def test_to_json(entity):
    output = entity.to_json()
    assert '"test_entity": {' in output
    assert '"description": "An entity used for testing the model",' in output
    assert '"fields": [' in output
    assert '"name": "string_field",'
    assert '"description": "A required field",'
    assert '"required": true,' in output
    assert '"default": "default str val",' in output
    assert '"example": "AnExampleValue",' in output
    assert '"type": "string"' in output
    #Don't print empty fields such as description
    assert 'description: ""' not in output
    assert True