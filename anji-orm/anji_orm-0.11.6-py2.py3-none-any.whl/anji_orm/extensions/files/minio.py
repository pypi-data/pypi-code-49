import io
import datetime
import platform
import urllib.parse
import typing

import frozendict
import minio
import minio.credentials
import minio.error
import minio.helpers
import minio.parsers
import minio.signer
import minio.fold_case_dict

from ..exceptions import RecordBindException
from .base import AbstractFileExtension, FileRecord

__author__ = "Bogdan Gladyshev"
__copyright__ = "Copyright 2017, Bogdan Gladyshev"
__credits__ = ["Bogdan Gladyshev"]
__license__ = "MIT"
__version__ = "0.11.6"
__maintainer__ = "Bogdan Gladyshev"
__email__ = "siredvin.dark@gmail.com"
__status__ = "Production"
__all__ = ['MinioFileExtension']

DEFAULT_REGION = 'us-east-1'

_COMMENTS = '({0}; {1})'
DEFAULT_USER_AGENT = 'Minio {0}'.format(
    _COMMENTS.format(
        platform.system(),
        platform.machine()
    )
)


class WrappedResponse:

    __slots__ = ('response', )

    def __init__(self, response) -> None:
        self.response = response

    @property
    def data(self):
        return self.response._body

    @property
    def headers(self):
        return self.response.headers

    @property
    def status(self):
        return self.response.status

    @property
    def reason(self):
        return '???'


