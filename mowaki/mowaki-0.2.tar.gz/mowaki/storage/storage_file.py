import mimetypes
import os
from typing import Any, Dict, NamedTuple, Type  # noqa
from urllib.parse import quote, urlparse

from .base import BaseStorage
from .types import FileInfo, FileMetadata


class FileSystemStorage(BaseStorage):
    """Filesystem-based local storage

    Warning:
        This is meant to be used for development, not production use!
    """

    def __init__(self, root_path: str) -> None:
        self.root_path = root_path

    @classmethod
    def from_url(cls, url):  # type: (str) -> BaseStorage
        parsed = urlparse(url)
        if parsed.netloc:
            raise ValueError(
                'File path cannot contain a netloc. '
                'Make sure the URL contains three forward slashes, eg. '
                'file:///path/to/storage')
        return cls(parsed.path)

    def get_file(self, key: str) -> FileInfo:
        return FileInfo(metadata=self.get_file_meta(key),
                        content=self.get_file_content(key))

    def get_file_meta(self, key: str) -> FileMetadata:
        path = self._get_file_path(key)
        if not os.path.exists(path):
            return None
        content_type, content_encoding = mimetypes.guess_type(path)
        return FileMetadata(
            content_type=content_type)

    def get_file_content(self, key: str) -> bytes:
        path = self._get_file_path(key)
        with open(path, 'rb') as fp:
            return fp.read()

    def put_file(self, key: str, data: bytes, mime_type: str = None) -> None:
        path = self._get_file_path(key)
        with open(path, 'wb') as fp:
            fp.write(data)

    def _get_file_path(self, key: str) -> str:
        key = quote(key, safe='')
        return os.path.join(self.root_path, key)

    def get_file_url(self, key: str) -> str:
        full_path = self._get_file_path(key)
        return 'file://{}'.format(full_path)

    def file_exists(self, key: str) -> bool:
        return os.path.exists(self._get_file_path(key))

    def get_etag(self, key: str) -> str:
        return None
