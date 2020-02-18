import pickle

from .. import Transformer

from spintop.models import (
    SpintopTestRecordCollection
)

class TestFormatTransformer(Transformer):
    
    def __call__(self, data):
        # TODO if cache is desired, add it here.
        data = self.collect_fn(data)
        data = self.transform_fn(data)
        return data
        
    def collect_fn(self, data):
        return data
            
    def transform_fn(self, data):
        return data