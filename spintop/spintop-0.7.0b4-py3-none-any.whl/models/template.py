import itertools
from dataclasses import dataclass, fields

from .internal import FeatureRecordTemplate
from .collection import SpintopTestRecord

def default_feature_filter(feature):
    return True

class TestRecordTemplate(object):
    def __init__(self, test_records, feature_filter=None):
        self.template_record = SpintopTestRecord()
        self.names_lookup = {}
        self.tests_contained = {}
        
        self.add_test_records(test_records, feature_filter=feature_filter)
        
        
    def add_test_records(self, test_records, feature_filter=None):
        
        for record in test_records:
            self._add_test_record(record, feature_filter=feature_filter)
            
        self.clean()
        
    def _add_test_record(self, test_record, feature_filter=None):
        
        if feature_filter is None: feature_filter = default_feature_filter
        
        features = tuple(feature for feature in test_record.features if feature_filter(feature))
        
        if not features:
            raise ValueError("Filter yields empty features list.")
        
        new_features = tuple(f.copy(as_cls=FeatureRecordTemplate, set_attributes=dict(source=f)) for f in features if (f.name not in self.names_lookup))
        
        self.template_record.features += new_features
        
        for template in new_features:
            self.names_lookup[template.name] = template
        
        # Update stats in template features
        for feature in features:
            self.names_lookup[feature.name].increment_records_count()
            
        self.tests_contained[test_record] = test_record
        
        
    def clean(self):
        # TODO Topological sort before reindexing
        self.template_record.reindex()
        
    def compute_stats(self):
        self.compute_match_scores()
        
    def compute_match_scores(self):
        abs_max_score = len(self.tests_contained)*len(self.names_lookup)
        max_score = 0
        for _, test_record in self.tests_contained.items():
            
            score_int = 0
            for feature in test_record.features:
                # Non-original features meant they were filled in or otherwise not part of the original test
                if feature.original and feature.name in self.names_lookup:
                    # Add score only if original feature and if present in lookup.
                    # If it's not present, it was probably filtered out during creation.
                    score_int += self.names_lookup[feature.name].records_count
            
            max_score = max(max_score, score_int)
            
            test_record.data.template_match_score = score_int
        
        # Normalize all scores based on max score
        for _, test_record in self.tests_contained.items():
            test_record.data.template_match_score_normalized = test_record.data.template_match_score/max_score
    
        
        
    def fill_missing_features(self, test_record):
        """ Based on this template, fill missing features with no data into test_record.
        """
        
        # First step is to reindex test_record features to match the template indices.
        # The names_lookup lookup table allows to quickly find indices.
        for feature in test_record.features:
            feature.index = self.names_lookup[feature.name].index
            
        test_record.fill_missing_from_source(
            self.template_record.features, 
            on_fill=lambda template: template.source.copy(
                with_data=False, 
                set_attributes=dict(original=False)
            )
        )
        