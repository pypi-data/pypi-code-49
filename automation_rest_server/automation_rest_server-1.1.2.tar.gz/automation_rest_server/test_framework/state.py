
class State(object):
    FAIL = 0
    PASS = 1
    NOT_START = 2
    RUNNING = 3
    ABORT = 4

    ERROR_NOT_FOUND = 11
    ERROR_BASE_EXCEPTION = 12
    ERROR_TIMEOUT = 13
    ERROR_CONNECTION = 14
    ERROR_ABNORMAL_END = 15

    verdicts_map = {
        FAIL: "FAIL",
        PASS: "PASS",
        NOT_START: "NOT_START",
        RUNNING: "RUNNING",
        ABORT: "ABORT",
        ERROR_NOT_FOUND: "ERROR_NOT_FOUND",
        ERROR_BASE_EXCEPTION: "ERROR_BASE_EXCEPTION",
        ERROR_TIMEOUT: "ERROR_TIMEOUT",
        ERROR_CONNECTION: "ERROR_CONNECTION",
        ERROR_ABNORMAL_END: "ERROR_ABNORMAL_END"
    }

    def __init__(self):
        pass


class TestType(object):

    TestCase = 1
    TestSuite = 2
    TestBenchmark = 3

    def __init__(self):
        pass
