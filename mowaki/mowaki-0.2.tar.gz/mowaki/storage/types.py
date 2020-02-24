from typing import Any, Dict, NamedTuple

# FIXME: what's the actual type? seems to be generated.. :(
S3Object = Any

FileMetadata = NamedTuple('FileMetadata', [
    ('content_type', str),
    # TODO: add others as needed
])
FileMetadata.__doc__ = \
    "Container for information about a file in the storage"
FileMetadata.content_type.__doc__ = \
    "File content type (mime type)"

FileInfo = NamedTuple('FileInfo', [
    ('metadata', FileMetadata),
    ('content', bytes),
])
FileInfo.__doc__ = \
    "Container for file metadata + content from the storage"

PresignedPostInfo = NamedTuple('PresignedPostInfo', [
    ('url', str),
    ('fields', Dict[str, str]),
])
PresignedPostInfo.__doc__ = \
    "Container for pre-signed post information"
PresignedPostInfo.url.__doc__ = \
    "The URL at which the POST request should be directed"
PresignedPostInfo.fields.__doc__ = \
    "Form data to be included in the POST request"
