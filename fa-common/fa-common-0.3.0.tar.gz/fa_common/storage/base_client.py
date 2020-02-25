import abc
from typing import List, Optional, Union
from .model import File
from fastapi import UploadFile
from io import BytesIO


class BaseClient(abc.ABC):
    @abc.abstractmethod
    async def make_bucket(self, name: str) -> None:
        pass

    @abc.abstractmethod
    async def bucket_exists(self, name: str) -> bool:
        pass

    @abc.abstractmethod
    async def delete_bucket(self, name: str):
        pass

    @abc.abstractmethod
    async def list_files(self, bucket_name: str, parent_path: str = "") -> List[File]:
        pass

    @abc.abstractmethod
    async def upload_file(
        self, file: UploadFile, bucket_name: str, parent_path: str = "",
    ) -> File:
        pass

    @abc.abstractmethod
    async def upload_string(
        self,
        string: Union[str, bytes],
        bucket_name: str,
        file_path: str,
        content_type="text/plain",
    ) -> File:
        pass

    @abc.abstractmethod
    async def get_file(self, bucket_name: str, file_path: str) -> Optional[BytesIO]:
        pass

    @abc.abstractmethod
    async def file_exists(self, bucket_name: str, file_path: str) -> bool:
        pass

    @abc.abstractmethod
    async def folder_exists(self, bucket_name: str, path: str) -> bool:
        pass

    @abc.abstractmethod
    async def delete_file(
        self, bucket_name: str, file_path: str, recursive: bool = False
    ) -> None:
        """
        Deletes a file or folder from the specified bucket

        Arguments:
            bucket_name {str} -- [description]
            file_path {str} -- [description]

        Keyword Arguments:
            recursive {bool} -- Deletes all child & folders files from a non empty folder (default: {False})

        """
        pass
