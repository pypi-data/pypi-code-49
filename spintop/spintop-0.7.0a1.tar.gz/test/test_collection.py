from spintop.models.collection import SpintopTestRecordView

def test_default_primitive_test_record(flat_test_record):
    view = SpintopTestRecordView()
    
    result = view.apply(flat_test_record, flatten_dict=False)
    
    assert 'test_id' in result
    
def test_tags_default_primitive_test_record(flat_test_record):
    view = SpintopTestRecordView()
    
    flat_test_record.add_tag('tag1')
    
    result = view.apply(flat_test_record, flatten_dict=False)
    
    assert result['test_id']['tags']['tag1']