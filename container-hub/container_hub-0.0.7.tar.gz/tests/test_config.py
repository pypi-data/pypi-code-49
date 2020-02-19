import pytest
import os


@pytest.fixture
def docker_simple_settings():
    # settings = LazySettings('tests.test_files.settings')
    os.environ.update({"SIMPLE_SETTINGS": "tests.test_files.docker_settings"})
    from container_hub.config import get_settings
    yield get_settings()
    os.environ.pop("SIMPLE_SETTINGS")

@pytest.fixture
def docker_django_settings():
    # settings = LazySettings('tests.test_files.settings')
    os.environ.update({"DJANGO_SETTINGS_MODULE": "tests.test_files.django_settings"})
    from container_hub.config import get_settings
    yield get_settings()
    os.environ.pop("DJANGO_SETTINGS_MODULE")


def test_import_error():
    with pytest.raises(ImportError):
        from container_hub import settings

def test_smoke_django(docker_django_settings):
    assert docker_django_settings.CONTAINER_CARRIER == 'docker'


def test_smoke_simple(docker_simple_settings):
    assert docker_simple_settings.CONTAINER_CARRIER == 'docker'


