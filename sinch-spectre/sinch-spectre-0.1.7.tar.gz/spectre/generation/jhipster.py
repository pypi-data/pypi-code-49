from spectre.generation import utils
from spectre.config import Config
from spectre.model import Entity, Field, SpectreType, UnknownTypeException

def generate(config: Config, path):
    spectre_entities = utils.read_entities(path)
    written = []
    for ent in spectre_entities:
        jhip_entity = generate_entity(ent)
        written.append(write_entity(ent.name, jhip_entity, config))
    return written

def write_entity(name, entity, config):
    return utils.write_to_file("\n".join(entity), f'jhipster/{name}.jdl', config)

def convert_type(t: SpectreType, name):

    int_type = 'Integer'
    string_type = 'String'
    timestamp_type = 'Instant'
    float_type = 'Double'
    id_type = 'UUID'
    enum_type = 'Enumeration'
    
    if t is SpectreType.INT: return int_type
    if t is SpectreType.STRING: return string_type
    if t is SpectreType.DATETIME: return timestamp_type
    if t is SpectreType.FLOAT: return float_type
    if t is SpectreType.UUID: return id_type
    if t is SpectreType.ENUM: return enum_type
    raise UnknownTypeException(f'{t.name} not supported by jhipster generator')

def generate_entity(entity):
    output = [f'entity {utils.to_pascal(entity.name)} {{']
    for field in entity.fields:
        field_name = field.name
        member = f'\t{field_name} {convert_type(field.type, field_name)}'
        output.append(member)
    output.append('}')
    return output