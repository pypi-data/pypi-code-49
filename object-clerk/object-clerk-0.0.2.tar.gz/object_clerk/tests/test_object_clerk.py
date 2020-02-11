"""
Tests for the ObjectClerk API

Tests marked @pytest.mark.development require environment variables
to specify an s3 instance location and tokens
"""
from os import environ
from hashlib import md5
from pathlib import Path
from io import BytesIO, BufferedReader

import boto3
import pytest

from object_clerk import ObjectClerk, ObjectNotFoundException

HOST = environ.get('HOST')
PORT = int(environ.get('PORT', 1))
ACCESS_KEY = environ.get('ACCESS_KEY')
SECRET_KEY = environ.get('SECRET_KEY')
# Configure retry to fail quickly on connection errors
RETRY = {'retry_delay': 1, 'retry_backoff': 1, 'retry_jitter': 1, 'retry_max_delay': 1, 'retry_tries': 1}
BUCKET = "test_object_clerk"


@pytest.fixture(scope="session")
def boto_client():
    endpoint_url = f"http://{HOST}:{PORT}/"
    return boto3.client(
            service_name="s3",
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
            endpoint_url=endpoint_url,
        )


@pytest.fixture(scope="module")
def object_store_data(boto_client):
    # Create Test Bucket
    boto_client.create_bucket(Bucket=BUCKET)
    with open("object_clerk/tests/example_object", mode='rb') as f:
        # Add Get file
        boto_client.upload_fileobj(f, Bucket=BUCKET, Key="get_file")
    with open("object_clerk/tests/example_object", mode='rb') as f:
        # Add Delete file
        boto_client.upload_fileobj(f, Bucket=BUCKET, Key="delete_file")
    with open("object_clerk/tests/example_object", mode='rb') as f:
        # Add Copy File
        boto_client.upload_fileobj(f, Bucket=BUCKET, Key="copy_file")
    yield
    # Delete objects
    boto_client.delete_object(Bucket=BUCKET, Key="get_file")
    boto_client.delete_object(Bucket=BUCKET, Key="delete_file")
    boto_client.delete_object(Bucket=BUCKET, Key="copy_file")
    # Delete Bucket
    boto_client.delete_bucket(Bucket=BUCKET)


@pytest.fixture()
def object_clerk():
    return ObjectClerk(
        host=HOST,
        port=PORT,
        access_key=ACCESS_KEY,
        secret_key=SECRET_KEY,
        **RETRY
    )


@pytest.mark.development
def test_get_object(object_clerk, object_store_data):
    response = object_clerk.get_object(BUCKET, "get_file")
    assert response == b'EXAMPLE OBJECT FOR TESTING OBJECT CLERK OPERATIONS'


@pytest.mark.development
@pytest.mark.parametrize(
    "bucket, key",
    [
        pytest.param(BUCKET, "foo", id="bad_key"),
        pytest.param("foo", "get_file", id="bad_bucket"),
        pytest.param("foo", "foo", id="bad_both"),
    ]
)
def test_get_object_not_found(object_clerk, object_store_data, bucket, key):
    with pytest.raises(ObjectNotFoundException):
        object_clerk.get_object(bucket, key)


@pytest.mark.development
def test_get_object_info(object_clerk, object_store_data):
    response = object_clerk.get_object_info(BUCKET, "get_file")
    with open("object_clerk/tests/example_object", mode='rb') as f:
        checksum = md5(f.read()).hexdigest()
    assert response['etag'][1:-1] == checksum


@pytest.mark.development
@pytest.mark.parametrize(
    "bucket, key",
    [
        pytest.param(BUCKET, "foo", id="bad_key"),
        pytest.param("foo", "get_file", id="bad_bucket"),
        pytest.param("foo", "foo", id="bad_both"),
    ]
)
def test_get_object_info_not_found(object_clerk, object_store_data, bucket, key):
    with pytest.raises(ObjectNotFoundException):
        object_clerk.get_object_info(bucket, key)


@pytest.mark.development
def test_copy_object(object_clerk, object_store_data):
    object_clerk.copy_object(BUCKET, "copy_file", BUCKET, "copied_file")
    source_checksum = object_clerk.get_object_info(BUCKET, "copy_file")['etag'][1:-1]
    destination_checksum = object_clerk.get_object_info(BUCKET, "copied_file")['etag'][1:-1]
    # clean up
    object_clerk.delete_object(BUCKET, "copied_file")
    assert source_checksum == destination_checksum


@pytest.mark.development
def test_delete_object(object_clerk, object_store_data):
    response = object_clerk.get_object_info(BUCKET, "delete_file")
    assert isinstance(response, dict)
    object_clerk.delete_object(BUCKET, "delete_file")
    with pytest.raises(ObjectNotFoundException):
        _ = object_clerk.get_object_info(BUCKET, "delete_file")

#str, Path, BufferedReader, BytesIO, bytes
@pytest.mark.development
@pytest.mark.parametrize(
    "file",
    [
        pytest.param("object_clerk/tests/example_object", id="str"),
        pytest.param(Path("object_clerk/tests/example_object"), id="Path"),
        pytest.param(BufferedReader(BytesIO(b'EXAMPLE OBJECT FOR TESTING OBJECT CLERK OPERATIONS')), id="BufferedReader"),
        pytest.param(BytesIO(b'EXAMPLE OBJECT FOR TESTING OBJECT CLERK OPERATIONS'), id="BytesIO"),
        pytest.param(b'EXAMPLE OBJECT FOR TESTING OBJECT CLERK OPERATIONS', id="bytes"),
    ]
)
def test_upload_object(object_clerk, object_store_data, file):
    object_clerk.upload_object(file, BUCKET, "upload_file")
    with open("object_clerk/tests/example_object", mode='rb') as f:
        checksum = md5(f.read()).hexdigest()
    etag = object_clerk.get_object_info(BUCKET, "upload_file")['etag']
    # clean up
    object_clerk.delete_object(BUCKET, "upload_file")
    assert etag[1:-1] == checksum


def test_pass():
    # work around for pipeline without any non development marked tests
    assert True
