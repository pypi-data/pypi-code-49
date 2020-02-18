import logging
import os
import re
from abc import abstractmethod
from glob import glob
from typing import Any, Dict, Generator, Optional, Tuple, Type
from zipfile import is_zipfile

import click
import requests
from elftools.elf.elffile import ELFFile
from requests import Response

from .authenticator import Authenticator
from .context import MemfaultCliClickContext, PackageInfo
from .gnu_build_id import get_gnu_build_id

LOG = logging.getLogger(__name__)

GNU_BUILD_ID_RE = re.compile(r"Build ID: (?P<gnu_build_id>[a-f\d]+)")


def check_response(response: Response):
    if response.status_code >= 400:
        raise Exception(
            f"Request failed with HTTP status {response.status_code}\nResponse body:\n{response.content.decode()}"
        )


class Uploader:
    def __init__(
        self, *, ctx: MemfaultCliClickContext, file_path: str, authenticator: Authenticator
    ):
        self.ctx: MemfaultCliClickContext = ctx
        self.file_path = file_path
        self.authenticator: Authenticator = authenticator

    @staticmethod
    @abstractmethod
    def project_key_auth() -> bool:
        pass

    @property
    def base_url(self):
        return self.ctx.file_url

    def _api_base_url(self) -> str:
        return f"{self.base_url}/api/v0"

    def _projects_base_url(self) -> str:
        return f"{self.base_url}/api/v0/organizations/{self.ctx.org}/projects/{self.ctx.project}"

    def upload_url(self) -> str:
        """
        The upload URL for a 'prepared upload' for the configured authentication method.
        """
        if self.authenticator.project_key_auth():
            return f"{self._api_base_url()}/upload"
        else:
            return f"{self._projects_base_url()}/upload"

    @abstractmethod
    def can_upload_file(self) -> bool:
        """Test the file pointed to by `file_path`."""
        pass

    @abstractmethod
    def entity_url(self) -> str:
        """The final URL to POST to during the prepared upload sequence."""
        pass

    @abstractmethod
    def requests_auth_params(self) -> dict:
        """A dict of `requests` parameters that should be used for authentication."""
        pass

    def _is_already_uploaded(self) -> bool:
        return False

    def _prepare_upload(self) -> Tuple[str, str]:
        response = requests.post(self.upload_url(), **self.authenticator.requests_auth_params())
        check_response(response)
        data = response.json()["data"]
        return data["upload_url"], data["token"]

    def _put_file(self, upload_url: str) -> None:
        with open(self.file_path, "rb") as file:
            check_response(requests.put(upload_url, data=file))

    def post_token_extra_request_data(self) -> Optional[Dict]:
        return None

    def _post_token(self, token: str) -> None:
        json_d = {"file": {"token": token}}
        extra_request_data = self.post_token_extra_request_data()
        if extra_request_data:
            json_d.update(extra_request_data)
        check_response(
            requests.post(
                self.entity_url(), json=json_d, **self.authenticator.requests_auth_params()
            )
        )

    def _is_elf(self) -> bool:
        with open(self.file_path, "rb") as file:
            if file.read(4) != b"\x7FELF":
                return False

        return True

    def _get_gnu_build_id_and_has_debug_info(self) -> Tuple[Optional[str], bool]:
        with open(self.file_path, "rb") as f:
            elf = ELFFile(f)
            return get_gnu_build_id(elf), elf.has_dwarf_info()

    def upload(self) -> None:
        if self._is_already_uploaded():
            LOG.info(f"{self.file_path}: skipping, already uploaded.")
            return
        upload_url, token = self._prepare_upload()
        self._put_file(upload_url)
        self._post_token(token)
        LOG.info(f"{self.file_path}: uploaded!")


class BugreportUploader(Uploader):
    def can_upload_file(self) -> bool:
        if not is_zipfile(self.file_path):
            LOG.error(f"{self.file_path} is not a valid zip file!")
            return False
        return True

    def entity_url(self) -> str:
        if self.authenticator.project_key_auth():
            return f"{self._api_base_url()}/upload/bugreport"
        else:
            return f"{self._projects_base_url()}/bugreports"


