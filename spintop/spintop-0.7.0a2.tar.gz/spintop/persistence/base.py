from spintop.generators import Generator

from spintop.models import (
    TestRecordSummary, 
    FeatureRecord, 
    SpintopTestRecord
)

from ..logs import _logger

logger = _logger('persistence')


class MissingMapper(Exception):
    def __init__(self, cls):
        super().__init__("Mapper for class {!r} is mandatory.".format(cls))

class NoMapperForObject(Exception):
    def __init__(self, obj, mappers):
        super(NoMapperForObject, self).__init__(
            'There are no known mapper able to interact with obj {!r} of class {}. Declared mappers are: {}'.format(
                obj,
                obj.__class__,
                [cls.__name__ for cls in mappers]
            )
        )
        
class DuplicateMapperClassName(Exception):
    def __init__(self, objcls):
        super(DuplicateMapperClassName, self).__init__(
            'The name of the class {} is duplicate. The class name linked to a mapper must be unique.'.format(
                objcls,
            )
        )

class PersistenceFacade(object):
    logger = logger
    def __init__(self, mappers):
        self.mappers = mappers
        self.mappers_name_index = create_mapper_name_index(mappers)
        self._init()
        
    def create(self, records):
        raise NotImplementedError()
        
    def retrieve(self, test_selector=None, feature_selector=None):
        """Generator."""
        raise NotImplementedError()
        
    def update(self, records):
        raise NotImplementedError()
    
    def delete(self, match_query):
        raise NotImplementedError()

    def _init(self):
        for key, mapper in self.mappers.items():
            mapper.init()
        
    def _get_mapper(self, obj):
        try:
            mapper = self.mappers[obj.__class__]
        except KeyError:
            raise NoMapperForObject(obj, mappers=self.mappers)
        return mapper
        
    def __getattr__(self, mapper_cls_name):
        try:
            return self.mappers_name_index[mapper_cls_name]
        except KeyError:
            raise AttributeError(mapper_cls_name)
    
    def create_records_generator(self):
        return PersistenceGenerator(self)
        
def create_mapper_name_index(mappers):
    mappers_name_index = {}
    for mapped_cls, mapper in mappers.items():
        name = mapped_cls.__name__
        if name in mappers_name_index:
            raise DuplicateMapperClassName(mapped_cls)
        mappers_name_index[name] = mapper
    return mappers_name_index
    
class PersistenceGenerator(Generator):
    def __init__(self, facade):
        super().__init__()
        self.facade = facade
    
    def __call__(self, test_selector=None, feature_selector=None):
        return self.facade.retrieve(
            test_selector=test_selector, 
            feature_selector=feature_selector
        )

class Mapper(object):
    def init(self):
        pass