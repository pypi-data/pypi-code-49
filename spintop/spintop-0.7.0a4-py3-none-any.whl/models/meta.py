import inspect
from collections import Mapping

from dataclasses import dataclass, fields, _MISSING_TYPE, MISSING, field, asdict

from .view import DataClassPrimitiveView, join_key_prefix

_TYPE_MAP = {}

def register_type(_type):
    def _wrap_cls(cls):
        cls._type = _type
        assert _type not in _TYPE_MAP, "Type %s is already registered to class %s" % (_type, _TYPE_MAP[_type])
        _TYPE_MAP[_type] = cls
        return cls
    return _wrap_cls

class CacheByCls():
    
    def __init__(self):
        self.value_by_cls = {}
        
    def retrieve(self, cls):
        if not self.value_by_cls.get(cls, None):
            self.value_by_cls[cls] = self._get(cls)
        return self.value_by_cls[cls]
    
    def _get(self, cls):
        raise NotImplementedError()
    
class FieldsCache(CacheByCls):
    """The fields() function is quite slow. This allows to store its 
    return value per cls, as it shouldn't change dynamically during
    runtime."""
    
    def _get(self, cls):
        return fields(cls)
    
class DefaultViewsCache(CacheByCls):
    def _get(self, cls):
        return DataClassPrimitiveView(
            cls.get_default_view_mapping()
        )

_fields_cache = FieldsCache()
_default_views_cache = DefaultViewsCache()

class KeyValueOf(object):
    def __init__(self, attr_name):
        self.attr_name = attr_name
    
    def __call__(self, obj):
        return getattr(obj, self.attr_name)

class MetaBaseDataClass(type):
    def __getattr__(cls, key):
        """ Allows fields to be accessed from class. I.e. 
        
        @dataclass()
        class MyDataClass(BaseDataClass):
            my_field: str
            
        MyDataClass.my_field.name == 'my_field'
        """
        try:
            return cls.get_field(key)
        except AttributeError:
            return super().__getattribute__(key)
    
    def get_field(cls, key, parent_fields=()):
        # no cache here has the cls might be being build.
        for field in fields(cls):
            if field.name == key:
                return MetaField(field, parents=parent_fields)
        else:
            raise AttributeError(key)


class MetaField(object):
    def __init__(self, field, parents=()):
        self.__parents = parents
        self.__field = field
    
    @property
    def name_(self):
        names = tuple(parent.__field.name for parent in (self.__parents + (self,))) 
        return '.'.join(names)

    def __getattr__(self, key):
        try:
            return self.__field.type.get_field(key, parent_fields=self.__parents + (self,))
        except AttributeError:
            return getattr(self.__field, key)
    
    def __eq__(self, other):
        if type(other) is type(self):
            return self.__members() == other.__members()
        else:
            return False

    def __hash__(self):
        return hash(self.__field)
    
    def __eq__(self, other):
        return self.__field == other.__field

    
# def make_operation(field, op_on_value):
#     return lambda real_obj: op_on_value(getattr(real_obj, field.name))

def model_dataclass(**kwargs):
    return dataclass(init=False, **kwargs)

@model_dataclass()
@register_type('_base')
class BaseDataClass(metaclass=MetaBaseDataClass):
    
    def __init__(self, *args, **kwargs):
        if args:
            raise NotImplementedError('Positionnal args not supported with BaseDataClass descendants.')
        defaults = self.defaults()
        defaults.update(kwargs)
        
        self.__dict__.update(defaults)
        
    @classmethod
    def defaults(cls, **others):
        return others
    
    @classmethod
    def null(cls, **not_null_fields):
        """ Creates an instance with all attributes set to None. 
        Calls null() on any sub- BaseDataClass fields.
        """
        arguments = {}
        fields = cls.get_fields()
        for field in fields:
            if inspect.isclass(field.type) and issubclass(field.type, BaseDataClass):
                value = field.type.null()
            elif not isinstance(field.default_factory, _MISSING_TYPE):
                value = field.default_factory()
            elif field.default != MISSING:
                value = field.default
            else:
                value = None
                # try:
                #     value = field.type()
                # except TypeError:
                #     raise Exception('Field {} of type {} from {} does not support call without arguments for null()'.format(field.name, field.type, cls))
            arguments[field.name] = value
        
        arguments.update(not_null_fields)
        return cls(**arguments)
    
    @classmethod
    def get_fields(cls):
        return _fields_cache.retrieve(cls)
    
    @classmethod
    def get_data_fields(cls):
        """ Sub classed by FeatureRecord below.
        """
        return cls.get_fields()
        
    @classmethod
    def get_default_view(cls):
        return _default_views_cache.retrieve(cls)
        
    @classmethod
    def get_default_view_mapping(cls, with_key_prefix=None):
        if with_key_prefix is not None:
            key_creator = lambda key: join_key_prefix(with_key_prefix, key)
        else:
            key_creator = lambda key: key
        
        # The default view uses the fields defined by the get_data_fields class method.
        fields = cls.get_data_fields()
        
        return {key_creator(field.name): field for field in fields}
        
    
    def copy(self, with_data=True, as_cls=None, set_attributes={}):
        if with_data:
            nullify_fields = []
        else:
            nullify_fields = self.get_data_fields()
            
        copy_obj = copy_nullify_fields(self, nullify_fields, target_cls=as_cls)
        for name, value in set_attributes.items():
            setattr(copy_obj, name, value)
        return copy_obj
    
    def as_dict(self):
        """ Transforms this object recursively into a dict. Adds the static
        _type field to the data"""
        data = asdict(self)
        data.update({'_type': self._type})
        return data
    
    @staticmethod
    def cls_data_from_dict(cls, data):
        _type = data.pop('_type', None)
        if _type:
            cls = _TYPE_MAP[_type]
        return cls, data
    
    def get_recursive(self, as_str=None, as_array=None):
        if as_str:
            as_array = as_str.split('.')
        
        this_attr_name = as_array.pop(0)
        this_attr = getattr(self, this_attr_name)
        if as_array:
            return this_attr.get_recursive(as_array=as_array)
        else:
            return this_attr


def copy_nullify_fields(obj, null_fields, target_cls=None):
    if target_cls is None:
        target_cls = obj.__class__
    
    copy_obj = target_cls.null()
    not_null_fields = (set(obj.get_fields()) - set(null_fields)) & set(target_cls.get_fields())
    for field in not_null_fields:
        setattr(copy_obj, field.name, getattr(obj, field.name))
    
    return copy_obj
