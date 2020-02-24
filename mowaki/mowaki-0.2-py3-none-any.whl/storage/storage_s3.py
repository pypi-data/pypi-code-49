import logging
import posixpath
from urllib.parse import urlparse

import boto3
from botocore.client import Config

from .base import BaseStorage
from .types import FileInfo, FileMetadata, PresignedPostInfo, S3Object

logger = logging.getLogger(__name__)


_config = None


def get_aws_session() -> boto3.Session:
    return boto3.Session()


def get_s3_public_file_url(region: str, bucket_name: str, path: str) -> str:
    return 'https://{name}.s3-{region}.amazonaws.com/{path}'.format(
        region=region, name=bucket_name, path=path)


class S3Storage(BaseStorage):
    """Amazon S3 backed storage

    This is the recommended choice for production.
    """

    def __init__(self, bucket_name: str, key_prefix: str = None) -> None:
        self.bucket_name = bucket_name
        self.key_prefix = key_prefix or ''

    @classmethod
    def from_url(cls, url):  # type: (str) -> BaseStorage
        parsed = urlparse(url)
        if not parsed.netloc:
            raise ValueError(
                'S3 bucket name missing. '
                'Make sure the URL is in the form s3://bucket-name/key-prefix')
        return cls(parsed.netloc, key_prefix=parsed.path.lstrip('/'))

    def get_file(self, key: str) -> FileInfo:
        full_key = self._get_full_key(key)
        data = self._get_bucket().Object(full_key).get()
        return FileInfo(
            metadata=FileMetadata(
                content_type=data['ContentType']),
            content=data['Body'])

    def get_file_meta(self, key: str) -> FileMetadata:
        return self.get_file(key).metadata

    def get_file_content(self, key: str) -> bytes:
        return self.get_file(key).content

    def get_presigned_post(self, key: str, content_type: str) \
            -> PresignedPostInfo:
        full_key = self._get_full_key(key)

        # s3 = get_aws_session().resource('s3')
        aws = get_aws_session()
        s3 = aws.client('s3', config=Config(signature_version='s3v4'))

        presigned_post = s3.generate_presigned_post(
            Bucket=self.bucket_name,
            Key=full_key,
            Fields={"Content-Type": content_type},
            Conditions=[
                # TODO: limit file size herx
                {"Content-Type": content_type}
            ],
            ExpiresIn=3600)
        return PresignedPostInfo(
            url=presigned_post['url'],
            fields=presigned_post['fields'])

    def _get_bucket(self):
        aws = get_aws_session()
        s3 = aws.resource('s3')
        return s3.Bucket(self.bucket_name)

    def _get_full_key(self, key: str) -> str:
        return posixpath.join(self.key_prefix, key)

    def _get_object(self, key: str) -> S3Object:
        full_key = self._get_full_key(key)
        return self._get_bucket().Object(full_key)

    def put_file(self, key: str, data: bytes, mime_type: str = None) -> None:
        self._get_object(key).put(Body=data, ContentType=mime_type)

    def get_file_url(self, key: str) -> str:
        full_key = self._get_full_key(key)
        return ('s3://{bucket}/{key}'
                .format(bucket=self.bucket_name, key=full_key))

    def file_exists(self, key: str) -> bool:
        from botocore.exceptions import ClientError

        aws = get_aws_session()
        s3_client = aws.client('s3')
        try:
            s3_client.head_object(
                Bucket=self.bucket_name,
                Key=self._get_full_key(key))
        except ClientError as e:
            if e.response['Error']['Code'] == "404":
                return False
            raise
        return True

    def get_etag(self, key: str) -> str:
        return self._get_object(key).e_tag
