
from bson.objectid import ObjectId

from spintop.models import BaseDataClass
from spintop.models.serialization import get_bson_serializer

def to_mongo_id(_dict, strip_id_none=False):
    if 'oid' in _dict:
        _dict['_id'] = to_object_id(_dict.pop('oid'))
    
    if strip_id_none and _dict.get('_id', False) is None:
        del _dict['_id']
        
    return _dict
    
def from_mongo_id(_dict):
    if '_id' in _dict:
        _dict['oid'] = from_object_id(_dict.pop('_id'))
    return _dict

def to_object_id(encoded_bytes):
    if encoded_bytes:
        return ObjectId(encoded_bytes)
    else:
        return None
    
def from_object_id(oid):
    if oid:
        return str(oid)
    else:
        return None

class DataClassSerializer(object):
    def __init__(self, serializer=None):
        if serializer is None: serializer = get_bson_serializer()
        
        self.serializer = serializer
        
    def serialize(self, obj):
        return self.serializer.serialize(obj)
    
    def serialize_many(self, objs):
        return [self.serialize(obj) for obj in objs]
    
    def deserialize(self, serialized):
        return self.serializer.deserialize(BaseDataClass, serialized)

    def deserialize_many(self, objs):
        return [self.deserialize(obj) for obj in objs]

    def serialized_to_mongo_id(self, serialized, keep_id_if_none=True):
        return to_mongo_id(serialized, strip_id_none=not keep_id_if_none)

    def serialized_from_mongo_id(self, serialized):
        return from_mongo_id(serialized)
    