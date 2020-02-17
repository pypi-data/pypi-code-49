import copy
import re
from spectre.generation.utils import make_form, get_form_name, to_pascal, write_to_file, read_entities
from spectre.model import Entity, Field, SpectreType, UnknownTypeException
from spectre.config import Config

def write(content, config):
    outfile = f"proto/{config.name}.proto"
    write_to_file(content, outfile, config)

def generate(config: Config, path):
    entities = read_entities(path)
    output = generate_proto(entities, config)
    write('\n'.join(output), config)

def generate_proto(entities, config: Config):
    output = []
    output.extend(create_header(config))
    #Empty line for space
    output.append('')
    output.extend(create_services(entities))
    output.append('')
    output.extend(create_messages(entities))
    return output

def create_header(config):
    name = config.name
    output = [
        'syntax = "proto3";',
        '',
        'import "google/protobuf/struct.proto";',
        '',
        'option java_multiple_files = true;',
        f'option java_package = "{config.namespace}.{name}.grpc";'.lower(),
        'option java_outer_classname = "Grpc";',
        '',
        f'package {config.namespace}.{name};'.lower(),
        '',
    ]
    return output

def create_messages(entities):

    def create_message(entity):
        OUTPUT = ['message ' + to_pascal(entity.name) + ' {']
        FIELD_COUNTER = 1
        def add(addition):
            OUTPUT.append('\t' + addition)

        def make_default(val, t: SpectreType):
            if t is SpectreType.STRING:
                return f'"{val}"'
            else: 
                return val

        def make_field(field: Field):
            field_type = convert_type(field.type)
            field_name = field.name
            #TODO: Implement support for repeated types in spectre typing and here
            rep = False
            repeated = 'repeated ' if rep else ''
            default_val = field.default
            #Don't set default value for required fields
            default = f' [default = {make_default(default_val, field.type)}]' if default_val else ''
            nonlocal FIELD_COUNTER
            output = f'{repeated}{field_type} {field_name} = {FIELD_COUNTER}{default};'
            FIELD_COUNTER += 1
            return output

        for field in entity.fields:
            add(make_field(field))

        OUTPUT.append('}')
        return OUTPUT
    
    output = []

    messages = copy.deepcopy(entities)

    for entity in entities:
        messages.append(make_form(entity))

    for msg in messages:
        output.extend(create_message(msg))
        output.append('')
    return output

def convert_type(t: SpectreType):
    if t is SpectreType.INT: return 'int32'
    if t is SpectreType.UUID: return 'string'
    if t is SpectreType.STRING: return 'string'
    if t is SpectreType.FLOAT: return 'double'
    if t is SpectreType.ENUM: return 'enum'
    if t is SpectreType.UNDEFINED: return 'TYPE UNDEFINED'
    if t is SpectreType.DATETIME: return 'Timestamp'
    raise UnknownTypeException(f'Proto generator does not support type {t.name}')

def create_services(entities):

    def make_crud(name):
        OUTPUT = []

        def add(addition):
            OUTPUT.append(f'\trpc {addition};')

        add(f'create({to_pascal(get_form_name(name))}) returns ({name})')
        add(f'retrieve({name}) returns ({name})')
        add(f'update({name}) returns ({name})')
        #No delete for now
        #add(f'delete({name}) returns (statusPlaceholderType)')
        return OUTPUT

    def create_service(entity):
        name = to_pascal(entity.name)
        service = [f'service {name}Service {{']
        service.extend(make_crud(name))
        service.append('}')
        return service

    services = []

    for entity in entities:
        services.extend(create_service(entity))
    return services
