# -*- coding: utf-8 -*-
from contextlib import contextmanager

import grpc
from google.protobuf.any_pb2 import Any

from . import common_pb2 as c_pb
from . import systemSettingsService_pb2 as ss_pb
from . import systemSettingsService_pb2_grpc as ss_grpc
from .models import (Version, SystemSettingsServiceException, VersionPageList, LowestVersion)


class SystemSettingsServiceGRPCClient:
    _endpoint = None
    _retry_time = 3
    _retry_interval = 2

    def __init__(self, endpoint: str, src: str = ''):
        self._endpoint = endpoint
        self._src = src

    @contextmanager
    def _version_rpc_stub(self):
        with grpc.insecure_channel(self._endpoint) as channel:
            stub = ss_grpc.VersionServiceStub(channel)
            try:
                yield stub
            except grpc.RpcError as e:
                raise SystemSettingsServiceException(str(e))

    @staticmethod
    def _check_response(r: c_pb.ResponseMessage):
        if r.code != 0:
            raise SystemSettingsServiceException("{} {}".format(str(r.code), r.msg))
        return r

    def _build_request(self, request):
        data = Any()
        data.Pack(request)
        return c_pb.RequestMessage(src=self._src, data=data)

    def get_version(self, project_name: ss_pb.ProjectName, id: int) -> Version:
        with self._version_rpc_stub() as stub:
            # 先构建通用 request message
            request = self._build_request(ss_pb.GetVersionRequest(project_name=project_name, id=id))
            resp = self._check_response(stub.GetVersion(request))
            unpacked_msg = ss_pb.VersionMessage()
            resp.data.Unpack(unpacked_msg)
            return Version.from_pb(unpacked_msg)

    def get_latest_version(self, project_name: ss_pb.ProjectName) -> Version:
        with self._version_rpc_stub() as stub:
            req = self._build_request(ss_pb.GetLatestVersionRequest(
                project_name=project_name
            ))
            resp = self._check_response(stub.GetLatestVersion(req))
            unpacked_msg = ss_pb.VersionMessage()
            resp.data.Unpack(unpacked_msg)
            return Version.from_pb(unpacked_msg)

    def is_problem_version(self, project_name: ss_pb.ProjectName, version: str) -> bool:
        with self._version_rpc_stub() as stub:
            req = self._build_request(ss_pb.IsProblemVersionRequest(
                project_name=project_name, version=version
            ))
            resp = self._check_response(stub.IsProblemVersion(req))
            unpacked_msg = ss_pb.IsProblemVersionResponse()
            resp.data.Unpack(unpacked_msg)
            return unpacked_msg.is_problem

    def get_version_list(self, project_name: ss_pb.ProjectName) -> list:
        with self._version_rpc_stub() as stub:
            req = self._build_request(ss_pb.GetVersionListRequest(
                project_name=project_name
            ))
            resp = self._check_response(stub.GetVersionList(req))
            unpacked_msg = ss_pb.GetVersionListResponse()
            resp.data.Unpack(unpacked_msg)
            return [Version.from_pb(t) for t in unpacked_msg.list]

    def get_version_page_list(self, project_name: ss_pb.ProjectName,
                              current_page: int, page_size: int) -> VersionPageList:
        with self._version_rpc_stub() as stub:
            req = self._build_request(ss_pb.GetVersionPageListRequest(
                project_name=project_name, current_page=current_page, page_size=page_size
            ))
            resp = self._check_response(stub.GetVersionPageList(req))
            unpacked_msg = ss_pb.GetVersionPageListResponse()
            resp.data.Unpack(unpacked_msg)
            return VersionPageList.from_pb(unpacked_msg)

    def add_version(self, project_name: ss_pb.ProjectName, version: str, release_date: str,
                    update_content: str, update_mode: ss_pb.VersionModeEnum,
                    update_url: str) -> Version:
        with self._version_rpc_stub() as stub:
            req = self._build_request(ss_pb.AddVersionRequest(
                project_name=project_name, version=version, release_date=release_date,
                update_content=update_content, update_mode=update_mode, update_url=update_url
            ))
            resp = self._check_response(stub.AddVersion(req))
            unpacked_msg = ss_pb.VersionMessage()
            resp.data.Unpack(unpacked_msg)
            return Version.from_pb(unpacked_msg)

    def update_version(self, project_name: ss_pb.ProjectName, id: int, version: str,
                       release_date: str, update_content: str,
                       update_mode: ss_pb.VersionModeEnum, update_url: str) -> None:
        with self._version_rpc_stub() as stub:
            req = self._build_request(ss_pb.EditVersionRequest(
                project_name=project_name, id=id, version=version, release_date=release_date,
                update_content=update_content, update_mode=update_mode, update_url=update_url
            ))
            self._check_response(stub.EditVersion(req))

    def del_version(self, project_name: ss_pb.ProjectName, id: int) -> None:
        with self._version_rpc_stub() as stub:
            req = self._build_request(ss_pb.DelVersionRequest(
                project_name=project_name, id=id
            ))
            self._check_response(stub.DelVersion(req))

    def mark_version(self, project_name: ss_pb.ProjectName, id: int, mark: bool,
                     defects_content: str) -> None:
        with self._version_rpc_stub() as stub:
            req = self._build_request(ss_pb.MarkVersionRequest(
                project_name=project_name, id=id, mark=mark, defects_content=defects_content
            ))
            self._check_response(stub.MarkVersion(req))

    def get_lowest_version(self, project_name: ss_pb.ProjectName) -> LowestVersion:
        with self._version_rpc_stub() as stub:
            req = self._build_request(ss_pb.GetLowestVersionRequest(
                project_name=project_name
            ))
            resp = self._check_response(stub.GetLowestVersion(req))
            unpacked_msg = ss_pb.GetLowestVersionResponse()
            resp.data.Unpack(unpacked_msg)
            return LowestVersion.from_pb(unpacked_msg)

    def update_advise_version(self, project_name: ss_pb.ProjectName, version_id: int):
        with self._version_rpc_stub() as stub:
            req = self._build_request(ss_pb.UpdateAdviseVersionRequest(
                project_name=project_name, id=version_id
            ))
            self._check_response(stub.UpdateAdviseVersion(req))

    def update_force_version(self, project_name: ss_pb.ProjectName, version_id: int):
        with self._version_rpc_stub() as stub:
            req = self._build_request(ss_pb.UpdateForceVersionRequest(
                project_name=project_name, id=version_id
            ))
            self._check_response(stub.UpdateForceVersion(req))
