import os
import pytest
from fa_common.auth import AuthUser

dirname = os.path.dirname(__file__)
env_file = os.path.join(dirname, ".env")
minio_env_file = os.path.join(dirname, ".env-minio")


@pytest.fixture(scope="module")
def env_path(scope="module"):
    return env_file


@pytest.fixture(scope="module")
def minio_env_path(scope="module"):
    return minio_env_file


def clean_env():
    os.environ.pop("STORAGE_TYPE", None)
    os.environ.pop("BUCKET_PREFIX", None)
    os.environ.pop("BUCKET_NAME", None)
    os.environ.pop("BUCKET_USER_FOLDER", None)
    os.environ.pop("DATABASE_TYPE", None)
    os.environ.pop("GOOGLE_APPLICATION_CREDENTIALS", None)
    os.environ.pop("ENABLE_FIREBASE", None)
    os.environ.pop("MINIO_ENDPOINT", None)
    os.environ.pop("MINIO_ACCESS_KEY", None)
    os.environ.pop("MINIO_SECRET_KEY", None)


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed ({})".format(previousfailed.name))


async def get_test_user() -> AuthUser:
    payload = {
        "sub": "test-sub",
        "name": "Test User",
        "email": "test.user@test.com",
        "nickname": "test.user",
        "email_verified": True,
        "picture": None,
        "updated_at": None,
        "scopes": [],
    }

    return AuthUser(**payload)
