from openhtf.core.test_record import TestRecord

from spintop.models import SpintopTestRecord

from spintop_openhtf.transforms.openhtf_fmt import OpenHTFTestRecordTransformer
from spintop_openhtf.transforms.openhtf_gen import OpenHTFTestsGenerator


generator = OpenHTFTestsGenerator()
transformer = OpenHTFTestRecordTransformer()

generate_transform = generator + transformer

def test_generate():
    tests = list(generator.generate(count=2))

    assert len(tests) == 2
    assert isinstance(tests[0], TestRecord)

def test_transform():

    spintop_records = list(generate_transform.generate(count=2))

    assert len(spintop_records) == 2
    assert isinstance(spintop_records[0], SpintopTestRecord)

