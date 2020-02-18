
from .operations import MongoOperations, ASCENDING
from .serialization import DataClassSerializer

from spintop.models import (
    TestRecordSummary, 
    FeatureRecord, 
    SpintopTestRecord, 
    SpintopFlatTestRecordBuilder,
    Query
)


from ...logs import _logger


SIMPLE_MAPPER_DATACLASSES_COLLECTION_NAMES = {}

SIMPLE_MAPPER_DATACLASSES_INIT_FNS = {}

logger = _logger('mongo')

def register_simple_mapper(cls, collection_name):
    SIMPLE_MAPPER_DATACLASSES_COLLECTION_NAMES[cls] = collection_name
    SIMPLE_MAPPER_DATACLASSES_INIT_FNS[cls] = None
    def _register_init(fn):
        SIMPLE_MAPPER_DATACLASSES_INIT_FNS[cls] = fn
        return fn
    return _register_init

# Mappers
@register_simple_mapper(TestRecordSummary, 'test-records')
def init_test_record_mapper(mapper):
    mapper.ops.create_index([("test_id.test_uuid", ASCENDING)], unique=True)
    
register_simple_mapper(FeatureRecord, 'test-features')

def create_mappers(mongo_db, serializer=None, operations_factory=None):
    if operations_factory is None: operations_factory = MongoOperations
    
    # Simple mappers are 1:1 with a document in a mongo collection.
    mappers = {}
    for dataclass, collection_name in SIMPLE_MAPPER_DATACLASSES_COLLECTION_NAMES.items():
        init_fn = SIMPLE_MAPPER_DATACLASSES_INIT_FNS[dataclass]
        ops = operations_factory(mongo_db[collection_name])
        mappers[dataclass] = SimpleMongoMapper(ops, serializer=serializer, on_init=init_fn, name=collection_name)
    
    return mappers

class SimpleMongoMapper(object):
    def __init__(self, ops, serializer=None, on_init=None, name="simple"):
        if serializer is None: serializer = DataClassSerializer()
        self.ops = ops
        self.dc_serializer = serializer
        self.on_init = on_init
        self.logger = logger.getChild(name)
    
    def init(self):
        if self.on_init: self.on_init(self)
    
    def create(self, dataclasses):
        serialized_dcs = self.dc_serializer.serialize_many(dataclasses, keep_id_if_none=False)
        
        resp = self.ops.insert_many(serialized_dcs)
        self.logger.info('Inserted %d new documents' % len(resp.inserted_ids))
        
        # ids are inserted client side into the 'serialized' dictionnary.
        # We can re-insert _ids into dataclasses.
        for dc, serialized in zip(dataclasses, serialized_dcs):
            dc.oid = serialized['_id']
            
    def retrieve(self, query):
        responses = self.ops.find(query)
        return self.dc_serializer.deserialize_many(responses)
        
    def update(self, dataclasses):
        serialized = self.dc_serializer.serialize_many(dataclasses)
        self.ops.update_many(serialized, by='_id')
        
    def delete(self, query):
        resp = self.ops.delete_many(query)
        self.logger.info('Deleted %d documents' % resp.deleted_count)