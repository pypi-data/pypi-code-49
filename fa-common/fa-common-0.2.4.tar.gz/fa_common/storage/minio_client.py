from minio import Minio, Object
from minio.error import BucketAlreadyExists, BucketAlreadyOwnedByYou, ResponseError
from typing import List, Optional
from fastapi import UploadFile
from .base_client import BaseClient
from fa_common import (
    force_async,
    get_current_app,
    logger as LOG,
    sizeof_fmt,
    StorageError,
)
from .model import File


class MinioClient(BaseClient):
    """
    Singleton client for interacting with Minio. Note we are wrapping all the call in threads to
    enable async support to a sync library.
    Please don't use it directly, use `core.storage.utils.get_storage_client`.
    """

    __instance = None
    minio: Minio = None

    def __new__(cls) -> "MinioClient":
        """
        Get called before the constructor __init__ and allows us to return a singleton instance.

        Returns:
            [MinioClient] -- [Singleton Instance of client]
        """
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            app = get_current_app()
            cls.__instance.minio = app.minio  # type: ignore
        return cls.__instance

    async def make_bucket(self, name: str) -> None:
        try:
            await force_async(self.minio.make_bucket)(name)
        except BucketAlreadyOwnedByYou:
            LOG.warning(f"Bucket {name} already owned by app")
        except BucketAlreadyExists:
            LOG.warning(f"Bucket {name} already exists")
        except ResponseError as err:
            LOG.error(f"Unable to create bucket {name}")
            LOG.error(err)
            raise err

    async def bucket_exists(self, name: str) -> bool:
        return await force_async(self.minio.bucket_exists)(name)

    async def delete_bucket(self, name: str):
        try:
            objects = await force_async(self.minio.list_objects_v2)(
                name, recursive=True
            )
            obj_list = []
            for obj in objects:
                LOG.info(obj)
                obj_list.append(obj.object_name)
            if len(obj_list) > 0:
                for del_err in self.minio.remove_objects(name, obj_list):
                    LOG.error(
                        f"Error while deleting objects in bucket {name}: {del_err}"
                    )
            return await force_async(self.minio.remove_bucket)(name)
        except ResponseError as err:
            LOG.error(f"Unable to delete bucket {name}")
            LOG.error(err)
            raise err

    @classmethod
    def object_to_file(
        cls, obj: Object, bucket_name: str, file_name: str = None
    ) -> Optional[File]:
        is_dir = obj.is_dir
        path = obj.object_name
        path_segments = path.split("/")

        if is_dir:
            if len(path_segments) == 1:
                return None
            path_segments = path_segments[0:-1]

        name = path_segments[-1]
        path = "/".join(path_segments[0:-1])

        LOG.debug("Converting Minio Object: {}", obj)

        return File(
            id=obj.object_name,
            url=obj.bucket_name + obj.object_name,
            size=sizeof_fmt(obj.size),
            dir=is_dir,
            path=path,
            name=name,
        )

    async def list_files(self, bucket_name: str, parent_path: str = "") -> List[File]:
        objects = await force_async(self.minio.list_objects_v2)(
            bucket_name, prefix=parent_path
        )
        files: List[File] = []
        for obj in objects:
            file = self.object_to_file(obj, bucket_name)
            if file is not None:
                files.append(file)
        return files

    async def upload_file(
        self, file: UploadFile, bucket_name: str, parent_path: str = "",
    ) -> File:

        if parent_path != "":
            parent_path += "/"
        try:
            # file.file.seek(0, 2)
            # filesize = file.file.tell()
            # file.file.seek(0)
            await force_async(self.minio.fput_object)(
                bucket_name, parent_path + file.filename, file.file.fileno()
            )

        except ResponseError as err:
            LOG.error(str(err))
            raise StorageError(
                "Something went wrong uploading file {}", parent_path + file.filename
            )
        obj = await force_async(self.minio.stat_object)(
            bucket_name, parent_path + file.filename
        )
        scidra_file = self.object_to_file(obj, bucket_name, parent_path + file.filename)
        if scidra_file is None:
            raise StorageError("A file could not be created from the Minio obj")
        return scidra_file
