from enum import Enum
from typing import *

from dataclasses_json import LetterCase
from pyhocon import ConfigTree

_FIELD_CONSTRUCTOR_ARGUMENT_TYPE = '__config_constructor_argument_type__field_name__'
_FIELD_CONSTRUCTOR_POST_INIT = '__config_constructor_post_init__field_name__'

class ConstructorDataType(Enum):
    """
    A data type which is used for the constructor
    
    The following data types are allowed:
    
     - String
     - Integer
     - Float
     - Boolean
     - Config
     - List
    """
    
    String = ConfigTree.get_string
    Integer = ConfigTree.get_int
    Float = ConfigTree.get_float
    Boolean = ConfigTree.get_bool
    Config = ConfigTree.get_config
    List = ConfigTree.get_list
    Any = ConfigTree.get

T = TypeVar('T')
PostInitFunctionType = Callable[[T, Type[T]], Any]
"""
A type alias for
`(self, cls) => Optional[self]`
"""

def deserialize_with(constructor_data_type: ConstructorDataType, *, post_init: Union[PostInitFunctionType, str, None] = None) -> Callable[[Type[T]], Type[T]]:
    """
    Decorates a class to mark it as an automatically deserialized while reading the configuration.
    
    Args:
        constructor_data_type: `ConstructorDataType`. A data type which is used for the constructor.
        post_init: Optional. `str` or `PostInitFunctionType`.
            If presented, defines the post-init callback for that type.
            It would be called after the constructor, with the following arguments:
            
             - instance
             - class (exactly as described in type annotations)
             - a `dataclasses_config.Config` instance which calls the post-init.
            
            If this method returns something that is not `None`,
            the original value would be reassigned.
            
            If the argument value is the string rather than callable,
            then it is counted as the class's method name.
            That method signature should be the same.
    
    """
    
    def decorator(cls: Type['T']):
        setattr(cls, _FIELD_CONSTRUCTOR_ARGUMENT_TYPE, constructor_data_type)
        nonlocal post_init
        if (isinstance(post_init, str)):
            post_init = getattr(cls, post_init)
        setattr(cls, _FIELD_CONSTRUCTOR_POST_INIT, post_init)
        return cls
    return decorator
del T    

def dataclass_json_config(*, letter_case: LetterCase = None, **kwargs):
    """
    Sets the config for the given JSON DataClass.
    
    Args:
        letter_case: `dataclasses_json.LetterCase`.
            A policy for JSON DataClass key switch.
        
        **kwargs: 
            Other settings those are introduced in the future.
    """
    
    from dataclasses_json import config, DataClassJsonMixin
    
    if (letter_case is not None):
        kwargs['letter_case'] = letter_case
    
    T = TypeVar('T', bound=DataClassJsonMixin)
    def wrapper(cls: Type[T]) -> Type[T]:
        if (kwargs):
            cls.dataclass_json_config = config(**kwargs)['dataclasses_json']
        return cls
    del T
    
    return wrapper

__all__ = \
[
    'dataclass_json_config',
    'deserialize_with',
    
    'ConstructorDataType',
    'PostInitFunctionType',
]
