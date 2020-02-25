from io import BytesIO
import asyncio

from google.cloud import storage
from google.cloud.exceptions import Conflict, NotFound, GoogleCloudError
from google.cloud.storage.bucket import Bucket, Blob

from typing import List, Optional, Union
from fastapi import UploadFile
from .base_client import BaseClient
from fa_common import (
    sizeof_fmt,
    force_async,
    get_current_app,
    logger as LOG,
    StorageError,
    get_settings,
)
from .model import File


class GoogleStorageClient(BaseClient):
    """
    Singleton client for interacting with GoogleStorage. Note we are wrapping all the call in threads to
    enable async support to a sync library.
    Please don't use it directly, use `core.storage.utils.get_storage_client`.
    """

    __instance = None
    gcp_storage: storage.Client = None

    def __new__(cls) -> "GoogleStorageClient":
        """
        Get called before the constructor __init__ and allows us to return a singleton instance.

        Returns:
            [GoogleStorageClient] -- [Singleton Instance of client]
        """
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            app = get_current_app()
            cls.__instance.gcp_storage = app.gcp_storage  # type: ignore
        return cls.__instance

    async def make_bucket(self, name: str) -> None:
        try:
            await force_async(self.gcp_storage.create_bucket)(name)
        except Conflict:
            LOG.warning(f"Bucket {name} already exists")

    async def bucket_exists(self, name: str) -> bool:
        bucket = await force_async(self.gcp_storage.lookup_bucket)(name)
        if bucket is None:
            return False
        return True

    async def delete_bucket(self, name: str):
        try:
            bucket = await self._get_bucket(name)
            return await force_async(bucket.delete)(force=True)
        except ValueError:
            LOG.warning(
                f"Too many object in the bucket, unable to delete Bucket: {name}"
            )
            raise StorageError(
                f"Too many object in the bucket, unable to delete Bucket: {name}"
            )

    async def _get_bucket(self, name: str) -> Bucket:
        """
        Internal method to GCP bucket
        """
        try:
            return await force_async(self.gcp_storage.get_bucket)(name)
        except NotFound:
            LOG.error("Trying to get bucket {} that doesn't exist", name)
            raise StorageError(f"Trying to get bucket {name} that doesn't exist")

    async def _get_blob(self, bucket_name, path):
        """
        Internal method to get GCP blob reference
        """
        bucket = await self._get_bucket(bucket_name)
        return bucket.blob(self.convert_path_in(path, bucket_name))

    async def _list_blobs(self, bucket_name, prefix) -> List[Blob]:
        bucket = await self._get_bucket(bucket_name)
        return await force_async(bucket.list_blobs)(
            prefix=self.convert_path_in(prefix, bucket_name)
        )

    @classmethod
    def convert_path_in(cls, path: str, bucket_name) -> str:
        return path

    @classmethod
    def convert_path_out(cls, path: str, bucket_name) -> str:
        return path

    @classmethod
    def blob_to_file(cls, blob: Blob, bucket_name: str) -> Optional[File]:
        is_dir = blob.name.endswith("/")
        path = cls.convert_path_out(blob.name, bucket_name)
        path_segments = path.split("/")

        if is_dir:
            if len(path_segments) == 1:
                return None
            path_segments = path_segments[0:-1]

        name = path_segments[-1]
        path = "/".join(path_segments[0:-1])

        return File(
            id=blob.id,
            url=blob.path,
            size=sizeof_fmt(blob.size),
            dir=is_dir,
            path=path,
            name=name,
        )

    async def list_files(self, bucket_name: str, parent_path: str = "") -> List[File]:
        blobs = await self._list_blobs(bucket_name, parent_path)
        files: List[File] = []
        for blob in blobs:
            file = self.blob_to_file(blob, bucket_name)
            if file is not None:
                files.append(file)

        return files

    async def upload_string(
        self,
        string: Union[str, bytes],
        bucket_name: str,
        file_path: str,
        content_type="text/plain",
    ) -> File:

        blob = await self._get_blob(bucket_name, file_path)
        try:
            await force_async(blob.upload_from_string)(
                string, content_type=content_type
            )
        except GoogleCloudError as err:
            LOG.error(str(err))
            raise StorageError("Something went wrong uploading file {}", file_path)
        scidra_file = self.blob_to_file(blob, bucket_name)
        if scidra_file is None:
            raise StorageError("A file could not be created from the GCP blob")
        return scidra_file

    async def upload_file(
        self, file: UploadFile, bucket_name: str, parent_path: str = "",
    ) -> File:
        bucket = await self._get_bucket(bucket_name)
        path = self.convert_path_in(parent_path, bucket_name)
        if path != "":
            path += "/"

        blob = bucket.blob(path + file.filename)
        try:
            file.file.seek(0)
            await force_async(blob.upload_from_file)(file.file)
        except GoogleCloudError as err:
            LOG.error(str(err))
            raise StorageError(
                "Something went wrong uploadinf file {}", path + file.filename
            )
        scidra_file = self.blob_to_file(blob, bucket_name)
        if scidra_file is None:
            raise StorageError("A file could not be created from the GCP blob")
        return scidra_file

    async def get_file(self, bucket_name: str, file_path: str) -> Optional[BytesIO]:
        blob = await self._get_blob(bucket_name, file_path)
        if not blob.exists():
            return None

        byte_stream = BytesIO()
        blob.download_to_file(byte_stream)
        byte_stream.seek(0)
        return byte_stream

    async def file_exists(self, bucket_name: str, file_path: str) -> bool:
        blob = await self._get_blob(bucket_name, file_path)

        return blob.exists()

    async def folder_exists(self, bucket_name: str, path: str) -> bool:
        blobs = await self._list_blobs(bucket_name, path)
        for blob in blobs:
            return True

        return False

    async def _delete_blob(self, blob: Blob):
        await force_async(blob.delete)()

    async def delete_file(
        self, bucket_name: str, file_path: str, recursive: bool = False
    ) -> None:
        try:
            if recursive:
                blobs = await self._list_blobs(bucket_name, file_path)
                futures = [self._delete_blob(blob) for blob in blobs]
                await asyncio.wait(futures)
            else:
                blob = await self._get_blob(bucket_name, file_path)
                await self._delete_blob(blob)
        except NotFound:
            raise StorageError(
                f"Trying to delete a file {bucket_name}/{file_path} that doesn't exist."
            )


