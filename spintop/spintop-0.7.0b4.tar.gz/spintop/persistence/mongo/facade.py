import os

from spintop.persistence import PersistenceFacade
from spintop.models import SpintopTestRecord, SpintopSerializedFlatTestRecord, Query, serialized_get_test_uuid

from .operations import db_from_mongo_uri
from .mappers import create_mappers, TestRecordSummary, FeatureRecord


class MongoPersistenceFacade(PersistenceFacade):
    def __init__(self, mongo_db, serializer=None):
        mappers = create_mappers(mongo_db, serializer=serializer)
        self.tr_mapper = mappers[TestRecordSummary]
        self.feature_mapper = mappers[FeatureRecord]
        self._init(mappers)
        self.dc_serializer = self.tr_mapper.dc_serializer
    
    def _init(self, mappers):
        for _, mapper in mappers.items():
            mapper.init()

    @classmethod
    def from_mongo_uri(cls, mongo_uri, database_name):
        return cls(db_from_mongo_uri(mongo_uri, database_name))
    
    @classmethod
    def from_env(cls, mongo_uri_env_name='SPINTOP_MONGO_URI', database_name_env_name='SPINTOP_DATABASE_NAME'):
        return cls.from_mongo_uri(
            mongo_uri=os.environ[mongo_uri_env_name],
            database_name=os.environ[database_name_env_name]
        )

    def serialize_barrier(self, records):
        if records and isinstance(records[0], SpintopTestRecord):
            records = self.dc_serializer.serialize_many(records)

        if records and isinstance(records[0], dict):
            return [SpintopSerializedFlatTestRecord(**record) for record in records]
        else:
            return records
        
    def create(self, records):
        self._iter_op('create', records)
        
    def _iter_op(self, op_name, records):
        records = self.serialize_barrier(records)

        test_top_level_records = [record.test_record for record in records] 

        all_features = []
        for record in records:
            all_features += record.features

        self.logger.info('Processing {} of {} flat records.'.format(
                op_name, len(test_top_level_records)
            )
        )
        getattr(self.tr_mapper, op_name)(test_top_level_records)
        getattr(self.feature_mapper, op_name)(all_features)
        
        
    def retrieve(self, test_selector=None, feature_selector=None, deserialize=True):
        top_level_records = self.tr_mapper.retrieve(test_selector)

        test_uuid_to_serialized = {serialized_get_test_uuid(tlr): SpintopSerializedFlatTestRecord(test_record=tlr, features=[]) for tlr in top_level_records}
        
        selected_ids = [serialized_get_test_uuid(tlr) for tlr in top_level_records]
        
        if not feature_selector: feature_selector = Query()
        
        feature_selector.test_uuid_any_of(selected_ids)
        
        all_features = self.feature_mapper.retrieve(feature_selector)
        
        for feature in all_features:
            test_uuid_to_serialized[serialized_get_test_uuid(feature)].features.append(feature)
        
        for _, serialized in test_uuid_to_serialized.items():
            if deserialize:
                yield serialized.deserialize(self.dc_serializer.serializer)
            else:
                yield serialized
        
    def update(self, records):
        self._iter_op('update', records)
    
    def delete(self, match_query):
        self.logger.info('Deleting flat records based on query: %s.' % repr(match_query))
        self.tr_mapper.delete(match_query)
        self.feature_mapper.delete(match_query)