class CoredumpUploader(Uploader):
    def can_upload_file(self) -> bool:
        with open(self.file_path, "rb") as f:
            hdr = f.read(4).decode("ascii", errors="ignore")
            if hdr != "CORE":
                LOG.error(f"{self.file_path} is not a Memfault Coredump")
                return False

        return True

    def entity_url(self) -> str:
        if self.authenticator.project_key_auth():
            return f"{self._api_base_url()}/upload/coredump"
        else:
            return f"{self._projects_base_url()}/coredumps"


class SymbolUploader(Uploader):
    gnu_build_id: str = ""

    def can_upload_file(self) -> Optional[Any]:
        if not self._is_elf():
            LOG.info(f"{self.file_path}: Not an ELF file")
            return False

        self.gnu_build_id, has_debug_info = self._get_gnu_build_id_and_has_debug_info()
        if not self.gnu_build_id:
            LOG.info(f"{self.file_path}: looks like an ELF but does not contain a GNU Build ID")
            return False
        if not has_debug_info:
            LOG.info(f"{self.file_path}: looks like an ELF but it has no .debug_info")
            return False
        LOG.info(
            f"{self.file_path}: ELF file with .debug_info and GNU Build ID: {self.gnu_build_id}"
        )
        return True

    def _is_already_uploaded(self) -> bool:
        response = requests.head(
            f"{self._projects_base_url()}/symbols-by-gnu-build-id/{self.gnu_build_id}",
            auth=self.ctx.account,
        )
        try:
            check_response(response)
        except:
            if response.status_code == 404:
                return False
            raise
        return True

    def entity_url(self) -> str:
        return f"{self._projects_base_url()}/symbols"


class SoftwareArtifactUploader(Uploader):
    def can_upload_file(self) -> Optional[Any]:
        if not self._is_elf():
            LOG.info(f"{self.file_path}: Not an ELF file")
            return False

        self.gnu_build_id, has_debug_info = self._get_gnu_build_id_and_has_debug_info()
        if not self.gnu_build_id:
            # We can handle a symbol artifact without a Build ID but might as well
            # recommend it!
            LOG.info(
                f"{self.file_path}: Consider adding a GNU Build ID to uniquely identify the build"
            )

        if not has_debug_info:
            LOG.info(f"{self.file_path}: looks like an ELF but it has no .debug_info")
            return False
        LOG.info(f"{self.file_path}: ELF file with .debug_info")
        return True

    def _is_already_uploaded(self) -> bool:
        return False

    def entity_url(self) -> str:
        return f"{self._projects_base_url()}/symbols"

    def post_token_extra_request_data(self) -> Optional[Dict]:
        software_type, software_version = self.ctx.software_info
        return {
            "software_version": {"version": software_version, "software_type": software_type,},
        }

    @staticmethod
    def project_key_auth() -> bool:
        return False


class ReleaseArtifactUploader(Uploader):
    def can_upload_file(self) -> Optional[Any]:
        # There are no restrictions for the type of binary a customer uses for
        # a release
        return True

    def _is_already_uploaded(self) -> bool:
        return False

    def entity_url(self) -> str:
        return f"{self._projects_base_url()}/releases/ota_payload"

    def post_token_extra_request_data(self) -> Optional[Dict]:
        software_type, software_version = self.ctx.software_info
        return {
            "software_version": {"version": software_version, "software_type": software_type,},
            "hardware_version": self.ctx.hardware_version,
        }


class DirectoryUploader(Uploader):
    uploader_cls: Type[Uploader] = None

    def can_upload_file(self) -> bool:
        return os.path.isdir(self.file_path)

    def _walk_files(self, root: str) -> Generator[str, Any, Any]:
        for root, dirs, files in os.walk(root):
            yield from map(lambda file: os.path.join(root, file), files)

    def upload(self) -> bool:
        did_upload = False
        for file_path in self._walk_files(self.file_path):
            uploader = self.uploader_cls(
                ctx=self.ctx, file_path=file_path, authenticator=self.authenticator
            )
            if uploader.can_upload_file():
                uploader.upload()
                did_upload |= True
            else:
                LOG.info(f"{file_path}: skipping...")
        return did_upload