class FirebaseStorageClient(GoogleStorageClient):
    """
    Singleton client for interacting with FirebaseStorage. Note this is the same as the GoogleStorageClient
    except it uses a single bucket with folders
    Please don't use it directly, use `core.storage.utils.get_storage_client`.
    """

    __instance = None
    # gcp_storage: storage.Client = None
    bucket: storage.Bucket = None

    def __new__(cls) -> "FirebaseStorageClient":
        """
        Get called before the constructor __init__ and allows us to return a singleton instance.

        Returns:
            [FirebaseStorageClient] -- [Singleton Instance of client]
        """
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            app = get_current_app()
            cls.__instance.gcp_storage = app.gcp_storage  # type: ignore
            cls.__instance.bucket = app.gcp_storage.get_bucket(get_settings().BUCKET_NAME)  # type: ignore
        return cls.__instance

    @classmethod
    def convert_path_in(cls, path: str, bucket_name) -> str:
        if path.startswith("/"):
            path = path[1:]
        return get_settings().BUCKET_USER_FOLDER + bucket_name + "/" + path

    @classmethod
    def convert_path_out(cls, path: str, bucket_name) -> str:
        return path.replace(get_settings().BUCKET_USER_FOLDER + bucket_name + "/", "")

    # Override to return single bucket for all users
    async def _get_bucket(self, name: str) -> Bucket:
        return self.bucket

    async def make_bucket(self, name: str) -> None:
        blob = self.bucket.blob(get_settings().BUCKET_USER_FOLDER + name + "/")
        await force_async(blob.upload_from_string)(
            "", content_type="application/x-www-form-urlencoded;charset=UTF-8"
        )

    async def bucket_exists(self, name: str) -> bool:
        blob = self.bucket.blob(get_settings().BUCKET_USER_FOLDER + name + "/")
        return await force_async(blob.exists)()

    @staticmethod
    def log_error_not_found(blob):
        LOG.warning("Trying to delete file {} that doesn't exist", blob.name)

    async def delete_bucket(self, name: str):
        blobs = await force_async(self.bucket.list_blobs)(
            prefix=get_settings().BUCKET_USER_FOLDER + name + "/"
        )
        await force_async(self.bucket.delete_blobs)(
            blobs, on_error=self.log_error_not_found
        )
