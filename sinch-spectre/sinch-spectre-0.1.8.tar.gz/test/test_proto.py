import pytest
from spectre.model import Entity, SpectreType, Field
from builtins import any
from spectre.generation import proto
from spectre.config import Config

@pytest.fixture
def entities():
    foo = Entity('Foo', 'An entity used for testing proto generation', [
        Field(name='stringField', type=SpectreType.STRING, description='A required field', required=True, default='default str val', example='AnExampleValue'),
        Field(name='id', type=SpectreType.UUID),
        Field(name='fooInt', type=SpectreType.INT),
        Field(name='barTimestamp', type=SpectreType.DATETIME),
    ])
    bar = Entity('Bar', 'Another entity used for testing proto generation', [
        Field(name='float_field', type=SpectreType.FLOAT, description='A required field', required=True, default=0.172, example='AnExampleValue'),
        Field(name='int_field', type=SpectreType.INT),
        Field(name='undefined_field', type=SpectreType.UNDEFINED),
    ])
    return [ foo, bar ]

@pytest.fixture
def config():
    output = Config()
    output.namespace = 'spectre.java.test'
    output.java_options = {
        'spring_data': True,
        'spring_web': True,
    }
    output.name = 'FooBar'
    return output

def string_in_collection(string, collection):
    return any(string in str for str in collection)

def test_generate_header(config):
    header = proto.create_header(config)
    assert string_in_collection('syntax = "proto3";', header)
    assert string_in_collection('import "google/protobuf/struct.proto";', header)
    assert string_in_collection('package spectre.java.test.foobar;', header)

def test_generate_services(entities, config):
    services = proto.create_services(entities)
    pass
    #Check both services are present
    assert string_in_collection('service FooService {', services)
    assert string_in_collection('service BarService {', services)
    #TODO: When proto generator is refactored to use standard methods from config, make sure the corresponding methods are present in the services as well

#Doesnt verify the entire content or the exact format. Just a sanity check that things are working roughly as intended
def test_generate_messages(entities, config):
    messages = proto.create_messages(entities)
    #Check both entities are present
    assert string_in_collection('message Foo {', messages)
    assert string_in_collection('message Bar {', messages)
    #Check string default value is formatted properly with quotes
    assert string_in_collection('string stringField = 1 [default = "default str val"];', messages)
    #check int type is properly formatted
    assert string_in_collection('int32 fooInt = 3;', messages)
    #check timestamp type
    assert string_in_collection('Timestamp barTimestamp = 4;', messages)
    #check float default values
    assert string_in_collection('double float_field = 1 [default = 0.172];', messages)
