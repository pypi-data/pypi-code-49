# -*- coding: utf-8 -*-
import inspect

from .grpc_client import StaticFileServiceGRPCClient
from .models import (OSSBucketInfo, StaticFileServiceException,
                     UploadCredentials)

__all__ = [
    "init_service",
    "StaticFileServiceException",
    "UploadCredentials",
    "OSSBucketInfo",
    "get_oss_bucket_info",
    "get_upload_credentials",
    "get_file",
    "get_file_md5",
    "put_file",
    "copy_file",
    "move_file"
    ]
_client: StaticFileServiceGRPCClient


def _param_check(func):
    def wrapper(*args, **kwargs):
        global _client
        assert _client is not None, "static file service sdk must be init first"
        sig = inspect.signature(func)
        params = list(sig.parameters.values())
        for i, v in enumerate(args):
            p = params[i]
            assert p.annotation is inspect.Parameter.empty or isinstance(v, p.annotation), "{} must be {}.".format(p.name, str(p.annotation))
        return func(*args, **kwargs)
    return wrapper


def init_service(endpoint: str) -> None:
    global _client
    assert type(endpoint) == str, "endpoint must be a str"
    _client = StaticFileServiceGRPCClient(endpoint=endpoint)


@_param_check
def get_oss_bucket_info() -> OSSBucketInfo:
    return _client.get_oss_bucket_info()


@_param_check
def get_upload_credentials() -> UploadCredentials:
    return _client.get_upload_credentials()


@_param_check
def get_file(path: str) -> bytes:
    return _client.get_file(path)


@_param_check
def get_file_md5(path: str) -> str:
    return _client.get_file_md5(path)


@_param_check
def put_file(path: str, file: bytes) -> None:
    _client.put_file(path, file)


@_param_check
def copy_file(from_path: str, to_path: str) -> None:
    _client.copy_file(from_path=from_path, to_path=to_path)


@_param_check
def move_file(from_path: str, to_path: str) -> None:
    _client.move_file(from_path=from_path, to_path=to_path)
