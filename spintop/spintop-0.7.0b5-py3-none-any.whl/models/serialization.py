import dateutil.parser
from datetime import datetime
from time import mktime
from copy import copy

from dataclasses_serialization.serializer_base import dict_to_dataclass, dict_serialization, list_deserialization

from .internal import BaseDataClass
from .collection import SpintopTestRecord, SpintopSerializedFlatTestRecord

SpintopBSONSerializer = None
SpintopJSONSerializer = None

class MalformedSerializedData(Exception):
    pass

def get_serializer():
    return get_bson_serializer()

def get_bson_serializer():
    """Make or return the singleton SpintopBSONSerializer"""
    from dataclasses_serialization.bson import BSONSerializer
    global SpintopBSONSerializer
    if SpintopBSONSerializer:
        return SpintopBSONSerializer

    serializer = copy(BSONSerializer)
    _make_serializer(serializer)
    SpintopBSONSerializer = serializer
    return serializer

def get_json_serializer():
    from dataclasses_serialization.json import JSONSerializer
    global SpintopJSONSerializer
    if SpintopJSONSerializer:
        return SpintopJSONSerializer
    
    serializer = copy(JSONSerializer)
    
    @serializer.register_serializer(datetime)
    def serialize_datetime(obj):
        return mktime(obj.timetuple())

    @serializer.register_deserializer(datetime)
    def deserialize_datetime(cls, obj):
        if isinstance(obj, str):
            return dateutil.parser.parse(obj)
        else:
            return datetime.fromtimestamp(obj)
        
    _make_serializer(serializer)

    SpintopJSONSerializer = serializer
    return serializer

def _make_serializer(serializer):
    orig_deserialize = serializer.deserialize
    def wrapped_deserialize(cls, obj):
        """ Always support any obj that is None. Default implementation
        will raise an error if obj is None and the type of a dataclass
        field is anything but Any or None
        """
        if obj is None:
            return None
        else:
            return orig_deserialize(cls, obj)
    
    serializer.deserialize = wrapped_deserialize
    
    @serializer.register_serializer(BaseDataClass)
    def serialize(obj):
        """Custom serializer for BaseDataClass that extracts the static
        attribute '_type' into the serialized dict for future deserialization."""
        data = dict_serialization(dict(obj.__dict__), key_serialization_func=serializer.serialize, value_serialization_func=serializer.serialize)
        data.update({'_type': obj._type})
        return data

    @serializer.register_deserializer(BaseDataClass)
    def deserialize(cls, obj):
        """ Custom deserializer that infers the BaseDataClass subclass based
        on the _type attribute. 
        """
        # Strips the _type field and returns the sub cls, if found. Else returns the cls
        # as passed in parameter
        cls, obj = BaseDataClass.cls_data_from_dict(cls, obj)
        return dict_to_dataclass(cls, obj, deserialization_func=serializer.deserialize)

    
    @serializer.register_serializer((SpintopTestRecord, SpintopSerializedFlatTestRecord))
    def serialize_spintop_test_record(obj):
        return serializer.serialize(obj.as_dict())

    @serializer.register_deserializer(SpintopTestRecord)
    def deserialize_spintop_test_record(cls, obj):
        result = {}
        if isinstance(obj, SpintopSerializedFlatTestRecord):
            result = obj.as_dict()
        else:
            if 'test_record' in obj:
                result['test_record'] = serializer.deserialize(BaseDataClass, obj['test_record'])
            
            if 'features' in obj:
                result['features'] = [serializer.deserialize(BaseDataClass, feat) for feat in obj['features']]

        return cls.from_dict(result)
    
    return serializer


def serialized_get_test_uuid(record):
    try:
        return record['test_id']['test_uuid']
    except KeyError:
        raise MalformedSerializedData("test_id.test_uuid not in record! {!r}".format(record))