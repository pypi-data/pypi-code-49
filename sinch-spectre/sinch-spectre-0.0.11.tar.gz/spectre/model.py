from enum import Enum
import json
from dataclasses import dataclass, field, asdict
from typing import List, Any

class UnknownTypeException(Exception):
    pass

@dataclass
class SpectreType(Enum):
    INT = 1
    STRING = 2
    BOOL = 3
    DATETIME = 4
    FLOAT = 5
    ENUM = 6
    UUID = 7
    UNDEFINED = 8

@dataclass
class Field:
    name: str = None
    type: SpectreType = SpectreType.UNDEFINED
    description: str = None
    required: bool = False
    default: Any = None
    example: Any = None
    #TODO: Add and enforce validation

    @staticmethod
    def from_dict(field_dict):
        fields = { 
            'name': {
                'validator': lambda val: isinstance(val, str),
                'value': lambda val: val
            },
            'type': {
                'validator': lambda val: True, 
                'value': lambda val: SpectreType[val.upper()]
            },
            'description': {                
                'validator': lambda val: True, 
                'value': lambda val: val
            },
            'required': {
                'validator': lambda val: True, 
                'value': lambda val: val
            },
            'example': {
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
                    raise Exception(f'Invalid data provided: {key}: {value}')
        return field

@dataclass
class Entity:
    name: str = None
    description: str = None
    fields: List[Field] = field(default_factory=list)

    def to_json(self):
        self_dict = asdict(self)
        for index, value in enumerate(self_dict['fields']):
            filtered = {k: v for k, v in value.items() if v is not None}
            self_dict['fields'][index] = filtered
        self.fields = filtered
        return json.dumps(self_dict, sort_keys=False,
                    indent=4, separators=(',', ': '))

    @staticmethod
    def from_dict(name, ent_dict):
        ent = Entity()
        ent.name = name
        ent.description = ent_dict.get('description', None)
        for field_dict in ent_dict['fields']:
            ent.fields.append(Field.from_dict(field_dict))
        return ent
