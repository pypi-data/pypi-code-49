import os
from unittest.mock import Mock

import pytest

from miniMinio import create_connection, get_buckets, get_all_object_details_in_bucket, \
    get_single_object_from_bucket_to_file, get_single_object_content_bytes
from miniMinio.utils import path_leaf_last


class MockBucket:
    def __init__(self, name, creation_date):
        self.name = name
        self.creation_date = creation_date


class MockObject:
    def __init__(self, object_name, creation_date):
        self.object_name = object_name
        self.creation_date = creation_date


@pytest.mark.parametrize("hostname",
                         [(("minio")),
                          (("local"))])
def test_create_connection(hostname, snapshot):
    access_key = "test_access_key"
    secret_key = "test_secret_key"
    client = create_connection(hostname, access_key, secret_key)
    if type(client) is str:
        snapshot.assert_match(client)
    # No connections actually made


def test_get_buckets(snapshot):
    mock_client = Mock()
    mock_client.list_buckets.return_value = [
        MockBucket("bucket1", "bucket1_date"),
        MockBucket("bucket2", "bucket2_date")
    ]
    result = get_buckets(mock_client)
    snapshot.assert_match(result)


@pytest.mark.parametrize("mock_client", [
    (("local")),
    (("remote"))
])
def test_get_buckets_local(mock_client, snapshot):
    if mock_client == "remote":
        mock_remote_dir = os.path.join(__file__, 'data')
    else:
        mock_remote_dir = None
    results = get_buckets(mock_client, mock_remote_dir)
    names = [result[0] for result in results]
    names = [path_leaf_last(name) for name in names]
    names.sort()
    snapshot.assert_match(names)


@pytest.mark.parametrize('filter_object', [
    (("file")),
    (("folder")),
    (("file", "folder")),
    (('excel')),
    (('excel', 'folder'))
])
def test_get_all_object_details_in_bucket(filter_object, snapshot):
    mock_client = Mock()
    mock_client.list_objects.return_value = [
        MockObject("bucket1/object1.pdf", "pdf_date"),
        MockObject("bucket2/folder/", "folder_date"),
        MockObject("bucket1/object2.xlsx", "xlsx_date"),
        MockObject("bucket2/object3.xls", "xls_date")
    ]
    bucket_name = "placeholder"
    attributes = ["creation_date"]
    results = get_all_object_details_in_bucket(mock_client, bucket_name, attributes, filter_object)
    names = [result[0] for result in results]
    names = [path_leaf_last(name) for name in names]
    names.sort()
    snapshot.assert_match(names)


@pytest.mark.parametrize('filter_object', [
    (("file")),
    (("folder")),
    (("file", "folder")),
    (('excel')),
    (('excel', 'folder'))
])
def test_get_all_object_details_in_bucket_local_fs(filter_object, snapshot):
    bucket_name = ""
    attributes = ["object_name"]
    results = get_all_object_details_in_bucket("local", bucket_name, attributes, filter_object)
    names = [result[0] for result in results]
    names = [path_leaf_last(name) for name in names]
    names.sort()
    snapshot.assert_match(names)


@pytest.mark.parametrize('filter_object', [
    (("file")),
    (("folder")),
    (("file", "folder")),
    (('excel')),
    (('excel', 'folder'))
])
def test_get_all_object_details_in_bucket_remote_fs(filter_object, snapshot):
    bucket_name = os.path.join(os.path.dirname(__file__), 'data')
    attributes = ["object_name"]
    results = get_all_object_details_in_bucket("remote", bucket_name, attributes, filter_object)
    names = [result[0] for result in results]
    names = [path_leaf_last(name) for name in names]
    names.sort()
    snapshot.assert_match(names)


def test_get_single_objects_from_bucket_to_file():
    environment = os.environ.get('ENVIRON', "local")
    if environment == "local":
        hostname = "localhost:9000"
    elif environment == "test":
        hostname = "minio:9000"
    client = create_connection(hostname, "minioadmin", "minioadmin", secure=False)
    object_name = "file1.txt"
    dir_path = os.path.join(os.path.realpath(os.path.dirname(__file__)), "receive_file1.txt")
    bucket_name = "buckettest"
    get_single_object_from_bucket_to_file(client, object_name, dir_path, bucket_name)
    os.remove(dir_path)  # remove to see file
    return


def test_get_single_objects_from_bucket_to_file_fs():
    client = create_connection("remote", "minioadmin", "minioadmin", secure=False)
    object_name_list = os.path.join(os.path.realpath(os.path.dirname(__file__)), "data", "buckettest", "file1.txt")
    dir_path = os.path.join(os.path.realpath(os.path.dirname(__file__)), "receive_file1.txt")
    get_single_object_from_bucket_to_file(client, object_name_list, dir_path)
    os.remove(dir_path)  # remove to see file
    return


def test_get_single_object_content_bytes(snapshot):
    environment = os.environ.get('ENVIRON', "local")
    if environment == "local":
        hostname = "localhost:9000"
    elif environment == "test":
        hostname = "minio:9000"
    client = create_connection(hostname, "minioadmin", "minioadmin", secure=False)
    bucket_name = "buckettest"
    object_name = "BigBook.xlsx"
    result = get_single_object_content_bytes(client, object_name, bucket_name)
    snapshot.assert_match(result)


def test_get_single_object_content_bytes_fs(snapshot):
    client = create_connection("remote", "minioadmin", "minioadmin", secure=False)
    object_name = os.path.join(os.path.realpath(os.path.dirname(__file__)), "data", "buckettest", "BigBook.xlsx")
    result = get_single_object_content_bytes(client, object_name)
    snapshot.assert_match(result)
