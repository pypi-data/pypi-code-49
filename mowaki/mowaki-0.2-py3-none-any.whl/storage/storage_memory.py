import hashlib
import logging
import posixpath
from typing import Dict
from urllib.parse import urlparse

from werkzeug.local import Local

from .base import BaseStorage
from .types import FileInfo, FileMetadata, PresignedPostInfo

logger = logging.getLogger(__name__)


_storage = Local()


BucketType = Dict[str, FileInfo]
StorageType = Dict[str, BucketType]


def get_local_storage() -> StorageType:
    try:
        return _storage.storage
    except AttributeError:
        _storage.storage = {}  # type: ignore
        return _storage.storage


def get_local_bucket(name: str) -> BucketType:
    storage = get_local_storage()
    storage.setdefault(name, {})
    return storage[name]


def get_stored_file(bucket: str, key: str) -> FileInfo:
    _bucket = get_local_bucket(bucket)
    try:
        return _bucket[key]
    except KeyError:
        return None


def clear_local_storage() -> None:
    try:
        del _storage.storage
    except AttributeError:
        pass


class MemoryStorage(BaseStorage):

    def __init__(self, bucket_name: str, key_prefix: str = None) -> None:
        self.bucket_name = bucket_name
        self.key_prefix = key_prefix or ''

    @classmethod
    def from_url(cls, url):  # type: (str) -> BaseStorage
        parsed = urlparse(url)
        if not parsed.netloc:
            raise ValueError(
                'Bucket name missing. '
                'Make sure the URL is in the form memory://bucket/prefix')
        return cls(parsed.netloc, key_prefix=parsed.path.lstrip('/'))

    def get_file(self, key: str) -> FileInfo:
        bucket = self._get_bucket()
        full_key = self._get_full_key(key)
        return bucket.get(full_key)

    def get_file_meta(self, key: str) -> FileMetadata:
        return self.get_file(key).metadata

    def get_file_content(self, key: str) -> bytes:
        return self.get_file(key).content

    def get_presigned_post(self, key: str, content_type: str) \
            -> PresignedPostInfo:
        raise NotImplementedError

    def _get_bucket(self):
        return get_local_bucket(self.bucket_name)

    def _get_full_key(self, key: str) -> str:
        return posixpath.join(self.key_prefix, key)

    def put_file(self, key: str, data: bytes, mime_type: str = None) -> None:
        bucket = self._get_bucket()
        full_key = self._get_full_key(key)
        bucket[full_key] = FileInfo(
            metadata=FileMetadata(content_type=mime_type),
            content=data)

    def get_file_url(self, key: str) -> str:
        full_key = self._get_full_key(key)
        return ('memory://{bucket}/{key}'
                .format(bucket=self.bucket_name, key=full_key))

    def file_exists(self, key: str) -> bool:
        bucket = self._get_bucket()
        full_key = self._get_full_key(key)
        return full_key in bucket

    def get_etag(self, key: str) -> str:
        if not self.file_exists(key):
            return None
        data = self.get_file_content(key)
        return hashlib.sha1(data).hexdigest()
