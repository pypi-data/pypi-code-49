# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Dict, List

from .grpc_client import (OperationLog, OperationLogServiceException,
                          OperationLogServiceGRPCClient, OperationLogPageList)

__all__ = ["init_service", "log", "get_operation_logs", "OperationLogServiceException", "OperationLog"]
_operation_log_service_grpc_client: OperationLogServiceGRPCClient
_source: str = ""


def init_service(endpoint: str, source: str) -> None:
    global _operation_log_service_grpc_client
    global _source
    assert type(endpoint) == str, "endpoint must be a str"
    assert type(source) == str, "source must be a str"
    _operation_log_service_grpc_client = OperationLogServiceGRPCClient(endpoint=endpoint)
    _source = source


def log(time: datetime = datetime.now(),
        topic: str = "",
        tags: Dict[str, str] = {},
        content: str = "") -> None:
    global _operation_log_service_grpc_client
    assert _operation_log_service_grpc_client is not None, "log service sdk must be init first"
    assert type(time) == datetime, "time must be a datetime"
    assert type(topic) == str, "topic must be a str"
    assert type(tags) == dict, "tags must be a dict"
    for k in tags.keys():
        assert type(k) == str, "tags key must be a str"
        assert type(tags[k]) == str, "tags value must be a str"
    assert type(content) == str, "content must be a str"
    global _source
    log_message = OperationLog(time=time, topic=topic, source=_source, tags=tags, content=content)
    _operation_log_service_grpc_client.log(log_message)


def get_operation_logs(start_time: datetime,
                       end_time: datetime,
                       offset: int = 0,
                       limit: int = 0,
                       reverse: bool = False,
                       topic_in: List[str] = [],
                       source_in: List[str] = [],
                       tag_contains: Dict[str, List[str]] = {}) -> OperationLogPageList:
    global _operation_log_service_grpc_client
    assert _operation_log_service_grpc_client is not None, "log service sdk must be init first"
    assert type(start_time) == datetime, "start_time must be a datetime"
    assert type(end_time) == datetime, "end_time must be a datetime"
    assert type(offset) == int, "offset must be an int"
    assert type(limit) == int, "limit must be an int"
    assert type(reverse) == bool, "reverse must be a bool"
    assert type(topic_in) == list, "topic_in must be a list"
    for t in topic_in:
        assert type(t) == str, "topic_in element must be a str"
    assert type(source_in) == list, "source_in must be a list"
    for s in source_in:
        assert type(s) == str, "source_in element must be a str"
    assert type(tag_contains) == dict, "tag_contains must be a dict"
    for k, v in tag_contains.items():
        assert type(k) == str, "tag_contains key must be a str"
        assert type(v) == list, "tag_contains value must be a list"
        for s in v:
            assert type(s) == str, "tag_contains value element must be a str"
    return _operation_log_service_grpc_client.get_logs(start_time, end_time, offset, limit, reverse, topic_in, source_in, tag_contains)
