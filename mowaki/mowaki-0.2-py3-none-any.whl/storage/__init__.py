"""File storage abstraction

The main interface is specified by :py:class:`BaseStorage`.

Use :py:func:`get_storage_from_url` to get an appropriate storage instance.

**Supported storage types**:

+----------+-------------------------------+---------------------------------+
| Scheme   | Class                         | Example URL                     |
+==========+===============================+=================================+
| ``s3``   | :py:class:`S3Storage`         | ``s3://bucket-name/key-prefix`` |
+----------+-------------------------------+---------------------------------+
| ``file`` | :py:class:`FileSystemStorage` | ``file:///path/to/files``       |
+----------+-------------------------------+---------------------------------+
|``memory``| :py:class:`MemoryStorage`     | ``memory://bucket/prefix``      |
+----------+-------------------------------+---------------------------------+

"""

from urllib.parse import urlparse
from typing import Dict, Type  # noqa

from .base import BaseStorage
from .storage_file import FileSystemStorage
from .storage_s3 import S3Storage
from .storage_memory import MemoryStorage
from .types import FileInfo, FileMetadata, PresignedPostInfo  # noqa


STORAGE_BACKENDS = {
    'file': FileSystemStorage,
    's3': S3Storage,
    'memory': MemoryStorage,
}  # type: Dict[str, Type[BaseStorage]]


def get_storage_from_url(url: str) -> BaseStorage:
    """Get a storage class instance from URL

    Args:
        url: Base URL for the storage location

    Returns:
        BaseStorage:
            An appropriate subclass of :py:class:`BaseStorage`,
            depending on the scheme of the specified URL.
    """

    parsed = urlparse(url)

    try:
        backend = STORAGE_BACKENDS[parsed.scheme]
    except KeyError:
        raise ValueError('Unsupported storage type: {}'.format(parsed.scheme))

    return backend.from_url(url)
