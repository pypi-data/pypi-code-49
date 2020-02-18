import xmltodict
import collections
import dateutil.parser

from spintop.models import (
    SpintopTreeTestRecordBuilder
)
from spintop.transforms import Transformer

from ...logs import _logger

logger = _logger('collectors.niatml')

class NiATMLFormatTransformer(Transformer):
    def __call__(self, atml_filename):
        test_record = collect_filename(atml_filename)
        test_results = test_record['trc:TestResultsCollection']['trc:TestResults']
        dut_id = test_results['tr:UUT']['c:SerialNumber']
        result_set = test_results['tr:ResultSet']
        start_datetime = dateutil.parser.parse(result_set.get('@startDateTime'))
        end_datetime = dateutil.parser.parse(result_set.get('@endDateTime'))
        outcome = 'Pass' in result_set.get('tr:Outcome', {}).get('@value')
        
        logger.info('Transforming %s on %s' % (dut_id, start_datetime))
        
        builder = SpintopTreeTestRecordBuilder()
        builder.set_top_level_information(
            start_datetime=dateutil.parser.parse(result_set.get('@startDateTime')),
            dut_id=dut_id,
            testbench_name='testbench',
            duration=(end_datetime-start_datetime).total_seconds(),
            outcome=outcome
        )
        
        collect_all_tests(collect_phase(result_set), builder)
        
        record = builder.build()
        return record

def collect_all_tests(result_set, builder, depth=0):
    if isinstance(result_set, collections.Mapping):
        with attach_phase(result_set, builder) as builder:
            collect_measures(result_set, builder)
            
            # Collect phases to extract start datetime
            # We sort by datetime because Test and TestGroup order were mixed up on xml parse.
            
            tests = collect_one_or_many_phases(result_set.get('tr:Test', []))
            test_groups = collect_one_or_many_phases(result_set.get('tr:TestGroup', []))
            
            phases = sorted(tests + test_groups, key = lambda phase: phase['start_datetime'])
            
            for test_phase in phases:
                collect_all_tests(test_phase, builder, depth=depth+1)

def collect_one_or_many_phases(array):
    return [collect_phase(test_phase) for test_phase in as_array(array)]
    
def as_array(array):
    if not isinstance(array, collections.Sequence):
        # sometimes contains only one test, which will appear as a dict instead of a sequence.
        array = [array]
    return array
    


def make_measure(result):
    return {
        'value': make_value(result)
    }

def make_params(result):
    params = result.get('tr:Parameters', {})
    if params:
        datum = params.get('tr:Parameter', {}).get('tr:Data', {}).get('c:Datum', {})
        value = datum.get('c:Value').split('\\')[-1]
        return [value]
    else:
        return []
    
def make_value(result):
    TYPES = {
        'ts:TS_double': float,
    }
    datum = result.get('tr:TestData', {}).get('c:Datum', {})
    value = datum.get('@value')
    if value is None:
        value = datum.get('c:Value')
    ts_type = datum.get('@xsi:type')
    return TYPES.get(ts_type, lambda x:x)(value)

def collect_measures(test_phase, builder):
    name = test_phase.get('@name')
    
    # Share the outcome with the surrounding test phase
    # which is usually an AcceptanceCriteria
    outcome = make_outcome(test_phase)
        
    results = as_array(test_phase.get('tr:TestResult', []))
    measures = {}
    
    for result in results:
        measure_name = name + ':' + result.get('@name')
        measures[measure_name] = make_measure(result)

    for measure_name, measure_result in measures.items():
        measure = builder.new_measure(
            name=measure_name,
            outcome=outcome,
            value=measure_result['value']
        )
        

def make_outcome(test_phase):
    
    is_skip = 'Skip' in test_phase.get('tr:Outcome', {}).get('@qualifier', '')
    is_pass = is_skip or 'Pass' in test_phase.get('tr:Outcome', {}).get('@value')
    return dict(
        is_pass=is_pass,
        is_skip=is_skip
    )

def collect_phase(test_phase, accept_all=False):
    name = '#'.join([test_phase.get('@name').split('\\')[-1]] + make_params(test_phase))
    
    return dict(
        name = name,
        start_datetime = dateutil.parser.parse(test_phase.get('@startDateTime')),
        end_datetime = dateutil.parser.parse(test_phase.get('@endDateTime')),
        outcome = make_outcome(test_phase),
        **test_phase
    )
    
def attach_phase(collected_phase, builder):
    return builder.new_phase(
        name=collected_phase['name'],
        outcome=collected_phase['outcome'],
        duration=(collected_phase['end_datetime']-collected_phase['start_datetime']).total_seconds(),
    )

def collect_filename(file_stream):
    data = file_stream.read()
    return xmltodict.parse(data)