class SymbolDirectoryUploader(DirectoryUploader):
    uploader_cls = SymbolUploader


class ProguardMappingUploader(Uploader):
    def __init__(
        self,
        *,
        ctx: MemfaultCliClickContext,
        file_path: str,
        authenticator: Authenticator,
        package_info: PackageInfo,
    ):
        super().__init__(ctx=ctx, file_path=file_path, authenticator=authenticator)
        self.package_info = package_info

    def can_upload_file(self) -> Optional[Any]:
        return True

    def entity_url(self) -> str:
        return f"{self._projects_base_url()}/symbols"

    def post_token_extra_request_data(self) -> Optional[Dict]:
        return {
            "software_version": {
                "version": f"{self.package_info.version_name}:{self.package_info.version_code}",
                "software_type": self.package_info.name,
            },
        }


class AndroidAppSymbolsUploader(Uploader):
    def can_upload_file(self) -> bool:
        if not os.path.isdir(self.file_path):
            LOG.error(
                f'{self.file_path} is not a directory. Please specify the Android app\'s root "build" path instead!'
            )
            return False
        return True

    def _find_apk_path(self) -> str:
        apk_dir = os.path.join(self.file_path, "outputs", "apk", self.ctx.build_variant)
        if not os.path.isdir(apk_dir):
            raise click.exceptions.FileError(
                apk_dir, hint=f'Please pass the Android app\'s root "build" path!'
            )
        apk_glob = os.path.join(apk_dir, "*.apk")
        apks = glob(apk_glob)
        if not apks:
            raise click.exceptions.FileError(apk_glob, hint=f"No .apk found!")
        if len(apks) > 1:
            raise click.exceptions.FileError(apk_glob, hint=f"Multiple .apks found!")
        return apks[0]

    def _get_package_info_from_apk(self) -> PackageInfo:
        from pyaxmlparser import APK

        apk = APK(self._find_apk_path())
        return PackageInfo(apk.get_package(), apk.version_name, apk.version_code)

    def _find_mapping_txt(self) -> Optional[str]:
        if self.ctx.android_mapping_txt:
            return self.ctx.android_mapping_txt
        # In older version, the default folder was called "proguard", later it got renamed to "mapping":
        subdirs = ("mapping", "proguard")
        paths_to_check = tuple(
            map(
                lambda subdir: os.path.join(
                    self.file_path, "outputs", "mapping", self.ctx.build_variant, "mapping.txt"
                ),
                subdirs,
            )
        )
        for path in paths_to_check:
            if os.path.isfile(path):
                return path
        LOG.info("No mapping.txt found in default locations, assuming ProGuard/R8 is disabled...")
        return None

    def _upload_mapping_txt(self) -> bool:
        mapping_txt_path = self._find_mapping_txt()
        if not mapping_txt_path:
            return False
        package_info = self.ctx.android_package_info
        if not package_info:
            package_info = self._get_package_info_from_apk()
        pg_uploader = ProguardMappingUploader(
            ctx=self.ctx,
            file_path=mapping_txt_path,
            package_info=package_info,
            authenticator=self.authenticator,
        )
        pg_uploader.upload()
        return True

    def _upload_ndk_symbols(self) -> bool:
        # TODO: add support for legacy ndkBuild?
        cmake_path_out = os.path.join(
            self.file_path, "intermediates", "cmake", self.ctx.build_variant
        )
        if not os.path.isdir(cmake_path_out):
            return False
        sym_dir_uploader = SymbolDirectoryUploader(
            ctx=self.ctx, file_path=cmake_path_out, authenticator=self.authenticator
        )
        return sym_dir_uploader.upload()

    def upload(self) -> None:
        did_upload = self._upload_mapping_txt() or self._upload_ndk_symbols()
        if not did_upload:
            raise click.exceptions.UsageError("No files uploaded!")
