from itertools import chain

from collections import Mapping, OrderedDict, defaultdict
from typing import NamedTuple, List

from .internal import TestIDRecord, TestRecordSummary, FeatureRecord, DefaultPrimitiveView
from .view import ComplexPrimitiveView

def normalize_features_len(dict_array):
    new_dict = {}
    max_column_key_len = max([len(key) for key in dict_array])
    for key, value in dict_array.items():
        if len(key) < max_column_key_len:
            key = key + ('',)*(max_column_key_len - len(key))
        new_dict[key] = value
    return new_dict
    
            
class SpintopTestRecordCollection(object):
    def __init__(self, flat_records=None):
        self.records = list(flat_records) if flat_records else []
    
    @property
    def collector(self):
        return self.add_record
    
    def add_record(self, record):
        self.records.append(record)
        
    def apply(self, *fns):
        for record in self.iter_records():
            for fn in fns:
                fn(record)
                
    def iter_records(self):
        for record in self.records:
            yield record
                
    def count_unique(self, key=lambda record: record.test_id.test_uuid):
        occurances = set()
        self.apply(lambda record: occurances.add(key(record)))
        return len(occurances)
            
    def sort(self, key=lambda record: record.test_id.start_datetime):
        self.records.sort(key=key)
        
    def avg_feature_count(self):
        feature_counts = [len(record.features) for record in self.iter_records()]
        return sum(feature_counts)/len(feature_counts)
    
class SpintopTestRecord(object):
    def __init__(self, test_record=None, features=None):
        self._data = None
        self._features = None
        
        self.data = test_record if test_record else TestRecordSummary.null() # The top-level data
        self.features = tuple(features) if features else tuple()
    
    @property
    def features(self):
        return self._features if self._features else tuple()
    
    @features.setter
    def features(self, features):
        self._broadcast_test_id(features)
        self._features = sorted(features, key=lambda feature: feature.index)
        
    def compute_stats(self):
        if not self._data.total_feature_count:
            self._data.total_feature_count = len(self.features)
        
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value
        self._broadcast_test_id(self.features)
        
    @property
    def test_id(self):
        return self.data.test_id
    
    def __hash__(self):
        return hash(self.test_id.test_uuid)

    def __eq__(self, other):
        return self.test_id.test_uuid == other.test_id.test_uuid

    
    def remove_duplicate_features(self):
        feature_names = set()
        features = []
        for feature in self.features:
            if feature.name in feature_names:
                continue
            else:
                features.append(feature)
                feature_names.add(feature.name)
        
        self.features = features
    
    def _broadcast_test_id(self, features):
        """Uses the top level test_id and sets it for all features, ensuring
        that all features have the same TestIDRecord reference."""
        for feature in features:
            feature.test_id = self.data.test_id
    
    def reindex(self):
        for index, feature in enumerate(self.features):
            feature.index = index
            
    def fill_missing_from_source(self, fill_source, on_fill=None):
        max_current_feature_index = max(self.features, key=lambda f: f.index)
        new_features_len = len(fill_source)
        
        assert new_features_len >= max_current_feature_index.index, "Fill source must be same length or bigger than this test_record max index."
        
        new_features = [None]*new_features_len
        
        if on_fill is None:
            on_fill = lambda obj: obj.copy()
            
        def fill_range(start, end):
            for i in range(start, end):
                new_features[i] = on_fill(fill_source[i])
        
        current_index = 0
        for feature in sorted(self.features, key=lambda f: f.index):
            fill_range(current_index, feature.index)
            new_features[feature.index] = feature # Keep this feature
            current_index = feature.index + 1
        
        fill_range(current_index, new_features_len) # Fill end
        
        self.features = new_features
                
    def find_feature(self, condition, start_index=0):
        return next(feat for feat in self.features[start_index:] if condition(feat))
    
    def add_tag(self, key, value=True):
        self.test_id.add_tag(key, value=value)
        
    def remove_tag(self, key):
        self.test_id.remove_tag(key)

    def as_dict(self):
        return dict(
            test_record=self._data,
            features=self._features
        )

    @classmethod
    def from_dict(cls, _dict):
        return cls(**_dict)

class SpintopTestRecordView(object):
    feature_prefix = ('features', lambda feat: feat._type, lambda feat: feat.complete_name)
    data_prefix = () 
    default_view = DefaultPrimitiveView()
    
    def apply(self, record, flatten_dict=True):
        data = OrderedDict()
        
        test_id_data = self.apply_default_test_id(record, flatten_dict=flatten_dict)
        data.update(test_id_data)
        
        for feature in record.features:
            feature_data = self.apply_default_feature(feature, flatten_dict=flatten_dict)
            data.update(feature_data)
            
        return data
    
    def apply_default_feature(self, feature, key_prefix=None, **apply_kwargs):
        if key_prefix is None: key_prefix = self.feature_prefix
        return self.default_view.apply(feature, key_prefix=key_prefix, **apply_kwargs)
    
    def apply_default_test_id(self, record, key_prefix=None, **apply_kwargs):
        if key_prefix is None: key_prefix = self.data_prefix
        data = self.default_view.apply(record.data, key_prefix=key_prefix, **apply_kwargs)
        return data

class SpintopFlatTestRecordBuilder(NamedTuple):
    data: TestRecordSummary
    features: List[FeatureRecord]
    
    def build(self):
        record = SpintopTestRecord(test_record=self.data, features=sorted(self.features, key=lambda feature: feature.index))
        record.compute_stats()
        return record
        
    