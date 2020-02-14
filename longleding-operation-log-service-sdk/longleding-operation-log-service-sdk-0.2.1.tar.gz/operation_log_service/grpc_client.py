# -*- coding: utf-8 -*-
import json
import time as time_b
from datetime import datetime, timedelta, timezone
from typing import Dict, List

import grpc
from google.protobuf.timestamp_pb2 import Timestamp

from . import operationLogService_pb2, operationLogService_pb2_grpc


class OperationLogServiceException(Exception):
    """ Operation Log Service Exception. """

    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def __new__(*args, **kwargs):
        pass


class OperationLog:
    def __init__(self, time: datetime, topic: str, source: str, tags: Dict[str, str], content: str):
        self.time = time
        self.topic = topic
        self.source = source
        self.tags = tags
        self.content = content

    @classmethod
    def from_pb(cls, log_message: operationLogService_pb2.OperationLogMessage):
        time = datetime.fromtimestamp(log_message.time.seconds)
        time.replace(tzinfo=timezone(timedelta(hours=8)))
        return cls(time, log_message.topic, log_message.source, dict(log_message.tags), log_message.content)

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        assert type(value) == datetime, "time must be a datetime"
        self._time = value

    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self, value):
        assert type(value) == str, "topic must be a str"
        self._topic = value

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        assert type(value) == str, "source must be a str"
        self._source = value

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        assert type(value) == dict, "tags must be a dict"
        for k in value.keys():
            assert type(k) == str, "tags key must be a str"
            assert type(value[k]) == str, "tags value must be a str"
        self._tags = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        assert type(value) == str, "content must be a str"
        self._content = value

    def _desc(self):
        return "<OperationLog(Time:{} Topic:{} Source:{} Tags:{} Content:{})>".format(
            self.time.strftime('%Y-%m-%dT%H:%M:%S+08:00'),
            self.topic,
            self.source,
            json.dumps(self.tags),
            self.content
        )

    def __str__(self):
        return self._desc()

    def __repr__(self):
        return self._desc()


class OperationLogPageList:
    def __init__(self, total: int, logs: List[OperationLog]):
        self.logs = logs
        self.total = total

    @classmethod
    def from_pb(cls, log_message: operationLogService_pb2.OperationLogMessage):
        return cls(log_message.total, [OperationLog.from_pb(l) for l in log_message.logs])

    @property
    def logs(self):
        return self._logs

    @logs.setter
    def logs(self, value):
        assert type(value) == list, "logs must be a list"
        self._logs = value

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        assert type(value) == int, "total must be a int"
        self._total = value

    def _desc(self):
        return "<OperationLogPageList(Total:{} Logs:{})>".format(
            self.total,
            self.logs
        )

    def __str__(self):
        return self._desc()

    def __repr__(self):
        return self._desc()


class OperationLogServiceGRPCClient:
    _endpoint = None
    _retry_time = 3
    _retry_interval = 2

    def __init__(self, endpoint):
        self._endpoint = endpoint

    def log(self, log_message: OperationLog):
        with grpc.insecure_channel(self._endpoint) as channel:
            stub = operationLogService_pb2_grpc.OperationLogServiceStub(channel)
            time_seconds = time_b.mktime(log_message.time.timetuple())
            timestamp = Timestamp(
                seconds=int(time_seconds),
                nanos=0
            )
            log_dict = {
                "time": timestamp,
                "topic": log_message.topic,
                "source": log_message.source,
                "tags": log_message.tags,
                "content": log_message.content
            }
            log_message = operationLogService_pb2.OperationLogMessage(**log_dict)
            response = None
            error = None
            for i in range(self._retry_time):
                try:
                    response = stub.Log(log_message)
                    break
                except grpc.RpcError as e:
                    error = e
                    time_b.sleep(self._retry_interval * (i + 1))
            if response is None:
                raise error
            if response.code != 0:
                raise OperationLogServiceException(response.msg)
            return response

    def get_logs(self,
                 start_time: datetime,
                 end_time: datetime,
                 offset: int = 0,
                 limit: int = 0,
                 reverse: bool = False,
                 topic_in: list = [],
                 source_in: list = [],
                 tag_contains: Dict[str, List[str]] = {}) -> OperationLogPageList:
        with grpc.insecure_channel(self._endpoint) as channel:
            stub = operationLogService_pb2_grpc.OperationLogServiceStub(channel)

            start_time_seconds = time_b.mktime(start_time.timetuple())
            end_time_seconds = time_b.mktime(end_time.timetuple())
            start_timestamp = Timestamp(
                seconds=int(start_time_seconds),
                nanos=0
            )
            end_timestamp = Timestamp(
                seconds=int(end_time_seconds),
                nanos=0
            )

            tag_contains_message = {}
            for k, v in tag_contains.items():
                tag_contains_message[k] = operationLogService_pb2.GetOperationLogsRequest.ListOfString(value_in=v)
            request = operationLogService_pb2.GetOperationLogsRequest(
                start_time=start_timestamp,
                end_time=end_timestamp,
                offset=offset,
                limit=limit,
                reverse=reverse,
                topic_in=topic_in,
                source_in=source_in,
                tag_contains=tag_contains_message,
            )
            response = None
            error = None
            for i in range(self._retry_time):
                try:
                    response = stub.GetOperationLogs(request)
                    break
                except grpc.RpcError as e:
                    error = e
                    time_b.sleep(self._retry_interval * (i + 1))
            if response is None:
                raise error
            if response.code != 0:
                raise OperationLogServiceException(response.msg)

            unpacked_msg = operationLogService_pb2.GetOperationLogsResponse()
            response.data.Unpack(unpacked_msg)
            return OperationLogPageList.from_pb(unpacked_msg)
