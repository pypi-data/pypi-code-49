"""
Tests for the ObjectClerk API

Tests marked @pytest.mark.development require environment variables
to specify an s3 instance location and tokens
"""
from os import environ
from hashlib import md5
from pathlib import Path
from io import BytesIO, BufferedReader
from typing import Tuple
from uuid import uuid4

import boto3
import pytest

from object_clerk import ObjectClerk, ObjectNotFoundException, ObjectSaveException
from object_clerk.clerk import MULTIPART_THRESHOLD


"""
S3 endpoint configuration
"""
HOST = environ.get("HOST")
PORT = int(environ.get("PORT", 1))
ACCESS_KEY = environ.get("ACCESS_KEY")
SECRET_KEY = environ.get("SECRET_KEY")
# Configure retry to fail quickly on connection errors
RETRY = {
    "retry_delay": 1,
    "retry_backoff": 1,
    "retry_jitter": 1,
    "retry_max_delay": 1,
    "retry_tries": 1,
}


"""
Fixtures for data and other dependencies
"""


@pytest.fixture(scope="session")
def boto_client() -> boto3.client:
    """
    Configure a boto3.client for s3
    :return: boto3.client instance
    """
    endpoint_url = f"http://{HOST}:{PORT}/"
    return boto3.client(
        service_name="s3",
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        endpoint_url=endpoint_url,
    )


@pytest.fixture(scope="session")
def bucket(boto_client) -> str:
    """
    Create a bucket and remove it at the end of the tests
    :param boto_client: boto3.client instance
    :return: bucket name str
    """
    bucket_name = "test_object_clerk"
    # Create Test Bucket
    boto_client.create_bucket(Bucket=bucket_name)
    yield bucket_name
    # Delete Bucket
    boto_client.delete_bucket(Bucket=bucket_name)


@pytest.fixture(scope="session")
def move_bucket(boto_client) -> str:
    """
    Create a bucket and remove it at the end of the tests
    :param boto_client: boto3.client instance
    :return: bucket name str
    """
    bucket_name = "test_object_clerk_move"
    # Create Test Bucket
    boto_client.create_bucket(Bucket=bucket_name)
    yield bucket_name
    # Delete Bucket
    boto_client.delete_bucket(Bucket=bucket_name)


@pytest.fixture(scope="session")
def object_store_data(boto_client, bucket) -> None:
    """
    Create objects for test cases in the bucket specified
    by the bucket param
    :param boto_client: boto3.client instance
    :param bucket: str name of the bucket to load the data in
    :return:
    """
    with open("object_clerk/tests/example_object", mode="rb") as f:
        # Add Get file
        boto_client.upload_fileobj(f, Bucket=bucket, Key="get_file")
    with open("object_clerk/tests/example_object", mode="rb") as f:
        # Add Delete file
        boto_client.upload_fileobj(f, Bucket=bucket, Key="delete_file")
    with open("object_clerk/tests/example_object", mode="rb") as f:
        # Add Copy File
        boto_client.upload_fileobj(f, Bucket=bucket, Key="copy_file")
    with open("object_clerk/tests/example_object", mode="rb") as f:
        # Add Copy File
        boto_client.upload_fileobj(f, Bucket=bucket, Key="move_file")
    yield
    # Delete objects
    boto_client.delete_object(Bucket=bucket, Key="get_file")
    boto_client.delete_object(Bucket=bucket, Key="delete_file")
    boto_client.delete_object(Bucket=bucket, Key="copy_file")
    # in case of test case failure remove the move object
    boto_client.delete_object(Bucket=bucket, Key="move_file")


@pytest.fixture(scope="function", params=[1, 3, 5, 8, 13, 16, 17])
def local_file(tmp_path_factory, request) -> Tuple[Path, int]:
    """
    Creates files locally of varying sizes based upon fixture params
    specifying a size in MB
    :param tmp_path_factory: pytest built in fixture for managing a temp directory
        3 tmp dirs are retained over test runs
    :param request: pytest built in fixture for accessing test case metadata e.g.
        fixture params
    :return: Tuple [local file path, size of file]
    """
    MB = 1024 * 1024
    size = request.param  # size in MB
    tmp_path = tmp_path_factory.mktemp(f"test_file_{size}_MB", numbered=False)

    file = tmp_path.joinpath(f"{size}_MB.file")
    with file.open(mode="wb") as f:
        if size == 0:
            f.write(b"")
        else:
            f.seek(size * MB - 1)
            f.write(b"\0")
    return file, size * MB


