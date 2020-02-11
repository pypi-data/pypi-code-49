import logging
import os
from datetime import datetime
from enum import Enum
from typing import List, Set, Optional

from dotenv import load_dotenv
from pydantic import AnyUrl, BaseSettings, SecretBytes, SecretStr

# from app.shared.utils import auth


class StorageType(str, Enum):
    MINIO = "MINIO"
    GCP_STORAGE = "GCP_STORAGE"
    FIREBASE_STORAGE = "FIREBASE_STORAGE"
    NONE = "NONE"


class DatabaseType(str, Enum):
    MONGODB = "MONGODB"
    GCP_FIRESTORE = "GCP_FIRESTORE"
    NONE = "NONE"


class Settings(BaseSettings):
    VERSION: str = "0.2.4"
    API_VERSION: int = 1
    API_PRE_PATH: str = f"/api/v{API_VERSION}"

    SENTRY_DSN: Optional[AnyUrl] = None
    DEBUG: bool = False
    UNIT_TESTING: bool = False

    SECRET_KEY: SecretBytes = os.urandom(32)
    BUILD_DATE: Optional[datetime] = None
    PROJECT_NAME: str = "FastAPI Backend"
    BACKEND_CORS_ORIGINS: Set[str] = set()
    MINIO_SECRET_KEY: Optional[SecretStr] = None
    MINIO_ACCESS_KEY: Optional[str] = None
    MINIO_ENDPOINT: Optional[str] = None
    MINIO_SSL: bool = False

    BUCKET_NAME: str = ""
    BUCKET_PREFIX: str = ""
    BUCKET_USER_FOLDER: str = "user-storage/"

    AUTH0_DOMAIN: str = ""
    API_AUDIENCE: str = ""
    OAUTH2_AUTH_URL: str = f"https://{AUTH0_DOMAIN}/authorize?audience={API_AUDIENCE}"
    JWT_ALGORITHMS: List[str] = ["RS256"]

    # logging configuration
    LOGGING_LEVEL: int = logging.DEBUG if DEBUG else logging.INFO

    DATABASE_TYPE: DatabaseType = DatabaseType.GCP_FIRESTORE  # FIRESTORE or MONGODB
    STORAGE_TYPE: StorageType = StorageType.GCP_STORAGE
    USE_FIREBASE: bool = (
        STORAGE_TYPE == StorageType.FIREBASE_STORAGE
        or DATABASE_TYPE == DatabaseType.GCP_FIRESTORE
    )

    MONGODB_DSN: Optional[str] = None
    MONGODB_DBNAME: Optional[str] = None
    mongodb_min_pool_size: int = 0
    mongodb_max_pool_size: int = 100
    TZ: str = "Australia/Perth"
    APP_PATH: str = "fa_common"
    FASTAPI_APP: str = ""

    debug_timing: bool = False

    # class Config:
    #     env_prefix = 'FA_COMMON_'  # defaults to no prefix, i.e. ""
    #     fields = {
    #         'auth_key': {
    #             'env': 'my_auth_key',
    #         },
    #         'redis_dsn': {
    #             'env': ['service_redis_dsn', 'redis_url']
    #         }
    #     }


settings: Optional[Settings] = None


def get_settings(env_path=None) -> Settings:
    # Load env variables from .env file
    if env_path is not None:
        load_dotenv(dotenv_path=env_path)

    global settings
    if settings is None or env_path is not None:
        settings = Settings()

    return settings
