import urllib.parse
from logging import Handler

from rest_framework.utils import json

from hologger.middleware import HoLoggingMiddleware


def get_serial_data(record):
    result = {}

    try:
        result['status'] = record.data['response'].status_code
    except (AttributeError, KeyError):
        result['status'] = ""

    try:
        result['host'] = record.data['request'].META['HTTP_HOST']
    except (AttributeError, KeyError):
        result['host'] = ""

    try:
        result['uri'] = urllib.parse.urlparse(record.data['request'].get_full_path()).path
    except (AttributeError, KeyError):
        result['uri'] = ""

    try:
        result['method'] = record.data['request'].method
    except (AttributeError, KeyError):
        result['method'] = ""

    try:
        result['remote_addr'] = record.data['request'].META['REMOTE_ADDR']
    except (AttributeError, KeyError):
        result['remote_addr'] = ""

    try:
        result['header'] = json.dumps(record.data['request'].headers.__dict__['_store'])
    except (AttributeError, KeyError):
        result['header'] = "{}"

    try:
        result['body'] = record.data['body'].decode('utf-8')
    except (AttributeError, KeyError):
        result['body'] = "{}"

    try:
        result['response'] = record.data['response'].content.decode('utf-8')
    except (AttributeError, KeyError):
        result['response'] = "{}"

    try:
        result['pid'] = record.data['pid']
    except (AttributeError, KeyError):
        result['pid'] = None

    try:
        result['queries'] = record.data['query']
    except (AttributeError, KeyError):
        result['queries'] = ""

    return result


class HoLogHandler(Handler):

    def emit(self, record):

        data = get_serial_data(record)
        if data['pid'] is not None:
            from .serializers import ApiResponseSerializer
            serializer = ApiResponseSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
        return


class HoLogSqlHandler(Handler):

    def emit(self, record):
        if hasattr(HoLoggingMiddleware.thread_local, "pid"):
            if not hasattr(HoLoggingMiddleware.thread_local, "query") or HoLoggingMiddleware.thread_local.query is None:
                HoLoggingMiddleware.thread_local.query = ""
            HoLoggingMiddleware.thread_local.query += "\n" + self.format(record)