@pytest.fixture(scope="session")
def object_clerk() -> ObjectClerk:
    """
    Fixture providing a configured instance of the Object clerk
    :return: ObjectClerk instance
    """
    return ObjectClerk(host=HOST, port=PORT, access_key=ACCESS_KEY, secret_key=SECRET_KEY, **RETRY)


"""
Test Cases
"""


@pytest.mark.development
def test_get_object(object_clerk, object_store_data, bucket):
    """
    Given: Object clerk instance, object in the object store
    When: Getting an existing object
    Then: expected object is retrieved
    :param object_clerk: instance of ObjectClerk
    :param object_store_data: fixture providing objects loaded in an object store
    :param bucket: name of the bucket the objects are loaded in
    :return: None
    """
    # When
    response = object_clerk.get_object(bucket, "get_file")
    # Then
    assert response == b"EXAMPLE OBJECT FOR TESTING OBJECT CLERK OPERATIONS"


@pytest.mark.development
@pytest.mark.parametrize(
    "bucket_name, key",
    [
        pytest.param(object, "foo", id="bad_key"),
        pytest.param("foo", "get_file", id="bad_bucket"),
        pytest.param("foo", "foo", id="bad_both"),
    ],
)
def test_get_object_not_found(object_clerk, bucket, bucket_name, key):
    """
    Given: ObjectClerk instance
    When: getting an object that is not there
    Then: receive an ObjectNotFoundException
    :param object_clerk: ObjectClerk instance
    :param bucket: Fixture providing a bucket that exists
    :param bucket_name: name of the bucket to attempt retrieval from
    :param key: name of the object to attempt retrieval of
    :return: None
    """

    # substitute bucket name with a valid bucket from the fixture
    if bucket_name is object:
        bucket_name = bucket
    # When Then
    with pytest.raises(ObjectNotFoundException):
        object_clerk.get_object(bucket_name, key)


@pytest.mark.development
def test_get_object_info(object_clerk, object_store_data, bucket):
    """
    Given: ObjectClerk instance, object in object store
    When: Getting object info for object that is present
    Then: receive expected checksum
    :param object_clerk: ObjectClerk instance
    :param object_store_data: Fixture that loaded objects into the object store
    :param bucket: Bucket containing the expected objects
    :return: None
    """
    with open("object_clerk/tests/example_object", mode="rb") as f:
        checksum = md5(f.read()).hexdigest()
    # When
    response = object_clerk.get_object_info(bucket, "get_file")
    # Then
    assert response["etag"][1:-1] == checksum


@pytest.mark.development
@pytest.mark.parametrize(
    "bucket_name, key",
    [
        pytest.param(object, "foo", id="bad_key"),
        pytest.param("foo", "get_file", id="bad_bucket"),
        pytest.param("foo", "foo", id="bad_both"),
    ],
)
def test_get_object_info_not_found(object_clerk, bucket, bucket_name, key):
    """
    Given: ObjectClerk instance
    When: getting an objects info that is not there
    Then: receive an ObjectNotFoundException
    :param object_clerk: ObjectClerk instance
    :param bucket: Fixture providing a bucket that exists
    :param bucket_name: name of the bucket to attempt retrieval from
    :param key: name of the object to attempt retrieval of
    :return: None
    """
    # substitute bucket name with a valid bucket from the fixture
    if bucket_name is object:
        bucket_name = bucket
    # When Then
    with pytest.raises(ObjectNotFoundException):
        object_clerk.get_object_info(bucket_name, key)


@pytest.mark.development
def test_copy_object(object_clerk, object_store_data, bucket):
    """
    Given: ObjectClerk instance, object to copy in object store
    When: Copying object
    Then: Copy of object in the new destination
    :param object_clerk: ObjectClerk instance
    :param object_store_data: Fixture that loaded objects in the object store
    :param bucket: name of the bucket the loaded objects are in
    :return: None
    """
    source_checksum = object_clerk.get_object_info(bucket, "copy_file")["etag"][1:-1]
    # When
    object_clerk.copy_object(bucket, "copy_file", bucket, "copied_file")
    destination_checksum = object_clerk.get_object_info(bucket, "copied_file")["etag"][1:-1]
    # clean up
    object_clerk.delete_object(bucket, "copied_file")
    # Then
    assert source_checksum == destination_checksum


@pytest.mark.development
def test_delete_object(object_clerk, object_store_data, bucket):
    """
    Given: ObjectClerk instance, object in the object store
    When: Deleting the existing object
    Then: Object is not found when attempting retrieval
    :param object_clerk: ObjectClerk instance
    :param object_store_data: Fixture that loaded data in the object store
    :param bucket: Name of the bucket the object is loaded in
    :return: None
    """
    response = object_clerk.get_object_info(bucket, "delete_file")
    assert isinstance(response, dict)
    # When
    object_clerk.delete_object(bucket, "delete_file")
    # Then
    with pytest.raises(ObjectNotFoundException):
        _ = object_clerk.get_object_info(bucket, "delete_file")


