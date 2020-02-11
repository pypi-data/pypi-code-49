"""
API (ObjectClerk) definition
"""

from hashlib import md5
from io import BufferedReader, BytesIO
import logging
from pathlib import Path
from sys import getsizeof
from typing import Union, Tuple

from boto3 import client as Boto3Client
from botocore.config import Config as BotoConfig
from botocore.exceptions import ConnectionError, HTTPClientError
from retry import retry
from retry.api import retry_call

from object_clerk.exceptions import (
    ObjectClerkException,
    ObjectSaveException,
    ObjectVerificationException,
)
from object_clerk.utils import mutate_client_exceptions

logger = logging.getLogger(__name__)

# Configure boto to not retry; handled by the retry api
BOTO_CONFIG = BotoConfig(connect_timeout=60, read_timeout=60, retries={"max_attempts": 0})
# Exceptions to retry according to the instance definition
CONNECTION_RETRY_EXCEPTIONS = (ConnectionError, HTTPClientError)
# Set threshold at which the md5 checksum isn't valid to compare to the etag due to multipart uploads
MULTIPART_THRESHOLD = 1024 * 1024 * 1024 * 5  # 5 GB
# Retry config for checksum failures
CHECKSUM_RETRY_CONFIG = {"tries": 3, "delay": 1}

__all__ = ["ObjectClerk"]


