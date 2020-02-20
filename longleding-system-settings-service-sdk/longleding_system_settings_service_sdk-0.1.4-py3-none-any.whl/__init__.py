# -*- coding: utf-8 -*-
import datetime
import inspect

from .models import UPDATE_CONTENT_MAX_LENGTH, DEFECTS_CONTENT_MAX_LENGTH
from .grpc_client import SystemSettingsServiceGRPCClient
from .models import (Version, SystemSettingsServiceException,
                     VersionPageList, LowestVersion)
from .systemSettingsService_pb2 import ProjectName

__all__ = [
    "init_service",
    "SystemSettingsServiceException",
    "get_version_doc_shot",
    "get_last_version_doc_shot",
    "is_problem_version_doc_shot",
    "get_version_list_doc_shot",
    "get_version_page_list_doc_shot",
    "add_version_doc_shot",
    "del_version_doc_shot",
    "update_version_doc_shot",
    "mark_version_doc_shot",
    "get_lowest_version_doc_shot",
    "update_advise_version_doc_shot",
    "update_force_version_doc_shot"
]

_client: SystemSettingsServiceGRPCClient


def _param_check(func):
    def wrapper(*args, **kwargs):
        global _client
        assert _client is not None, "system settings service sdk must be init first"
        sig = inspect.signature(func)
        params = list(sig.parameters.values())
        for i, v in enumerate(args):
            p = params[i]
            assert p.annotation is inspect.Parameter.empty or isinstance(v, p.annotation), "{} must be {}.".format(
                p.name, str(p.annotation))
        return func(*args, **kwargs)

    return wrapper


def init_service(endpoint: str, src: str) -> None:
    global _client
    assert type(endpoint) == str, "endpoint must be a str"
    _client = SystemSettingsServiceGRPCClient(endpoint=endpoint, src=src)


@_param_check
def get_version_doc_shot(id: int) -> Version:
    """获取某个某个版本的信息详情"""
    return _client.get_version(ProjectName.PROJECT_NAME_DOC_SHOT, id)


@_param_check
def get_last_version_doc_shot() -> Version:
    """获取某个项目最后一个版本信息详情"""
    return _client.get_latest_version(ProjectName.PROJECT_NAME_DOC_SHOT)


@_param_check
def is_problem_version_doc_shot(version: str) -> bool:
    """判断某个项目的某一个版本是否是问题版本"""
    return _client.is_problem_version(ProjectName.PROJECT_NAME_DOC_SHOT, version)


@_param_check
def get_version_list_doc_shot() -> list:
    """获取某个项目下所有版本列表，不分页"""
    return _client.get_version_list(ProjectName.PROJECT_NAME_DOC_SHOT)


@_param_check
def get_version_page_list_doc_shot(current_page: int, page_size: int) -> VersionPageList:
    """获取某个项目的版本列表，分页信息，返回VersionPageList对象"""
    return _client.get_version_page_list(ProjectName.PROJECT_NAME_DOC_SHOT, current_page, page_size)


@_param_check
def add_version_doc_shot(version: str, release_date: str, update_mode: int,
                         update_content: str = '', update_url: str = '') -> Version:
    """为某个项目新增版本信息"""
    _validate_date_str(release_date)
    _validate_version_str(version)
    if len(update_content) > UPDATE_CONTENT_MAX_LENGTH:
        raise SystemSettingsServiceException('更新内容描述长度超出限制')
    return _client.add_version(
        project_name=ProjectName.PROJECT_NAME_DOC_SHOT,
        version=version,
        release_date=release_date,
        update_mode=update_mode,
        update_content=update_content,
        update_url=update_url
    )


@_param_check
def update_version_doc_shot(version_id: int, version: str, release_date: str, update_mode: int,
                            update_content: str = '', update_url: str = '') -> None:
    """更新某个项目的某个版本的信息"""
    _validate_date_str(release_date)
    _validate_version_str(version)
    if len(update_content) > UPDATE_CONTENT_MAX_LENGTH:
        raise SystemSettingsServiceException('更新内容描述长度超出限制')
    _client.update_version(
        project_name=ProjectName.PROJECT_NAME_DOC_SHOT,
        id=version_id,
        version=version,
        release_date=release_date,
        update_mode=update_mode,
        update_content=update_content,
        update_url=update_url
    )


@_param_check
def del_version_doc_shot(version_id: int) -> None:
    """删除某个项目的一个版本"""
    _client.del_version(ProjectName.PROJECT_NAME_DOC_SHOT, version_id)


@_param_check
def mark_version_doc_shot(version_id: int, mark: bool,
                          defects_content: str) -> None:
    """标记问题版本"""
    if len(defects_content) > DEFECTS_CONTENT_MAX_LENGTH:
        raise SystemSettingsServiceException('问题描述内容长度超出限制')
    _client.mark_version(ProjectName.PROJECT_NAME_DOC_SHOT, version_id, mark, defects_content)


@_param_check
def get_lowest_version_doc_shot() -> LowestVersion:
    """获取某个项目最低要求版本信息，包括建议最低版本和强制最低版本"""
    return _client.get_lowest_version(ProjectName.PROJECT_NAME_DOC_SHOT)


@_param_check
def update_advise_version_doc_shot(version_id: int) -> None:
    """修改某个项目的建议更细最低版本"""
    _client.update_advise_version(
        project_name=ProjectName.PROJECT_NAME_DOC_SHOT,
        version_id=version_id
    )


@_param_check
def update_force_version_doc_shot(version_id: int) -> None:
    """修改某个项目的强制更新的最低版本"""
    _client.update_force_version(
        project_name=ProjectName.PROJECT_NAME_DOC_SHOT,
        version_id=version_id
    )


def _validate_date_str(the_date: str):
    """验证字符串日期是否有效"""
    try:
        temp = [int(t) for t in the_date.split('-')]
        datetime.date(*temp)
    except (ValueError, TypeError):
        raise SystemSettingsServiceException('发布日期不合法')


def _validate_version_str(version: str):
    try:
        version_info = [int(t) for t in version.split('.')]
        if len(version_info) != 3:
            raise SystemSettingsServiceException('版本号不合法')
    except ValueError:
        raise SystemSettingsServiceException('版本号不合法')