# str, Path, BufferedReader, BytesIO, bytes
@pytest.mark.development
@pytest.mark.parametrize(
    "file",
    [
        pytest.param("object_clerk/tests/example_object", id="str"),
        pytest.param(Path("object_clerk/tests/example_object"), id="Path"),
        pytest.param(
            BufferedReader(BytesIO(b"EXAMPLE OBJECT FOR TESTING OBJECT CLERK OPERATIONS")),
            id="BufferedReader",
        ),
        pytest.param(BytesIO(b"EXAMPLE OBJECT FOR TESTING OBJECT CLERK OPERATIONS"), id="BytesIO"),
        pytest.param(b"EXAMPLE OBJECT FOR TESTING OBJECT CLERK OPERATIONS", id="bytes"),
    ],
)
def test_upload_object(object_clerk, bucket, file):
    """
    Given: ObjectClerk instance, file to upload
    When: upload object to object store
    Then: Object can be retrieved from the object store
    :param object_clerk: ObjectClerk instance
    :param bucket: Name of the bucket to upload to
    :param file: File to upload
    :return: None
    """
    with open("object_clerk/tests/example_object", mode="rb") as f:
        checksum = md5(f.read()).hexdigest()
    # When
    object_clerk.upload_object(file, bucket, "upload_file")
    etag = object_clerk.get_object_info(bucket, "upload_file")["etag"]
    # clean up
    object_clerk.delete_object(bucket, "upload_file")
    # Then
    assert etag[1:-1] == checksum


@pytest.mark.development
def test_upload_object_checksums_by_size(object_clerk, local_file, bucket):
    """
    Given: ObjectClerk instance, object to upload and its size
    :param object_clerk: ObjectClerk instance
    :param local_file: Fixture providing a file and its size
    :param bucket: Bucket to load the object into
    :return: None
    """

    def calculate_s3_etag():
        """
        Alternate checksum calculation implementation to validate object clerk
        checksum calculation
        :return: expected s3 etag
        """
        md5s = []
        with file_path.open("rb") as fp:
            while True:
                data = fp.read(MULTIPART_THRESHOLD)
                if not data:
                    break
                md5s.append(md5(data))
        if len(md5s) == 1 and size != MULTIPART_THRESHOLD:
            return '"{}"'.format(md5s[0].hexdigest())
        digests = b"".join(m.digest() for m in md5s)
        digests_md5 = md5(digests)
        return '"{}-{}"'.format(digests_md5.hexdigest(), len(md5s))

    file_path, size = local_file
    object_key = f"object_clerk/test/{uuid4().hex}.file"
    checksum = calculate_s3_etag()
    # When
    object_clerk.upload_object(file_path, bucket, object_key)

    etag = object_clerk.get_object_info(bucket, object_key)["etag"]
    # clean up
    object_clerk.delete_object(bucket, object_key)
    # Then
    assert etag == checksum


@pytest.mark.development
def test_upload_empty_file(object_clerk, bucket):
    """
    Given: Object clerk instance
    When: Uploading an empty file
    Then: Receive a ObjectSaveException
    :param object_clerk: ObjectClerk instance
    :param bucket: Name of the bucket to upload to
    :return: None
    """
    # When Then
    with pytest.raises(ObjectSaveException):
        object_clerk.upload_object(b"", bucket, "object_clerk/test/empty")


@pytest.mark.development
def test_move_object(object_clerk, bucket, object_store_data, move_bucket):
    """
    Given: ObjectClerk instance, object that exists
    When: Move existing object to new bucket, object key
    Then: Object is available in new location and not available in the old one
    :param object_clerk: ObjectClerk instance
    :param bucket: Bucket the existing object is in
    :param object_store_data: Fixture that loaded objects
    :param move_bucket: Bucket to move to
    :return: None
    """
    source_checksum = object_clerk.get_object_info(bucket, "copy_file")["etag"][1:-1]
    # When
    object_clerk.move_object(bucket, "move_file", move_bucket, "moved_file")
    destination_checksum = object_clerk.get_object_info(move_bucket, "moved_file")["etag"][1:-1]
    # clean up
    object_clerk.delete_object(move_bucket, "moved_file")
    # Then
    assert source_checksum == destination_checksum
    with pytest.raises(ObjectNotFoundException):
        object_clerk.get_object_info(bucket, "move_file")


def test_pass():
    # work around for pipeline without any non development marked tests
    assert True
