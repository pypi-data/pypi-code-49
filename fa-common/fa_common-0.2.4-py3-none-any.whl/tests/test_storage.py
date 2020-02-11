import os

from starlette.testclient import TestClient
from fastapi import FastAPI, UploadFile
from fa_common import create_app, force_sync, utils, start_app
from fa_common.storage import get_storage_client, File

from .conftest import clean_env

dirname = os.path.dirname(__file__)
test_data_path = os.path.join(dirname, "data")


def exercise_storage(path: str):
    bucket_name = "facf-test-bucket"

    app = create_app(env_path=path)
    force_sync(start_app)(app)
    utils.current_app = app

    assert isinstance(app, FastAPI)
    client = get_storage_client()

    force_sync(client.make_bucket)(bucket_name)
    assert force_sync(client.bucket_exists)(bucket_name)

    filename = "file1.txt"
    file = UploadFile(
        filename=filename, file=open(os.path.join(test_data_path, filename), "r")
    )

    file_ref: File = force_sync(client.upload_file)(file, bucket_name, "files")
    assert file_ref is not None

    files = force_sync(client.list_files)(bucket_name, "files")
    assert files is not None and len(files) == 1

    force_sync(client.delete_bucket)(bucket_name)
    assert not force_sync(client.bucket_exists)(bucket_name)

    clean_env()


def test_firbase_storage(env_path):

    exercise_storage(env_path)


def test_minio_storage(minio_env_path):

    exercise_storage(minio_env_path)
