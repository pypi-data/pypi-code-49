import os
import json

from schema_registry.client import SchemaRegistryClient, schema
from schema_registry.serializers import FaustSerializer


def get_avro_client() -> SchemaRegistryClient:
    """
    Configures a client for the schema registry using an environment variable
    :return: (SchemaRegistryClient)
    """
    return SchemaRegistryClient(url=os.environ['SCHEMA_REGISTRY_URL'])


def parse_schema(file_loc):
    with open(file_loc, 'r') as f:
        avro_schema = schema.AvroSchema(json.dumps(json.load(f)))
    return avro_schema


def key_serializer(client) -> FaustSerializer:
    """
    Creates Faust Serializer for generic string schema
    """
    return FaustSerializer(schema_registry_client=client,
                           schema_subject='generic_faust_avro_key',
                           schema=schema.AvroSchema('''{"type":"string"}'''),
                           is_key=True)


def value_serializer(client, topic, schema_json_fp):
    return FaustSerializer(schema_registry_client=client,
                           schema_subject=topic,
                           schema=parse_schema(schema_json_fp))