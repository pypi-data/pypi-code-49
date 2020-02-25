from fastapi import FastAPI

from fa_common import StorageType, get_settings, logger
from .base_client import BaseClient

# from minio.error import ResponseError


def setup_storage(app: FastAPI) -> None:
    settings = get_settings()
    if settings.STORAGE_TYPE == StorageType.MINIO:
        from minio import Minio

        if (
            settings.MINIO_SECRET_KEY is None
            or settings.MINIO_ACCESS_KEY is None
            or settings.MINIO_ENDPOINT is None
        ):
            raise ValueError("Missing minio settings from env variables")

        minioClient = Minio(
            settings.MINIO_ENDPOINT,
            access_key=settings.MINIO_ACCESS_KEY,
            secret_key=settings.MINIO_SECRET_KEY.get_secret_value(),
            secure=settings.MINIO_SSL,
        )
        app.minio = minioClient  # type: ignore
    elif (
        settings.STORAGE_TYPE == StorageType.GCP_STORAGE
        or settings.STORAGE_TYPE == StorageType.FIREBASE_STORAGE
    ):
        from google.cloud import storage

        # Uses GOOGLE_APPLICATION_CREDENTIALS Env Var
        gcp_storage_client = storage.Client()
        app.gcp_storage = gcp_storage_client  # type: ignore
    elif settings == StorageType.NONE:
        logger.info("Storage set to NONE and cannot be used")
        return
    else:
        raise ValueError("STORAGE_TYPE Setting is not a valid storage option.")


def get_storage_client() -> BaseClient:
    if get_settings().STORAGE_TYPE == StorageType.MINIO:
        from .minio_client import MinioClient

        return MinioClient()
    elif get_settings().STORAGE_TYPE == StorageType.GCP_STORAGE:
        from .gcp_client import GoogleStorageClient

        return GoogleStorageClient()
    elif get_settings().STORAGE_TYPE == StorageType.FIREBASE_STORAGE:
        from .gcp_client import FirebaseStorageClient

        return FirebaseStorageClient()

    raise ValueError("STORAGE_TYPE Setting is not a valid storage option.")
