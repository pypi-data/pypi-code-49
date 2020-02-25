import dateutil.parser

from collections import defaultdict, Sequence

from spintop.models import (
    SpintopTestRecordCollection
)
from spintop.models.internal import DutOp

from .base import Transformer

from ..utils import load_yaml_file
from ..logs import _logger

logger = _logger('transforms.op_log')

def and_(*transformers):
    """Record transformer that calls all transformers in order."""
    def call_all_transformers(value):
        for transformer in transformers:
            value = transformer(value)
        return value
    return call_all_transformers
        
class DutOpLog(object):
    def __init__(self):
        self.dut_ops = defaultdict(list)
    
    @classmethod
    def from_yaml(cls, yaml_filename):
        """
        """
        content = load_yaml_file(yaml_filename)
        return cls.from_dict(content)
    
    @classmethod
    def from_dict(cls, content):
        """ Can contain two keys:
        
        ops_by_dut_id: A dut_id indexed list of operations
        ops: A list of operation
        
        (in yaml format)
        ops:
          - dut_match: 'my_unit'
            dut_after: 
                id: 'my_unit' # optional
                version: 'my_version'
            op_datetime: '2018-02-11 11:02:57'
          - (other ops...)
          
        OR
        
        ops_by_dut_id:
            my_unit:
                - dut_after:
                    version: 'my_version'
                  op_datetime: '2018-02-11 11:02:57'
        """
        
        ops = content.get('ops', None)
        ops_by_dut_id = content.get('ops_by_dut_id', None)
        if ops:
            return cls._parse_ops_array(ops)
        elif ops_by_dut_id:
            return cls._parse_ops_by_dut_id_dict(ops_by_dut_id)
        else:
            raise ValueError('Dict content must have either a ops or ops_by_dut_id top-level key. Received keys: {}'.format(
                list(content.keys())
            ))
        
    
    @classmethod
    def _parse_ops_by_dut_id_dict(cls, ops_dict):
        all_ops = []
        for dut_match, ops in ops_dict.items():
            for op in ops:
                if 'dut_match' not in op:
                    op['dut_match'] = dut_match
            all_ops += ops
        
        return cls._parse_ops_array(all_ops)
        
    
    @classmethod
    def _parse_ops_array(cls, ops_list):
        op_log = cls()
        for op in ops_list:
            datetime_str = op['op_datetime']
            dut_matches = op['dut_match']
            
            if not isinstance(dut_matches, Sequence) or isinstance(dut_matches, str):
                dut_matches = [dut_matches]
            
            dut_after = op['dut_after']
            
            for dut_match in dut_matches:
                op = DutOp.create(dut_match, dut_after, dateutil.parser.parse(datetime_str))
                op_log.add_op(op)
        return op_log
    
    def add_op(self, dut_op):
        key = dut_op.dut_match.id
        self.dut_ops[key].append(dut_op)
        self.dut_ops[key].sort(key=lambda op: op.op_datetime, reverse=True)
        
    def get_latest_dut(self, dut, on_datetime):
        ops = self.dut_ops[dut.id]
        for op in ops:
            if op.does_applies_to(dut, on_datetime):
                return op.apply(dut)
        # No op match
        return dut
        

class DutOpLogTransformer(Transformer):
    """Record transformer that attaches version information to DUTs
    based on an operation log."""
    def __init__(self, op_log):
        self.op_log = op_log
        
    def __call__(self, test_record):
        on_datetime = test_record.test_id.start_datetime
        dut = test_record.test_id.dut
        
        new_dut = self.op_log.get_latest_dut(dut, on_datetime)
        
        if new_dut != test_record.test_id.dut:
            logger.info('Applied operation on {} @ {} to become {}'.format(
                test_record.test_id.dut,
                test_record.test_id.start_datetime,
                new_dut
            ))
        else:
            logger.debug('No operation applied on {} @ {}'.format(
                test_record.test_id.dut,
                test_record.test_id.start_datetime
            ))
        
        test_record.test_id.dut = new_dut
        return test_record


        