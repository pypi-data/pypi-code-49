
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
        
    def serialize(self, obj, keep_id_if_none=True):
        serialized = self.serializer.serialize(obj)
        return to_mongo_id(serialized, strip_id_none=not keep_id_if_none)
    
    def serialize_many(self, objs, keep_id_if_none=True):
        return [self.serialize(obj, keep_id_if_none=keep_id_if_none) for obj in objs]
    
    def deserialize(self, obj):
        serialized = from_mongo_id(obj)
        return self.serializer.deserialize(BaseDataClass, serialized)
    
    def deserialize_many(self, objs):
        return [self.deserialize(obj) for obj in objs]
