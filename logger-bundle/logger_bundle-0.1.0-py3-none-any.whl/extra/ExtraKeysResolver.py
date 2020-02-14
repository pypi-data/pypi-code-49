class ExtraKeysResolver:

    ignoredRecordKeys = [
        'name', 'msg', 'args', 'created', 'exc_info', 'exc_text', 'filename', 'funcName', 'levelname', 'levelno', 'lineno',
        'module', 'msecs', 'pathname', 'process', 'processName', 'relativeCreated', 'stack_info', 'thread', 'threadName'
    ]

    @staticmethod
    def getExtraKeys(record):
        return record.__dict__.keys() - ExtraKeysResolver.ignoredRecordKeys