class ObjectClerk:
    """
    A wrapper for the following boto3 s3 client operations below the multipart upload threshold of 5 GB:
    boto3.client.func : object_clerk.func
    - get_object : get_object
    - head_object : get_object_info
    - upload_fileobj : upload_object
    - copy_object : copy_object
    - delete_object : delete_object
    """
    def __init__(
        self,
        host: str,
        port: int,
        access_key: str,
        secret_key: str,
        retry_delay: int,
        retry_backoff: int,
        retry_jitter: Union[int, Tuple[int, int]],
        retry_max_delay: int,
        retry_tries: int = -1,
        use_ssl: bool = False,
    ):
        """
        Intialize the Object clerk with the location of the s3 gateway
        and configuration for retrying connection issues
        :param host: Host name or ip for an s3 Gateway
        :param port: Post the s3 gateway listens on
        :param access_key: Access Key for the gateway
        :param secret_key: Secret Key for the gateway
        :param retry_delay: initial delay between attempts for connection errors.
        :param retry_backoff: multiplier applied to delay between attempts to connect.
        :param retry_jitter: extra seconds added to delay between attempts to connect.
                   fixed if a number, random if a range tuple (min, max)
        :param retry_max_delay: the maximum value of delay between connection attempts.
        :param retry_tries: Number of time to retry connecting ot hte gateway. -1 for indefinite retries
        :param use_ssl: True for https and False for http
        """
        self.access_key = access_key
        self.secret_key = secret_key
        self.host = host
        self.port = port
        self.retry_delay = retry_delay
        self.retry_backoff = retry_backoff
        self.retry_jitter = retry_jitter
        self.retry_max_delay = retry_max_delay
        self.retry_tries = retry_tries
        self.use_ssl = use_ssl
        self.retry_config = {
            "tries": self.retry_tries,
            "delay": self.retry_delay,
            "max_delay": self.retry_max_delay,
            "backoff": self.retry_backoff,
            "jitter": self.retry_jitter,
            "exceptions": CONNECTION_RETRY_EXCEPTIONS,
        }
        protocol = "https" if self.use_ssl else "http"
        self.endpoint_url = f"{protocol}://{self.host}:{self.port}"
        self.client = Boto3Client(
            service_name="s3",
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            endpoint_url=self.endpoint_url,
        )
        logger.info(str(self))

    def __repr__(self):
        return f"ObjectClerk(host={self.host}, port={self.port}, access_key={self.access_key}, " \
               f"secret_key=<SECRET KEY>, retry_delay={self.retry_delay}, retry_backoff={self.retry_backoff}, " \
               f"retry_jitter={self.retry_jitter}, retry_max_delay={self.retry_max_delay}, " \
               f"retry_tries={self.retry_tries}, use_ssl={self.use_ssl})"

    def __str__(self):
        return f"ObjectClerk connected to {self.endpoint_url} retrying connection errors with {self.retry_config}"

    @staticmethod
    def _get_object_checksum(object_stream: bytes) -> str:
        """
        Get the md5 checksum of a bytestream
        :param object_stream: bytes to create a checksum for
        :return: str md5 checksum
        :raises: ObjectClerkException if the bytes stream is too large so as to be invalid
        for comparison to the s3 etag
        """
        # Verify that the size doesn't exceed the limit at which the etag is != md5 checksum
        size = getsizeof(object_stream)
        if size > MULTIPART_THRESHOLD:
            logger.warning(f"Cannot verify the check sum of a file > {MULTIPART_THRESHOLD} bytes")
            raise ObjectClerkException(
                f"Cannot verify the check sum of a file > {MULTIPART_THRESHOLD} bytes"
            )
        return md5(object_stream).hexdigest()

    @staticmethod
    def _verify_checksum(object_checksum: str, etag: str) -> None:
        """
        Verify the checksum matches the etag response from an s3 gateway
        :param object_checksum: checksum of the bytes object
        :param etag: checksum from the s3 api
        :return: None
        :raises: ObjectVerificationException if the the checksums don't match
        """
        # Strip leading and trailing quotes on the etag if they exist
        etag = etag.replace('"', '')
        if object_checksum == etag:
            return

        logger.warning(
            f"Object checksum verification failed: check_sum={object_checksum}, etag={etag}"
        )
        raise ObjectVerificationException(
            f"Object checksum verification failed: check_sum={object_checksum}, etag={etag}"
        )

    @mutate_client_exceptions
    def _get_object(self, bucket: str, object_key: str) -> bytes:
        """
        Executes the boto3.client.get_object function with ClientError exceptions
        transformed to more precise ObjectClerk exceptions
        :param bucket: Bucket to retrieve the object from
        :param object_key: Key of the object in the bucket
        :return: bytes of the object retrieved
        """
        logger.debug(f"Attempting object retrieval: bucket={bucket}, object_key={object_key}")
        return self.client.get_object(Bucket=bucket, Key=object_key)

    @retry(ObjectVerificationException, **CHECKSUM_RETRY_CONFIG)
    def get_object(
        self, bucket: str, object_key: str, verify_checksum: bool = True
    ) -> bytes:
        """
        Retrieves a bytes object from an S3 endpoint retrying connection errors
        according to object clerk instance attributes
        errors according to object_clerk definition
        :param bucket: Bucket to retrieve the objext from
        :param object_key: Key of the object in the bucket
        :param verify_checksum: boolean to determine whether or not to verify the checksum of the retrieved bytes
        against the etag
        :return: bytes of the object retrieved
        :raises: ObjectNotFoundException, ObjectClerkException, ObjectVerificationException
        """
        response = retry_call(
            self._get_object,
            fkwargs={"bucket": bucket, "object_key": object_key},
            **self.retry_config,
        )
        object_stream = response.get("Body").read()
        etag = response.get("ETag")
        if verify_checksum:
            checksum = self._get_object_checksum(object_stream)
            self._verify_checksum(checksum, etag)
        return object_stream

    @mutate_client_exceptions
    def _get_object_info(self, bucket: str, object_key: str) -> dict:
        """
        Executes the boto3.client.head_object function with ClientError exceptions
        transformed to more precise ObjectClerk exceptions
        :param bucket: Bucket to retrieve headers for the object from
        :param object_key: Key of the object in the bucket
        :return: dict of the object s3 headers
        """
        logger.debug(f"Attempting object info retrieval: bucket={bucket}, object_key={object_key}")
        return self.client.head_object(Bucket=bucket, Key=object_key)

    def get_object_info(self, bucket: str, object_key: str) -> dict:
        """
        Retrieves a headers for an object from an S3 endpoint retrying connection errors
        according to object clerk instance attributes
        :param bucket: Bucket to retrieve headers for the object from
        :param object_key: Key of the object in the bucket
        :return: dict of the object s3 headers
        :raises: ObjectNotFoundException, ObjectClerkException
        """
        response = retry_call(
            self._get_object_info,
            fkwargs={"bucket": bucket, "object_key": object_key},
            **self.retry_config,
        )
        return response["ResponseMetadata"].get("HTTPHeaders")

    @mutate_client_exceptions
    def _delete_object(self, bucket: str, object_key: str) -> None:
        """
        Executes the boto3.client.delete_object function with ClientError exceptions
        transformed to more precise ObjectClerk exceptions
        :param bucket: Bucket to delete the object from
        :param object_key: Key of the object in the bucket to delete
        :return: None
        """
        logger.debug(f"Attempting object delete: bucket={bucket}, object_key={object_key}")
        self.client.delete_object(Bucket=bucket, Key=object_key)

    def delete_object(self, bucket: str, object_key: str) -> None:
        """
        Deletes an object from an S3 endpoint retrying connection errors
        according to object clerk instance attributes
        :param bucket: Bucket to delete the object from
        :param object_key: Key of the object in the bucket to delete
        :return: None
        :raises: ObjectNotFoundException, ObjectClerkException
        """
        retry_call(
            self._delete_object,
            fkwargs={"bucket": bucket, "object_key": object_key},
            **self.retry_config,
        )

    @staticmethod
    def _data_to_bytes(
        data: Union[str, Path, BufferedReader, BytesIO, bytes]
    ) -> bytes:
        """
        Transform multiple types into a bytes object
        :param data: variable to convert
        :return: file converted to bytes
        """
        if isinstance(data, bytes):
            return data
        if isinstance(data, (BufferedReader, BytesIO)):
            data.seek(0)  # support retry
            return data.read()
        if isinstance(data, str):
            data = Path(data)
        if not isinstance(data, Path):
            raise TypeError("file must be of one of type str, Path, BufferedReader, BytesIO, bytes")
        try:
            data = data.open(mode="rb")
            bytes_obj = data.read()
            data.close()
        except OSError as e:
            raise ObjectSaveException(f"File cannot be opened: detail={e}")
        return bytes_obj

    @mutate_client_exceptions
    def _upload_object(self, bytes_obj: bytes, bucket: str, object_key: str) -> None:
        """
        Executes the boto3.client.upload_fileobj function with ClientError exceptions
        transformed to more precise ObjectClerk exceptions
        :param bucket: Bucket to upload the object to
        :param object_key: Key of the object in the bucket to upload to
        :param bytes_obj: bytes to upload
        :return: None
        """
        logger.debug(f"Attempting object upload: bucket={bucket}, object_key={object_key}")
        self.client.upload_fileobj(BytesIO(bytes_obj), Bucket=bucket, Key=object_key)

    @retry(ObjectVerificationException, **CHECKSUM_RETRY_CONFIG)
    def upload_object(
        self, object_data: Union[str, Path, BufferedReader, BytesIO, bytes], bucket: str, object_key: str, verify_checksum: bool = True
    ) -> None:
        """
        Uploads a data to the specified bucket and object key retrying connection errors according to instance
        retry specification and checksum failures according to internal config if requested (default)
        :param object_data: Data to upload
        :param bucket: Bucket to upload to
        :param object_key: Object Key in the bucket for the object after upload
        :param verify_checksum: Boolean indicator of whether to verify the checksum of the uploaded file matches
        what is in the S3 bucket
        :return: None
        :raises: ObjectVerificationException, ObjectSaveException, ObjectClerkException
        """
        bytes_obj = self._data_to_bytes(object_data)
        # get checksum before boto operations
        checksum = self._get_object_checksum(bytes_obj)
        if checksum == 'd41d8cd98f00b204e9800998ecf8427e':
            raise ObjectSaveException("Attempt to upload an empty file not allowed.")
        retry_call(
            self._upload_object,
            fkwargs={"bytes_obj": bytes_obj, "bucket": bucket, "object_key": object_key},
            **self.retry_config,
        )
        if verify_checksum:
            etag = self.get_object_info(bucket, object_key).get("etag")
            try:
                self._verify_checksum(checksum, etag)
            except ObjectVerificationException as e:
                logger.warning(f"Saved object does not match check sum: detail={e}")
                self.delete_object(bucket, object_key)
                logger.debug(f"Saved object is removed: bucket={bucket}, object_key={object_key}")
                raise e

    @mutate_client_exceptions
    def _copy_object(
        self, source_bucket: str, source_object_key: str, destination_bucket: str, destination_object_key: str
    ) -> None:
        """
        Execute boto3.client.copy_object function with ClientError exceptions
        transformed to more precise ObjectClerk exceptions
        :param source_bucket: Bucket of the object being copied
        :param source_object_key: Object key of the object being copied
        :param destination_bucket: Bucket to copy to
        :param destination_object_key: Object key of the copied object
        :return: None
        """
        logger.debug(f"Attempting object retrieval: source_bucket={source_bucket}, "
                     f"source_object_key={source_object_key}, destination_bucket={destination_bucket}, "
                     f"destination_object_key={destination_object_key}")
        copy_source = {"Bucket": source_bucket, "Key": source_object_key}
        self.client.copy_object(
            Bucket=destination_bucket, Key=destination_object_key, CopySource=copy_source
        )

    @retry(exceptions=ObjectVerificationException, **CHECKSUM_RETRY_CONFIG)
    def copy_object(
        self,
        source_bucket: str,
        source_object_key: str,
        destination_bucket: str,
        destination_object_key: str,
        verify_checksum: bool = True,
    ) -> None:
        """
        Create a copy of an object in an existing s3 bucket in another location retrying
        connection errors according to instance retry specification and checksum failures
        according to internal config if requested (default)
        :param source_bucket: Bucket of the object being copied
        :param source_object_key: Object key of the object being copied
        :param destination_bucket: Bucket to copy to
        :param destination_object_key: Object key of the copied object
        :param verify_checksum: Boolean indicator of whether to verify the checksum of the
        copied file matches the original
        :return: None
        :raises: ObjectVerificationException, ObjectSaveException, ObjectClerkException
        """
        source_object_info = self.get_object_info(source_bucket, source_object_key)
        if int(source_object_info["content-length"]) > MULTIPART_THRESHOLD:
            logger.warning(
                f"Attempt to copy file greater than multipart threshold: threshold={MULTIPART_THRESHOLD}, "
                f"size={source_object_info['content-length']}, bucket={source_bucket}, object_key={source_object_key}"
            )
            raise ObjectSaveException(
                f"API doesn't support uploads over {MULTIPART_THRESHOLD} bytes.  "
                f"Use the Boto3 mutltipart upload api."
            )

        retry_call(
            self._copy_object,
            fkwargs={
                "source_bucket": source_bucket,
                "source_object_key": source_object_key,
                "destination_bucket": destination_bucket,
                "destination_object_key": destination_object_key,
            },
            **self.retry_config,
        )

        if verify_checksum:
            destination_object_info = self.get_object_info(
                destination_bucket, destination_object_key
            )
            if source_object_info["etag"] == destination_object_info["etag"]:
                return
            self.delete_object(destination_bucket, destination_object_key)
            logger.warning(
                f"Copied object does not match check sum: source_bucket={source_bucket}, "
                f"source_object_key={source_bucket}, source_checksum={source_object_info['etag']}, "
                f"destination_bucket={destination_bucket}, destination_object_key={destination_object_key}, "
                f"destination_check_sum={destination_object_info['etag']}"
            )
            self.delete_object(destination_bucket, destination_object_key)
            logger.debug(
                f"Copied object is removed: bucket={destination_bucket}, object_key={destination_object_key}"
            )
            raise ObjectVerificationException(
                f"Object checksum verification failed: "
                f"source_etag={source_object_info['etag']}, "
                f"destination_etag={destination_object_info['etag']}"
            )
