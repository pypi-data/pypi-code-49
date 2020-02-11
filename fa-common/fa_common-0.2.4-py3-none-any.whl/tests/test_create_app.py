from starlette.testclient import TestClient

from fastapi import FastAPI
from fa_common import create_app, get_settings


def test_create_app(env_path):

    app = create_app(env_path=env_path)
    assert isinstance(app, FastAPI)

    settings = get_settings()
    assert settings.PROJECT_NAME == "Fast Api Commons Test"
