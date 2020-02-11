class ForceTestbenchNameTransformer(object):
    def __init__(self, testbench_name):
        self.testbench_name = testbench_name
    
    def __call__(self, test_record):
        test_record.test_id.testbench_name = self.testbench_name
        return test_record