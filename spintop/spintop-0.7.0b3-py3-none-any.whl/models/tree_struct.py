from copy import copy
from collections import Mapping

from anytree import NodeMixin, RenderTree, PreOrderIter, LevelOrderGroupIter
from anytree.render import ContStyle

from .collection import SpintopTestRecord, SpintopFlatTestRecordBuilder
from .internal import TestIDRecord, OutcomeData, PhaseFeatureRecord, MeasureFeatureRecord, TestRecordSummary, NAME_SEPARATOR
    
class SpintopTestRecordError(Exception): pass
    
class AbstractSpintopTestRecordNode(NodeMixin):
    internal_feature = None
    separator = NAME_SEPARATOR
    
    def __init__(self, name, parent=None, **data):
        self._test_id = None
        
        self.name = name
        self.parent = parent
        self.data = {}
        if data:
            self.define_data(**data)
        
    @property
    def tree_name(self):
        return self.separator.join(p.name for p in self.path)
    
    @property
    def test_id(self):
        return self._test_id
    
    def _set_test_id(self, value):
        # Recursively sets the test id of the whole tree.
        self._test_id = value
        for child in self.children:
            child._set_test_id(value)
            
    def _post_attach(self, parent):
        self._test_id = parent._test_id

    def child_tree_name(self, child_name):
        return self.separator.join([self.tree_name, child_name])
    
    def define_id(self, 
            start_datetime,
            dut_id,
            testbench_name):
        
        test_id = TestIDRecord.create(
            testbench_name,
            dut_id,
            start_datetime
        )
        
        # Find the root, which will recursively set the id of all nodes in the tree.
        self.root._set_test_id(test_id)
        
        
    def define_data(self, **data):
        self._update_data(**data)
        
    def _update_data(self, **data):
        self.data.update(data)
        
    def __repr__(self):
        return "%s(name='%s')" % (self.__class__.__name__, self.name)
    
    def __copy__(self):
        return self.__class__(self.name, parent=None, **self.data)
    
    def to_internal(self, index=0):
        if self.test_id is None:
            raise Exception('The test id must be defined before calling')
        internal_cls = self.internal_feature
        obj = internal_cls(
            oid=None, # New class, not bound to any stored one.
            name=self.name,
            version=0,
            depth=self.depth,
            index=index,
            ancestors=[node.name for node in self.path[:-1]],
            original=True,
            test_id=self.test_id,
            user_data={},
            **self._data_for_internal()
        )
        return obj
        
    def _data_for_internal(self):
        return self.data
        
class Phase(AbstractSpintopTestRecordNode):
    internal_feature = PhaseFeatureRecord
    def define_data(self, outcome, duration):
        super(Phase, self).define_data(
            outcome=make_outcome(outcome), 
            duration=duration
        )
    
class Measure(AbstractSpintopTestRecordNode):
    internal_feature = MeasureFeatureRecord
    def define_data(self, outcome, value):
        super(Measure, self).define_data(
            outcome=make_outcome(outcome), 
            value=value
        )
        
class PhasesView(Phase):
    """ Allows to group multiple phases into one. Outcomes are boolean AND and durations are summed.
    """
    phases = []
    
    def define_data(self, wrapped_phases):
        outcome = all([phase.data.get('outcome', True) for phase in wrapped_phases])
        duration = sum([phase.data.get('duration', 0) for phase in wrapped_phases])
        super(PhasesView, self).define_data(outcome=outcome, duration=duration)
        
class SpintopTreeTestRecord(Phase):
    internal_feature = TestRecordSummary
    def __init__(self):
        super(SpintopTreeTestRecord, self).__init__('', parent=None)
    
    def _data_for_internal(self):
        return dict(
            **self.data
        )
    
    def flatten_data(self):
        builder = SpintopFlatTestRecordBuilder(
            data = self.to_internal(),
            features = [node.to_internal(index-1) for index, node in enumerate(PreOrderIter(self)) if node is not self]
        )
        return builder.build()
    
    def pprint(self):
        print(RenderTree(self, style=ContStyle()))
        
    def group_outcomes(self, depth=1):
        for nodes in LevelOrderGroupIter(self, maxlevel=depth):
            if nodes[0].depth < depth-1:
                continue
            else:
                current_group = []
                for node in nodes:
                    if node.data.get('outcome', True):
                        current_group.append(node)
                    else:
                        if current_group:
                            yield current_group, True
                            current_group = []
                    
                        yield [node], False
        
                if current_group:
                    yield current_group, True
                
        

class SpintopTestRecordBuilderContext(object):
    def __init__(self, ensure_unique_names=True):
        self._should_ensure_unique_names = ensure_unique_names
        self._duplicate_key_index = {}
        self._unique_ensured_nodes = {}
        
    def ensure_unique_key(self, key, parent):
        unique_name = parent.child_tree_name(key)
        if self._should_ensure_unique_names and unique_name in self._unique_ensured_nodes:
            suffix = self._duplicate_key_index.get(unique_name, 0)
            self._duplicate_key_index[unique_name] = suffix + 1
            key = key + str(suffix)
            return self.ensure_unique_key(key, parent)
        return key
    
    def add_unique_node(self, node):
        self._unique_ensured_nodes[node.tree_name] = node
    
class SpintopTreeTestRecordBuilder(object):
    def __init__(self, node=None, context=None, **context_kwargs):
        if node is None:
            node = SpintopTreeTestRecord()
        if context is None:
            context = SpintopTestRecordBuilderContext(**context_kwargs)
            
        self.node = node
        self.context = context
    
    def __enter__(self):
        if self.node.parent is None:
            raise SpintopTestRecordError('Cannot use the top level node as a context manager')
        return self
    
    def __exit__(self, *args, **kwargs):
        pass
    
    @property
    def test_record(self):
        return self.node.root
    
    def build(self):
        return self.test_record.flatten_data()
    
    def set_top_level_information(self, 
            start_datetime,
            dut_id,
            testbench_name,
            outcome=None,
            duration=None):
        
        top_level_node = self.test_record
        
        top_level_node.define_id(
            start_datetime,
            dut_id,
            testbench_name
        )
        
        top_level_node.define_data(
            outcome=outcome,
            duration=duration
        )
        
    def new_phase(self, name, outcome, duration):
        return self._new_node(Phase, name,
            outcome=outcome,
            duration=duration
        )
    
    def new_measure(self, name, outcome, value):
        return self._new_node(Measure, name,
            outcome=outcome,
            value=value
        )
    
    def _new_node(self, cls, name, **data):
        name = self.context.ensure_unique_key(name, parent=self.node)
        node = cls(name, parent=self.node, **data)
        self.context.add_unique_node(node)
        return self._wrap(node)
    
    def _wrap(self, node):
        return self.__class__(node, self.context)
    

def make_outcome(outcome):
    if isinstance(outcome, bool):
        outcome = OutcomeData(is_pass=outcome)
    elif isinstance(outcome, Mapping):
        outcome = OutcomeData(**outcome)
    else:
        raise TypeError((
'Outcome (%s) should either be a boolean that indicates if this test passed or failed, ' 
'or a dictionnary of one or more of the following attributes: %s'
        ) % (outcome, [f.name for f in OutcomeData.get_fields()]))
    return outcome