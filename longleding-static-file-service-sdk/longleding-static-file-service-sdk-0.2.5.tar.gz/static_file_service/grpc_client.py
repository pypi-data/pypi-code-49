# -*- coding: utf-8 -*-
from contextlib import contextmanager

import grpc

from . import common_pb2 as c_pb
from . import staticFileService_pb2 as s_pb
from . import staticFileService_pb2_grpc as s_grpc
from .models import (OSSBucketInfo, StaticFileServiceException,
                     UploadCredentials)


class StaticFileServiceGRPCClient:
    _endpoint = None
    _retry_time = 3
    _retry_interval = 2

    def __init__(self, endpoint):
        self._endpoint = endpoint

    @contextmanager
    def _rpc_stub(self):
        with grpc.insecure_channel(self._endpoint) as channel:
            stub = s_grpc.StaticFileServiceStub(channel)
            try:
                yield stub
            except grpc.RpcError as e:
                raise StaticFileServiceException(str(e))

    def _check_response(self, r: c_pb.ResponseMessage):
        if r.code != 0:
            raise StaticFileServiceException("{} {}".format(str(r.code), r.msg))
        return r

    def get_oss_bucket_info(self) -> OSSBucketInfo:
        with self._rpc_stub() as stub:
            response = self._check_response(stub.GetOSSBucketInfo(c_pb.Empty()))
            unpacked_msg = s_pb.OSSBucketInfoMessage()
            response.data.Unpack(unpacked_msg)
            return OSSBucketInfo.from_pb(unpacked_msg)

    def get_upload_credentials(self) -> UploadCredentials:
        with self._rpc_stub() as stub:
            response = self._check_response(stub.GetUploadCredentials(c_pb.Empty()))
            unpacked_msg = s_pb.UploadCredentialsMessage()
            response.data.Unpack(unpacked_msg)
            return UploadCredentials.from_pb(unpacked_msg)

    def get_file(self, path: str) -> bytes:
        with self._rpc_stub() as stub:
            response = self._check_response(stub.GetFile(s_pb.GetFileRequest(path=path)))
            unpacked_msg = s_pb.GetFileResponse()
            response.data.Unpack(unpacked_msg)
            return unpacked_msg.file

    def get_file_md5(self, path: str) -> str:
        with self._rpc_stub() as stub:
            response = self._check_response(stub.GetFileMD5(s_pb.GetFileMD5Request(path=path)))
            unpacked_msg = s_pb.GetFileMD5Response()
            response.data.Unpack(unpacked_msg)
            return unpacked_msg.md5

    def put_file(self, path: str, file: bytes) -> None:
        with self._rpc_stub() as stub:
            self._check_response(stub.PutFile(s_pb.PutFileRequest(path=path, file=file)))

    def copy_file(self, from_path: str, to_path: str) -> None:
        with self._rpc_stub() as stub:
            self._check_response(stub.CopyFile(s_pb.CopyFileRequest(from_path=from_path, to_path=to_path)))

    def move_file(self, from_path: str, to_path: str) -> None:
        with self._rpc_stub() as stub:
            self._check_response(stub.MoveFile(s_pb.MoveFileRequest(from_path=from_path, to_path=to_path)))