class AsyncMinio:

    __slots__ = (
        'client',
        'credentials',
        'url', 'region_name',
        'secure_protocol'
    )

    def __init__(self, access_key: str, secret_key: str, secure_protocol: bool, address: str) -> None:
        import aiohttp

        self.client = aiohttp.ClientSession()
        self.secure_protocol = secure_protocol
        if secure_protocol:
            self.url = f'https://{address}'
        else:
            self.url = f'http://{address}'
        self.credentials = minio.credentials.Credentials(
            provider=minio.credentials.Chain(
                providers=[
                    minio.credentials.Static(access_key, secret_key, None),
                    minio.credentials.EnvAWS(),
                    minio.credentials.EnvMinio(),
                    minio.credentials.IamEc2MetaData(),
                ]
            )
        )

    async def close(self):
        await self.client.close()

    async def request(
            self, method, bucket_name=None, object_name=None,
            query=None, data=None, headers=frozendict.frozendict({}),
            content_sha256=None):
        """
        Open a url wrapper around signature version '4'
           and :meth:`urllib3.PoolManager.urlopen`
        """
        # HTTP headers are case insensitive filter out
        # all duplicate headers and pick one.
        fold_case_headers = minio.fold_case_dict.FoldCaseDict()

        # Set user agent once before executing the request.
        fold_case_headers['User-Agent'] = DEFAULT_USER_AGENT
        for header in headers:
            fold_case_headers[header] = headers[header]

        # Get bucket region.
        region = DEFAULT_REGION

        url = minio.helpers.get_target_url(
            self.url, bucket_name=bucket_name,
            object_name=object_name, bucket_region=region,
            query=query
        )

        # Get signature headers if any.
        headers = minio.signer.sign_v4(
            method, url, region,
            fold_case_headers,
            self.credentials,
            content_sha256, datetime.datetime.utcnow()
        )

        response = await self.client._request(
            method,
            url,
            data=data,
            headers=headers
        )
        await response.read()

        if response.status != 200 and response.status != 204 \
           and response.status != 206:

            supported_methods = [
                'HEAD',
                'GET',
                'POST',
                'PUT',
                'DELETE'
            ]

            if method in supported_methods:
                raise minio.error.ResponseError(
                    WrappedResponse(response), method, bucket_name, object_name
                ).get_exception()
            raise ValueError(
                'Unsupported method returned error: {0}'.format(response.status)
            )

        return response

    async def bucket_exists(self, bucket_name: str) -> bool:
        minio.helpers.is_valid_bucket_name(bucket_name, False)

        try:
            await self.request('HEAD', bucket_name=bucket_name)
        # If the bucket has not been created yet, Minio will return a "NoSuchBucket" error.
        except minio.error.NoSuchBucket:
            return False
        return True

    async def make_bucket(self, bucket_name: str) -> None:
        minio.helpers.is_valid_bucket_name(bucket_name, True)

        await self.request(
            'PUT', bucket_name=bucket_name
        )

    async def put_object(
            self, bucket_name, object_name, data, length,
            content_type='application/octet-stream',
            metadata=None, sse=None,
            part_size=minio.helpers.DEFAULT_PART_SIZE):

        minio.helpers.is_valid_sse_object(sse)
        minio.helpers.is_valid_bucket_name(bucket_name, False)
        minio.helpers.is_non_empty_string(object_name)

        if not callable(getattr(data, 'read')):
            raise ValueError(
                'Invalid input data does not implement a callable read() method')

        if length > (part_size * minio.helpers.MAX_MULTIPART_COUNT):
            raise minio.error.InvalidArgumentError(
                'Part size * max_parts(10000) is '
                ' lesser than input length.'
            )

        if part_size < minio.helpers.MIN_PART_SIZE:
            raise minio.error.InvalidArgumentError(
                'Input part size is smaller '
                ' than allowed minimum of 5MiB.'
            )

        if part_size > minio.helpers.MAX_PART_SIZE:
            raise minio.error.InvalidArgumentError(
                'Input part size is bigger '
                ' than allowed maximum of 5GiB.'
            )

        if not metadata:
            metadata = {}

        metadata = minio.helpers.amzprefix_user_metadata(metadata)

        metadata['Content-Type'] = 'application/octet-stream' if \
            not content_type else content_type

        current_data = data.read(length)
        if len(current_data) != length:
            raise minio.error.InvalidArgumentError(
                'Could not read {} bytes from data to upload'.format(length)
            )

        return await self._do_put_object(
            bucket_name, object_name,
            current_data, len(current_data),
            metadata=metadata, sse=sse,
        )

    async def _do_put_object(
            self, bucket_name, object_name, part_data,
            part_size, upload_id='', part_number=0,
            metadata=None, sse=None):
        minio.helpers.is_valid_bucket_name(bucket_name, False)
        minio.helpers.is_non_empty_string(object_name)

        # Accept only bytes - otherwise we need to know how to encode
        # the data to bytes before storing in the object.
        if not isinstance(part_data, bytes):
            raise ValueError('Input data must be bytes type')

        headers = {
            'Content-Length': str(part_size),
        }

        md5_base64 = ''
        sha256_hex = ''
        if self.secure_protocol:
            md5_base64 = minio.helpers.get_md5_base64digest(part_data)
            sha256_hex = minio.signer._UNSIGNED_PAYLOAD
        else:
            sha256_hex = minio.helpers.get_sha256_hexdigest(part_data)

        if md5_base64:
            headers['Content-Md5'] = md5_base64

        if metadata:
            headers.update(metadata)

        query = {}
        if part_number > 0 and upload_id:
            query = {
                'uploadId': upload_id,
                'partNumber': str(part_number),
            }
            # Encryption headers for multipart uploads should
            # be set only in the case of SSE-C.
            if sse and sse.type() == "SSE-C":
                headers.update(sse.marshal())
        elif sse:
            headers.update(sse.marshal())

        response = await self.request(
            'PUT',
            bucket_name=bucket_name,
            object_name=object_name,
            query=query,
            headers=headers,
            data=io.BytesIO(part_data),
            content_sha256=sha256_hex
        )

        return response

    async def get_object(self, bucket_name, object_name, request_headers=None, sse=None):
        minio.helpers.is_valid_bucket_name(bucket_name, False)
        minio.helpers.is_non_empty_string(object_name)

        return await self._get_partial_object(
            bucket_name,
            object_name,
            request_headers=request_headers,
            sse=sse
        )

    async def _get_partial_object(
            self, bucket_name, object_name,
            offset=0, length=0, request_headers=None, sse=None):
        minio.helpers.is_valid_sse_c_object(sse=sse)
        minio.helpers.is_valid_bucket_name(bucket_name, False)
        minio.helpers.is_non_empty_string(object_name)

        headers = {}
        if request_headers:
            headers = request_headers

        if offset != 0 or length != 0:
            request_range = '{}-{}'.format(
                offset, "" if length == 0 else offset + length - 1
            )
            headers['Range'] = 'bytes=' + request_range

        if sse:
            headers.update(sse.marshal())

        return await self.request(
            'GET', bucket_name=bucket_name, object_name=object_name,
            headers=headers
        )

    async def remove_object(self, bucket_name, object_name):
        """
        Remove an object from the bucket.
        :param bucket_name: Bucket of object to remove
        :param object_name: Name of object to remove
        :return: None
        """
        minio.helpers.is_valid_bucket_name(bucket_name, False)
        minio.helpers.is_non_empty_string(object_name)

        await self.request('DELETE', bucket_name=bucket_name, object_name=object_name)


