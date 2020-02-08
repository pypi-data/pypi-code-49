import pytest

from datetime import datetime
from spintop import models 
from spintop.models.internal import DutOp, DutIDRecord, NO_VERSION, MeasureFeatureRecord, TestIDRecord, BaseDataClass, DefaultPrimitiveView


from spintop.models.view import ComplexPrimitiveView, DataClassPrimitiveView


def test_simple_tree_test():
    builder = models.SpintopTreeTestRecordBuilder()
    builder.set_top_level_information(
        start_datetime = datetime(year=2020, month=1, day=1),
        dut_id = 'dut_id',
        testbench_name = 'testbench_name',
        outcome=True,
        duration=0.2
    )
    
    with builder.new_phase('test1', True, 0.2) as test1:
        test1.new_measure('test1_measure', True, 4.5)
        
def test_dut_op_strings():
    op = DutOp.create('match', 'new', op_datetime=datetime(year=2019, month=1, day=1))
    dut = DutIDRecord.create('match')
    
    assert op.does_applies_to(dut, on_datetime=datetime(year=2019, month=2, day=1)) # One month later
    assert not op.does_applies_to(dut, on_datetime=datetime(year=2018, month=1, day=1)) # One year previous: does not apply.
    
def test_dut_op_match():
    op = DutOp.create('match', 'new', op_datetime=datetime(year=2019, month=1, day=1))
    match_dut = DutIDRecord.create('match')
    no_match_dut = DutIDRecord.create('no_match')
    
    assert op.does_applies_to(match_dut, on_datetime=datetime(year=2019, month=2, day=1)) # One month later
    assert not op.does_applies_to(no_match_dut, on_datetime=datetime(year=2019, month=2, day=1)) # One month later
    
def test_dut_op_match_version():
    op = DutOp.create({'id': 'match', 'version': 'match_v'}, 'new', op_datetime=datetime(year=2019, month=1, day=1))
    match_dut = DutIDRecord.create('match', version='match_v')
    no_match_dut = DutIDRecord.create('match', version='no_match_v')
    
    assert op.does_applies_to(match_dut, on_datetime=datetime(year=2019, month=2, day=1)) # One month later
    assert not op.does_applies_to(no_match_dut, on_datetime=datetime(year=2019, month=2, day=1)) # One month later
    
    assert op.apply(match_dut).version == NO_VERSION, "The after_dut has no version, the version should be None."

def test_meta_class_field_access():
    assert DutIDRecord.version.name_ == 'version'

def test_nested_field_access():
    assert TestIDRecord.dut.id.name_ == 'dut.id'
    
A_TEST_ID_RECORD = TestIDRecord(
    testbench_name = 'foo',
    dut= DutIDRecord(id='x', version='0'),
    test_uuid= 'unique',
    tags= {'my-tag': True},
    start_datetime= datetime(year=2019, month=2, day=1)
)

def create_a_view(*args, **kwargs):
    primitive_view = ComplexPrimitiveView(BaseDataClass, *args, **kwargs)
    primitive_view.add_view(
        TestIDRecord, 
        {
            'testbench_name': TestIDRecord.testbench_name,
            'dut': TestIDRecord.dut
        }
    )
    primitive_view.add_view(
        DutIDRecord,
        {
            'serial': DutIDRecord.id
        }
    )
    return primitive_view
    
def test_data_primitive_view_deep():
    test_id = A_TEST_ID_RECORD
    
    # primitive_view = ComplexPrimitiveView(cls_missing_view_fn=lambda cls: cls.get_default_view())
    primitive_view = create_a_view()
    
    raw_data = primitive_view.apply(test_id)
    
    assert raw_data == {
        'testbench_name': test_id.testbench_name,
        'dut': {
            'serial': test_id.dut.id
        }
    }
    
def test_data_primitive_view_flatten():
    test_id = A_TEST_ID_RECORD
    
    # primitive_view = ComplexPrimitiveView(cls_missing_view_fn=lambda cls: cls.get_default_view())
    primitive_view = create_a_view()
    
    raw_data = primitive_view.apply(test_id, flatten_dict=True)
    
    assert raw_data == {
        ('testbench_name',): test_id.testbench_name,
        ('dut', 'serial'): test_id.dut.id
    }
    
def test_data_primitive_view_defaults():
    test_id = A_TEST_ID_RECORD
    
    primitive_view = DefaultPrimitiveView()
    raw_data = primitive_view.apply(test_id, flatten_dict=True)
    
    assert raw_data == {
        ('testbench_name',): test_id.testbench_name,
        ('dut', 'id'): test_id.dut.id,
        ('dut', 'version'): test_id.dut.version,
        ('test_uuid',): test_id.test_uuid,
        ('tags', 'my-tag'): test_id.tags['my-tag'],
        ('start_datetime',): test_id.start_datetime,
    }
    
def test_data_primitive_view_deepen():
    test_id = A_TEST_ID_RECORD
    
    # primitive_view = ComplexPrimitiveView(cls_missing_view_fn=lambda cls: cls.get_default_view())
    primitive_view = create_a_view()
    
    raw_data_one_level = primitive_view.apply(test_id, key_prefix=('one',))
    
    assert raw_data_one_level == {
        'one': {
            'testbench_name': test_id.testbench_name,
            'dut': {
                'serial': test_id.dut.id
            }
        }
    }
    
    raw_data_two_levels = primitive_view.apply(test_id, key_prefix=('one', 'two'))
    
    assert raw_data_two_levels == {
        'one': {
            'two': {
                'testbench_name': test_id.testbench_name,
                'dut': {
                    'serial': test_id.dut.id
                }
            }
        }
    }
    
def test_data_primitive_view_flatten_key_prefix():
    test_id = A_TEST_ID_RECORD
    
    # primitive_view = ComplexPrimitiveView(cls_missing_view_fn=lambda cls: cls.get_default_view())
    primitive_view = create_a_view()
    
    raw_data = primitive_view.apply(test_id, flatten_dict=True, key_prefix=('one',))
    
    assert raw_data == {
        ('one', 'testbench_name',): test_id.testbench_name,
        ('one', 'dut', 'serial'): test_id.dut.id
    }
    
def test_data_primitive_key_prefix_callable():
    primitive_view = ComplexPrimitiveView(BaseDataClass)
    primitive_view.add_view(
        DutIDRecord,
        {
            (lambda feat: 'deep',): DutIDRecord.id
        }
    )
    
    dut = DutIDRecord(id='x', version='0')
    raw_data = primitive_view.apply(dut, key_prefix=(lambda feat: 'serial',), flatten_dict=True)
    
    assert raw_data == {
        ('serial', 'deep'): 'x'
    }
    
    