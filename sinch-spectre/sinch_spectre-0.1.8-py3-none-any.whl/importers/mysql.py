import re
from spectre.generation.serializer import to_json 
from spectre.generation.utils import write_to_file
from spectre.model import Entity, Field, SpectreType, UnknownTypeException

def import_mysql(config, path):
    with open(path, 'r') as file:
        name = re.sub(r'.*/', '', path)
        name = re.sub(r'\..*', '', name)
        entity = Entity(name)
        entity.description = f'Imported entity from mysql table {name}'
        text = file.readlines()
        fields = []
        for line in text:
            fields.append(to_field(line))
        entity.fields = fields
        out_path = f'{name}.spec'
        write_to_file(entity.to_json(), out_path, config)
        return out_path

def convert_type(t):
    t = re.sub(r'\(.*\)', '', t)
    t = t.replace(' unsigned', '')
    if t in [ 'smallint', 'int', 'mediumint', 'bigint', 'tinyint' ]:
        return SpectreType.INT
    if t in [ 'enum' ]:
        return SpectreType.ENUM
    if t in [ 'varchar', 'char' ]:
        return SpectreType.STRING
    if t in [ 'timestamp' ]:
        return SpectreType.DATETIME
    if t in [ 'binary' ]:
        #Not supported but expected, shouldn't crash
        return SpectreType.UNDEFINED
    try:
        return SpectreType[t.upper()]
    except:
        raise UnknownTypeException(f'Unsupported type: {t}')

def to_field(line):

    columns = line.split('\t')
    field = Field()
    field.name = columns[0]
    field.type = convert_type(columns[1])
    field.required = not 'YES' in columns[2]
    field.default = columns[4] if not 'NULL' in columns[4] else None
    field.validate()
    return field