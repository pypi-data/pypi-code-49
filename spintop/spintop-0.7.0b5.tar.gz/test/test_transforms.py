from unittest.mock import MagicMock
import pytest

from datetime import datetime, timedelta

from spintop.models.internal import DutIDRecord, NO_VERSION
from spintop.transforms import TransformBuilder, DutOp, DutOpLog, join_transforms, transformer

V1_DATETIME = datetime(year=2019, month=1, day=1)
V2_DATETIME = datetime(year=2019, month=2, day=1)

def string_format(datetime):
    return datetime.strftime("%Y-%m-%d %H:%M:%S")

def after(datetime):
    return datetime + timedelta(days=1)

def before(datetime):
    return datetime - timedelta(days=1)

@pytest.fixture()
def op_log():
    log = DutOpLog()
    op1 = DutOp.create(dut_match='my_unit', dut_after={'version': 'v1'}, op_datetime=V1_DATETIME)
    op2 = DutOp.create(dut_match='my_unit', dut_after={'version': 'v2'}, op_datetime=V2_DATETIME)
    
    log.add_op(op2)
    log.add_op(op1)
    return log

def basic_test_on(op_log):
    dut = DutIDRecord.create('my_unit')
    
    assert op_log.get_latest_dut(dut, before(V1_DATETIME)).version == NO_VERSION
    assert op_log.get_latest_dut(dut, after(V1_DATETIME)).version == 'v1'
    assert op_log.get_latest_dut(dut, after(V2_DATETIME)).version == 'v2'

def test_op_log(op_log):
    basic_test_on(op_log)
    
    
def test_op_log_from_dict_ops_by_dut_id_form():
    op_log_dict = dict(
        ops_by_dut_id=dict(
            my_unit=[
                dict(
                    dut_after={'version': 'v1'},
                    op_datetime=string_format(V1_DATETIME)
                ),
                dict(
                    dut_after={'version': 'v2'},
                    op_datetime=string_format(V2_DATETIME)
                )
            ]
        )
    )
    op_log = DutOpLog.from_dict(op_log_dict)
    basic_test_on(op_log)
    
def test_op_log_from_dict_ops_form():
    op_log_dict = dict(
        ops=[
            dict(
                dut_match='my_unit',
                dut_after={'version': 'v1'},
                op_datetime=string_format(V1_DATETIME)
            ),
            dict(
                dut_match='my_unit',
                dut_after={'version': 'v2'},
                op_datetime=string_format(V2_DATETIME)
            )
        ]
    )
    op_log = DutOpLog.from_dict(op_log_dict)
    basic_test_on(op_log)
    
def test_op_log_from_dict_multi_match():
    op_log_dict = dict(
        ops=[
            dict(
                dut_match=['my_unit', 'other_unit'],
                dut_after={'version': 'v1'},
                op_datetime=string_format(V1_DATETIME)
            ),
            dict(
                dut_match='my_unit',
                dut_after={'version': 'v2'},
                op_datetime=string_format(V2_DATETIME)
            )
        ]
    )
    op_log = DutOpLog.from_dict(op_log_dict)
    basic_test_on(op_log)
    
    
def append_arg_transform_factory(arg):
    @transformer
    def _transform(obj):
        return obj + arg
    return _transform

def test_transform_builder_steps():
    builder = TransformBuilder(
        append_arg_transform_factory('a'),
        append_arg_transform_factory('b'),
        append_arg_transform_factory('c')
    )

    assert builder("") == "abc"
    
def test_transform_builder_append():
    builder = TransformBuilder(
        append_arg_transform_factory('a')
    )
    
    builder.append(append_arg_transform_factory('b'))
    
    assert builder("") == "ab"
    
def test_transform_builder_prepend():
    builder = TransformBuilder(
        append_arg_transform_factory('b')
    )
    
    builder.prepend(append_arg_transform_factory('a'))
    
    assert builder("") == "ab"
    
def test_transform_builder_append_prepend():
    builder = TransformBuilder(
        append_arg_transform_factory('b')
    )
    
    builder.prepend(append_arg_transform_factory('a'))
    builder.append(append_arg_transform_factory('c'))
    
    assert builder("") == "abc"
    
def test_transform_builder_split():
    
    b_transform = MagicMock(side_effect=lambda obj: obj + "b")
    
    builder = TransformBuilder(b_transform)
    
    builder_a, builder_c = builder.split(2)
    
    builder_a.prepend(append_arg_transform_factory('a'))
    
    builder_c.append(append_arg_transform_factory('c'))
    
    assert builder_a("") == "ab"
    assert builder_c("") == "bc"
    
    assert b_transform.call_count == 2, "The shared transform should be called twice"
    
def test_transform_builder_append_factories():
    ab_builder = TransformBuilder(
        append_arg_transform_factory('a'),
        append_arg_transform_factory('b')
    )
    
    c_builder = TransformBuilder(
        append_arg_transform_factory('c')
    )
    
    ab_builder.append(c_builder)
    
    assert ab_builder("") == "abc"
    
def test_transform_builder_prepend_factories():
    bc_builder = TransformBuilder(
        append_arg_transform_factory('b'),
        append_arg_transform_factory('c')
    )
    
    a_builder = TransformBuilder(
        append_arg_transform_factory('a')
    )
    
    bc_builder.prepend(a_builder)
    
    assert bc_builder("") == "abc"
    
def test_transform_builder_branch_in_and_out():
    """ 
    +A -> +B \           / +D
              |-> +C -> |
    +C -> +C /           \ +E
    
    Results should be
    - ABCD
    - ABCE
    - CCCD
    - CCCE
    """ 
    
    
    ab = join_transforms(
        append_arg_transform_factory('a'),
        append_arg_transform_factory('b')
    )
    
    cc = join_transforms(
        append_arg_transform_factory('c'),
        append_arg_transform_factory('c')
    )
    
    c = append_arg_transform_factory('c')
    
    d = append_arg_transform_factory('d')
    
    e = append_arg_transform_factory('e')
    
    abcd = ab + c + d
    abce = ab + c + e
    cccd = cc + c + d
    ccce = cc + c + e
    
    assert abcd("") == "abcd"
    assert abce("") == "abce"
    assert cccd("") == "cccd"
    assert ccce("") == "ccce"

@transformer
def append_d_and_e(obj):
    for append in ('d', 'e'):
        yield obj + append

def test_transform_generator():
    """ 
           / +D
    +C -> |
           \ +E
    """

    c = append_arg_transform_factory('c')

    
    cde = c + append_d_and_e
    result = cde.generate("")
    assert list(result) == ['cd', 'ce']


def test_transform_generator_alone():

    result = append_d_and_e.generate("")
    assert list(result) == ['d', 'e']