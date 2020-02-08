import re
from .internal import FeatureRecord

class Query():
    model_type = FeatureRecord

    def __init__(self):
        # The field key must equal exactly value, or re.search if a compiled regex
        self._value_equals = dict()

        # The field of type list named key must contain value
        self._list_contains = dict()

        # The field named key must equal one of the sub value in the list value
        self._value_equals_one_of = dict()

    @property
    def value_equals(self):
        return self._value_equals

    @property
    def list_contains(self):
        return self._list_contains

    @property
    def value_equals_one_of(self):
        return self._value_equals_one_of

    def name_regex_is(self, regex):
        self._value_equals[self.model_type.name.name_] = re.compile(regex)
        return self
        
    def type_is(self, cls):
        self._value_equals['_type'] = cls._type
        return self

    def type_any_of(self, classes):
        self._value_equals_one_of['_type'] = [cls._type for cls in classes]
        return self
    
    def test_uuid_is(self, test_uuid):
        self._value_equals[self.model_type.test_id.test_uuid.name_] = test_uuid
        return self
    
    def test_uuid_any_of(self, test_uuids):
        self._value_equals_one_of[self.model_type.test_id.test_uuid.name_] = test_uuids
        return self
    
    def testbench_name_is(self, testbench_name):
        self._value_equals[self.model_type.test_id.testbench_name.name_] = testbench_name
        return self
    
    def outcome_is(self, **outcome_attributes):
        for field_name, value in outcome_attributes.items():
            field = getattr(self.model_type.outcome, field_name)
            self._value_equals[field.name_] = value
        return self
    
    def dut_match(self, id=None, version=None):
        if id is not None:
            self._value_equals[self.model_type.test_id.dut.id.name_] = re.compile(id)
        if version is not None:
            self._value_equals[self.model_type.test_id.dut.version.name_] = re.compile(version)
        return self

    def __repr__(self):
        return '{}(eq={}, one-of={}, contains={})'.format(
            self.__class__.__name__,
            repr(self._value_equals),
            repr(self._value_equals_one_of),
            repr(self._list_contains)
        )