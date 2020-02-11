from enum import Enum
import json
from dataclasses import dataclass, field, asdict
from typing import List, Any

class UnknownTypeException(Exception):
    pass

class BadInputException(Exception):
    pass

@dataclass
class SpectreType(Enum):
    INT = 0
    STRING = 1
    BOOL = 2
    FLOAT = 3
    ENUM = 4
    DATETIME = 5
    UUID = 6
    #UNDEFINED has to go last or it will mess up prompts and typing. Value does not matter, only relative position has to be last
    UNDEFINED = 7

@dataclass
class Field:
    name: str = None
    type: SpectreType = SpectreType.UNDEFINED
    description: str = None
    required: bool = False
    default: Any = None
    example: Any = None
    #TODO: Add and enforce validation

    def validate(self):
        pass

    @staticmethod
    def from_dict(field_dict):
        def get_type(val):
            try:
                return SpectreType[val.upper()]
            except KeyError as e:
                print('lol')
                raise BadInputException(f'Invalid type: {val}')

        fields = { 
            'name': {
                'validator': lambda val: isinstance(val, str),
                'value': lambda val: val
            },
            'type': {
                'validator': lambda val: True, 
                'value': get_type
            },
            'description': {                
                'validator': lambda val: isinstance(val, str),
                'value': lambda val: val
            },
            'required': {
                'validator': lambda val: isinstance(val, bool), 
                'value': lambda val: val
            },
            'example': {
                'validator': lambda val: True,
                'value': lambda val: val
            },
            'default': {
                'validator': lambda val: True,
                'value': lambda val: val
            }
        }
        field = Field()
        for key, field_properties in fields.items():
            raw_value = field_dict.get(key, None)
            value = field_properties['value'](raw_value)
            if value:
                if field_properties['validator'](value):
                    setattr(field, key, value)
                else:
                    raise BadInputException(f'Invalid data provided: {key}: {value}')
        return field

@dataclass
class Entity:
    name: str
    description: str = None
    fields: List[Field] = field(default_factory=list)

    def __init__(self, name: str, description='', fields=[]):
        self.name = name
        self.description = description
        self.fields=fields
        self.validate()

    def validate(self):
        def validate_name(name):
            if not name:
                raise Exception('Name cannot be empty')
            if not isinstance(name, str):
                raise BadInputException(f'Name must be a string: {name}')
        validate_name(self.name)

    def to_json(self):
        self_dict = {k: v for k, v in asdict(self).items() if v}
        fields = []
        for field in self.fields:
            filtered = {k: v for k, v in asdict(field).items() if v}
            filtered['type'] = field.type.name.lower()
            fields.append(filtered)
        self_dict['fields'] = fields
        output = {}
        output[self_dict.pop('name')] = self_dict
        return json.dumps(output, sort_keys=False,
                    indent=4, separators=(',', ': '))

    @staticmethod
    def from_dict(name, ent_dict):
        ent = Entity(name=name, description=ent_dict.get('description', None))
        for field_dict in ent_dict['fields']:
            ent.fields.append(Field.from_dict(field_dict))
        return ent
