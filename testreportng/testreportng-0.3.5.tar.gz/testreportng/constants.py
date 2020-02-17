class Label(object):
    LABEL_NAME: str = "name"

    # count
    LABEL_TOTAL: str = "total"

    # status
    LABEL_STATUS_INIT: str = "init"
    LABEL_STATUS_PASS: str = "pass"
    LABEL_STATUS_FAIL: str = "fail"
    LABEL_STATUS_ERROR: str = "error"
    LABEL_STATUS_SKIP: str = "skip"

    # others
    LABEL_CASE_NAME: str = "name"
    LABEL_PASS_RATE: str = "pass_rate"
    LABEL_STATUS: str = "status"
    LABEL_REASON: str = "reason"
    LABEL_ERROR: str = "error"
    LABEL_TRACEBACK: str = "traceback"
    LABEL_START_TIME: str = "start_time"
    LABEL_END_TIME: str = "end_time"
    LABEL_DURATION: str = "duration"