class MinioFileExtension(AbstractFileExtension):

    __slots__ = (
        'client', 'bucket_name',
        'access_key', 'secret_key',
        'address',
        'secure_protocol'
    )

    client: typing.Union[minio.Minio, AsyncMinio]

    def __init__(self, uri: str) -> None:
        super().__init__(uri)
        parsed_uri = urllib.parse.urlparse(self.uri)
        self.bucket_name = parsed_uri.path.replace('/', '')
        self.access_key = parsed_uri.username
        self.secret_key = parsed_uri.password
        self.address = f'{parsed_uri.hostname}:{parsed_uri.port}'
        self.secure_protocol = parsed_uri.scheme == 'miniossl'

    async def async_load(self):
        await super().async_load()
        self.client = AsyncMinio(self.access_key, self.secret_key, self.secure_protocol, self.address)
        if not await self.client.bucket_exists(self.bucket_name):
            await self.client.make_bucket(self.bucket_name)

    def load(self):
        super().load()
        self.client = minio.Minio(
            self.address,
            access_key=self.access_key,
            secret_key=self.secret_key,
            secure=self.secure_protocol
        )
        if not self.client.bucket_exists(self.bucket_name):
            self.client.make_bucket(self.bucket_name)

    def upload_file(self, file_record: FileRecord) -> None:
        if file_record.record is None:
            raise RecordBindException('For this operation, file_record should be bind to record')
        if file_record.content is None:
            raise ValueError("Cannot upload empty file")
        if file_record.in_bytes:
            stream = io.BytesIO(file_record.content)  # type: ignore
        else:
            stream = io.BytesIO(file_record.content.encode('utf-8'))  # type: ignore
        self.client.put_object(
            self.bucket_name, f'{file_record.record.id}-{file_record.name}',
            stream, len(file_record.content)
        )

    async def async_upload_file(self, file_record: FileRecord) -> None:
        if file_record.record is None:
            raise RecordBindException('For this operation, file_record should be bind to record')
        if file_record.content is None:
            raise ValueError("Cannot upload empty file")
        if file_record.in_bytes:
            stream = io.BytesIO(file_record.content)  # type: ignore
        else:
            stream = io.BytesIO(file_record.content.encode('utf-8'))  # type: ignore
        await self.client.put_object(
            self.bucket_name, f'{file_record.record.id}-{file_record.name}',
            stream, len(file_record.content)
        )

    def download_file(self, file_record: FileRecord) -> None:
        if file_record.record is None:
            raise RecordBindException('For this operation, file_record should be bind to record')
        file_content = self.client.get_object(
            self.bucket_name, f'{file_record.record.id}-{file_record.name}'
        ).data
        if not file_record.in_bytes and isinstance(file_content, bytes):
            file_content = file_content.decode('utf-8')
        file_record._content = file_content

    async def async_download_file(self, file_record: FileRecord) -> None:
        if file_record.record is None:
            raise RecordBindException('For this operation, file_record should be bind to record')
        file_content = (await self.client.get_object(
            self.bucket_name, f'{file_record.record.id}-{file_record.name}'
        ))._body
        if not file_record.in_bytes and isinstance(file_content, bytes):
            file_content = file_content.decode('utf-8')
        file_record._content = file_content

    async def async_delete_file(self, file_record: FileRecord) -> None:
        if file_record.record is None:
            raise RecordBindException('For this operation, file_record should be bind to record')
        await self.client.remove_object(
            self.bucket_name, f'{file_record.record.id}-{file_record.name}'
        )

    def delete_file(self, file_record: FileRecord) -> None:
        if file_record.record is None:
            raise RecordBindException('For this operation, file_record should be bind to record')
        self.client.remove_object(
            self.bucket_name, f'{file_record.record.id}-{file_record.name}'
        )

    async def async_close(self):
        await self.client.close()
