import logging
from django.conf import settings
from log_labeler import local, DEFAULT_HEADER_VALUE, LOG_LABEL_REQUEST_SETTING


class HeaderToLabelFilter(logging.Filter):
    def filter(self, record):
        if hasattr(settings, LOG_LABEL_REQUEST_SETTING) and isinstance(getattr(settings, LOG_LABEL_REQUEST_SETTING), dict):
            for label in getattr(settings, LOG_LABEL_REQUEST_SETTING):
                header_value = getattr(local, label, DEFAULT_HEADER_VALUE)
                setattr(record, label, header_value)
                if isinstance(record.msg, dict):
                    if "_log_identifier" not in record.msg:
                        record.msg["_log_identifier"] = dict()
                    record.msg["_log_identifier"][label] = header_value
        return True
