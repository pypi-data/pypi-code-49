# -*- coding: utf-8 -*-
from enum import Enum, unique

from .systemSettingsService_pb2 import VersionMessage, GetLowestVersionResponse, GetVersionPageListResponse
from .systemSettingsService_pb2 import VersionModeEnum as PBVersionModeEnum


class SystemSettingsServiceException(Exception):
    pass


@unique
class VersionModeEnum(Enum):
    """版本更新动作枚举"""
    DOWNLOAD = 1
    WEB_PAGE = 2
    APP_STORE = 3


UPDATE_CONTENT_MAX_LENGTH = 1000
DEFECTS_CONTENT_MAX_LENGTH = 100


class Version:

    def __init__(self, id: int, version: str, release_date: str,
                 update_content: str, update_mode: int, update_url: str,
                 is_problem: bool, defects_content: str):
        self.id = id
        self.version = version
        self.release_date = release_date
        self.update_content = update_content
        self.update_url = update_url
        self.is_problem = is_problem
        self.defects_content = defects_content
        if update_mode == PBVersionModeEnum.VERSION_MODE_DOWNLOAD:
            self.update_mode = VersionModeEnum.DOWNLOAD
        elif update_mode == PBVersionModeEnum.VERSION_MODE_WEB_PAGE:
            self.update_mode = VersionModeEnum.WEB_PAGE
        elif update_mode == PBVersionModeEnum.VERSION_MODE_APP_STORE:
            self.update_mode = VersionModeEnum.APP_STORE
        else:
            raise SystemSettingsServiceException('版本更新类型错误')

    @classmethod
    def from_pb(cls, version: VersionMessage):
        return cls(
            version.id, version.version, version.release_date,
            version.update_content, version.update_mode, version.update_url,
            version.is_problem, version.defects_content
        )

    def _desc(self):
        return "<Version(id:{} version:{} release_date:{} update_content:{} update_mode:{} " \
               "update_url:{} is_problem:{}) defects_content:{})>".format(
            self.id, self.version, self.release_date, self.update_content, self.update_mode,
            self.update_url, self.is_problem, self.defects_content
        )

    def __str__(self):
        return self._desc()

    def __repr__(self):
        return self._desc()


class VersionPageList:

    def __init__(self, current_page: int, page_size: int, page_total: int, total: int, list: list):
        self.current_page = current_page
        self.page_size = page_size
        self.page_total = page_total
        self.total = total
        self.list = list

    @classmethod
    def from_pb(cls, get_version_page_list_response: GetVersionPageListResponse):
        return cls(
            get_version_page_list_response.current_page,
            get_version_page_list_response.page_size,
            get_version_page_list_response.page_total,
            get_version_page_list_response.total,
            [Version.from_pb(t) for t in get_version_page_list_response.list]
        )

    def _desc(self):
        return "<VersionPageList(current_page:{} page_size:{} page_total:{} total:{} list:{})>".format(
            self.current_page, self.page_size, self.page_total, self.total, self.list
        )

    def __str__(self):
        return self._desc()

    def __repr__(self):
        return self._desc()


class LowestVersion:

    def __init__(self, advise: Version, force: Version):
        self.advise = advise
        self.force = force

    @classmethod
    def from_pb(cls, get_lowest_version_response: GetLowestVersionResponse):
        the_advise = Version.from_pb(get_lowest_version_response.advise) \
            if get_lowest_version_response.advise.id != 0 else None

        the_force = Version.from_pb(get_lowest_version_response.force) \
            if get_lowest_version_response.force.id != 0 else None

        return cls(
            advise=the_advise,
            force=the_force
        )

    def _desc(self):
        return "<LowestVersion(advise:{} force:{})>".format(
            self.advise,
            self.force
        )

    def __str__(self):
        return self._desc()

    def __repr__(self):
        return self._desc()
