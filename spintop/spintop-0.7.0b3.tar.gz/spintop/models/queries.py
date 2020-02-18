import re
from functools import wraps
from collections import OrderedDict, defaultdict
from .internal import FeatureOutcomeRecord
from .serialization import get_json_serializer

def record_call(fn):
    @wraps(fn)
    def _recorded(self, arg):
        self._record_call(fn.__name__, arg)
        return fn(self, arg)
    return _recorded

class Query():
    model_type = FeatureOutcomeRecord

    def __init__(self):
        # The field key must equal exactly value, or re.search if a compiled regex
        self._value_equals = dict()

        # The field of type list named key must contain value
        self._list_contains = dict()

        # The field named key must equal one of the sub value in the list value
        self._value_equals_one_of = dict()

        self._calls = OrderedDict()

    @property
    def value_equals(self):
        return self._value_equals

    @property
    def list_contains(self):
        return self._list_contains

    @property
    def value_equals_one_of(self):
        return self._value_equals_one_of

    def _record_call(self, fn_name, arg):
        self._calls[fn_name] = arg

    def add_call(self, fn_name, arg):
        getattr(self, fn_name)(arg)

    @record_call
    def name_regex_is(self, regex):
        self._value_equals[self.model_type.name.name_] = re.compile(regex)
        return self
    
    def type_is(self, cls):
        return self.type_is_str(cls._type)

    @record_call
    def type_is_str(self, cls_str):
        self._value_equals['_type'] = cls_str
        return self

    def type_any_of(self, classes):
        return self.type_any_of_str([cls._type for cls in classes])
    
    @record_call
    def type_any_of_str(self, classes_str):
        self._value_equals_one_of['_type'] = classes_str
        return self

    @record_call
    def test_uuid_is(self, test_uuid):
        self._value_equals[self.model_type.test_id.test_uuid.name_] = test_uuid
        return self
    
    @record_call
    def test_uuid_any_of(self, test_uuids):
        self._value_equals_one_of[self.model_type.test_id.test_uuid.name_] = test_uuids
        return self
    
    @record_call
    def testbench_name_is(self, testbench_name):
        self._value_equals[self.model_type.test_id.testbench_name.name_] = testbench_name
        return self
    
    def outcome_is(self, **outcome_attributes):
        return self.outcome_is_raw(outcome_attributes)

    @record_call
    def outcome_is_raw(self, outcome_attributes):
        for field_name, value in outcome_attributes.items():
            field = getattr(self.model_type.outcome, field_name)
            self._value_equals[field.name_] = value
        return self
    
    def dut_match(self, id=None, version=None):
        return self.dut_match_raw({'id': id, 'version': version})

    @record_call
    def dut_match_raw(self, id_and_version):
        _id = id_and_version.get('id', None)
        _version = id_and_version.get('version', None)
        if _id is not None:
            self._value_equals[self.model_type.test_id.dut.id.name_] = re.compile(_id)
        if _version is not None:
            self._value_equals[self.model_type.test_id.dut.version.name_] = re.compile(_version)
        return self



    def __eq__(self, other_q):
        same_len = len(self._calls) == len(other_q._calls)
        if not same_len:
            return False

        for key, value in self._calls.items():
            if key not in other_q._calls or other_q._calls[key] != value:
                return False
        
        return True

    def __repr__(self):
        return '{}(eq={}, one-of={}, contains={})'.format(
            self.__class__.__name__,
            repr(self._value_equals),
            repr(self._value_equals_one_of),
            repr(self._list_contains)
        )

    def as_dict(self):
        serializer = get_json_serializer()
        return serializer.serialize(self._calls)

    @classmethod
    def from_dict(cls, _calls):
        query = cls()
        for fn_name, arg in _calls.items():
            query.add_call(fn_name, arg)
        return query

def multi_query_serialize(**queries):
    """ Serialized as key_subkey = subvalue for key key, query in queries.
    """

    result = {}

    for key, query in queries.items():
        if '_' in key:
            raise ValueError('Query key {!r} cannot contain an underscore.'.format(key))
        if query:
            for subkey, subvalue in query.as_dict().items():
                result['{}_{}'.format(key, subkey)] = subvalue
    
    return result

def multi_query_deserialize(_dict):
    queries = defaultdict(Query)

    for key, value in _dict.items():
        query_name, fn_name = split_key(key)
        queries[query_name].add_call(fn_name, value)
    
    return queries

def split_key(key):
    split_key = key.split('_')
    return split_key[0], '_'.join(split_key[1:])