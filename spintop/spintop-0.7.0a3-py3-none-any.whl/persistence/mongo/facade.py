import os

from spintop.persistence import PersistenceFacade
from spintop.models import SpintopFlatTestRecordBuilder, Query

from .operations import db_from_mongo_uri
from .mappers import create_mappers, TestRecordSummary, FeatureRecord

class MongoPersistenceFacade(PersistenceFacade):
    def __init__(self, mongo_db, serializer=None):
        mappers = create_mappers(mongo_db, serializer=serializer)
        super(MongoPersistenceFacade, self).__init__(mappers=mappers)

        self.tr_mapper = mappers[TestRecordSummary]
        self.feature_mapper = mappers[FeatureRecord]
    
    @classmethod
    def from_mongo_uri(cls, mongo_uri, database_name):
        return cls(db_from_mongo_uri(mongo_uri, database_name))
    
    @classmethod
    def from_env(cls, mongo_uri_env_name='SPINTOP_MONGO_URI', database_name_env_name='SPINTOP_DATABASE_NAME'):
        return cls.from_mongo_uri(
            mongo_uri=os.environ[mongo_uri_env_name],
            database_name=os.environ[database_name_env_name]
        )
        
    def create(self, records):
        self._iter_op('create', records)
        
    def _iter_op(self, op_name, records):

        test_top_level_records = [record.data for record in records]
        all_features = []
        for record in records:
            all_features += record.features

        self.logger.info('Processing {} of {} flat records.'.format(
                op_name, len(test_top_level_records)
            )
        )
        getattr(self.tr_mapper, op_name)(test_top_level_records)
        getattr(self.feature_mapper, op_name)(all_features)
        
        
    def retrieve(self, test_selector=None, feature_selector=None):
        top_level_records = self.tr_mapper.retrieve(test_selector)
        
        test_uuid_to_flat_builder = {tlr.test_id.test_uuid: SpintopFlatTestRecordBuilder(data=tlr, features=[]) for tlr in top_level_records}
        
        selected_ids = [tlr.test_id.test_uuid for tlr in top_level_records]
        
        if not feature_selector: feature_selector = Query()
        
        feature_selector.test_uuid_any_of(selected_ids)
        
        all_features = self.feature_mapper.retrieve(feature_selector)
        
        for feature in all_features:
            test_uuid_to_flat_builder[feature.test_id.test_uuid].features.append(feature)
        
        for _, flat_builder in test_uuid_to_flat_builder.items():
            yield flat_builder.build()
        
    def update(self, records):
        self._iter_op('update', records)
    
    def delete(self, match_query):
        self.logger.info('Deleting flat records based on query: %s.' % repr(match_query))
        self.tr_mapper.delete(match_query)
        self.feature_mapper.delete(match_query)