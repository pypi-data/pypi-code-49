"""
Upload a file to DISCO, so it could later be used to run jobs.
"""
import io
import os
import pathlib
import requests
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from azure.storage.blob import BlobClient

from disco.core import create_progress_bar, constants
from disco.core.constants import ClusterType
from .base_controller import BaseController


class FileWrapper:
    """
    File Wrapper
    """

    def __init__(self, stream, length=0):
        self.stream = stream
        self.len = length
        self.content_type = None

    def read(self, size):
        """
        Args:
            size:
        """
        return self.stream.read(size)


class Asset(BaseController):
    """Provides functionality for uploading and downloading disco files"""

    def _request_url_for_upload(self, file_name, cluster_id=None):
        params = {'key': file_name}
        if cluster_id:
            params['clusterId'] = cluster_id
        return self.rest(url='/files/uploadparams',
                         data=params,
                         method='post'
                         )

    @classmethod
    def _upload_to_aws_with_callback(cls, url, file_name, form_fields, file_content_bytes, callback):
        """
        Upload file to AWS S3 with callback for monitoring the progress

        Args:
            url (str):
            file_name (str):
            form_fields (dict):
            file_content_bytes (bytes):
            callback (func):
        """
        form_fields = form_fields or {}
        encoder = MultipartEncoder({
            **form_fields,
            'file': (file_name, io.BytesIO(file_content_bytes)),
        })
        monitor = MultipartEncoderMonitor(encoder, callback)
        response = requests.request(
            'post',
            url,
            data=monitor,
            headers={'Content-Type': monitor.content_type}
        )
        response.raise_for_status()

    @classmethod
    def _upload_to_azure(cls, url, file_content_bytes):
        """
        Upload file to Azure with callback for monitoring the progress

        Args:
            url (str):
            file_content_bytes (bytes):
        """
        blob_client = BlobClient.from_blob_url(blob_url=url)
        blob_client.upload_blob(file_content_bytes)

    @classmethod
    def _upload_to_gcp_with_callback(cls, url, file_content_bytes, callback):
        """
        Upload file to GCP with callback for monitoring the progress

        Args:
            url (str):
            file_content_bytes (bytes):
            callback (func):
        """
        file_wrapper = FileWrapper(stream=io.BytesIO(file_content_bytes), length=len(file_content_bytes))
        monitor = MultipartEncoderMonitor(file_wrapper, callback)
        response = requests.request(
            'post',
            url,
            data=monitor,
        )
        response.raise_for_status()

    def _register(self, token):
        return self.rest(
            url='/files',
            data={'token': token},
            method='post')['id']

    def upload(self, file_name, file, cluster=None, show_progress_bar=True):
        """Upload a file to DISCO, so it could later be used to run jobs.

        Args:
            file_name (str):
            file: `file` can be either the file contents,
                in binary or string forms, a file
                object, or a Path` object that points to a file.
            cluster (ClusterDetails):
            show_progress_bar (bool):

        Returns:
            str: The id of the uploaded file.
        """
        if isinstance(file, bytes):
            file_content = file
        elif isinstance(file, str):
            file_content = file.encode()
        elif isinstance(file, pathlib.Path):
            file_content = file.read_bytes()
        elif hasattr(file, 'read'):
            file_content = file.read()
            if isinstance(file_content, bytes):
                pass
            elif isinstance(file_content, str):
                file_content = file_content.encode()
        else:
            file_content = pathlib.Path(str(file)).read_bytes()

        cluster_id = cluster.id if hasattr(cluster, 'id') else None
        cluster_type = cluster.type if hasattr(cluster, 'type') else None

        data = self._request_url_for_upload(file_name, cluster_id)
        bucket_upload_url = data['url']

        disable_progress_bar = os.environ.get(constants.ENV_VAR_DISABLE_PROGRESS_BAR) == '1' or (not show_progress_bar)

        if cluster_type == ClusterType.Azure.value:
            self._upload_to_azure(bucket_upload_url, file_content_bytes=file_content)
        else:
            with create_progress_bar(
                    total=len(file_content),
                    desc=f"Uploading {file_name}", unit='B',
                    ncols=80, disable=disable_progress_bar, unit_scale=True) as progress_bar:

                update_progress_bar_callback = self.__create_update_progress_bar_callback(progress_bar)

                if cluster_type == ClusterType.GCP.value:
                    self._upload_to_gcp_with_callback(bucket_upload_url,
                                                      file_content_bytes=file_content,
                                                      callback=update_progress_bar_callback)
                else:
                    self._upload_to_aws_with_callback(bucket_upload_url,
                                                      file_name,
                                                      form_fields=data['fields'],
                                                      file_content_bytes=file_content,
                                                      callback=update_progress_bar_callback)

        register_result = self._register(data['token'])
        return register_result

    @staticmethod
    def __create_update_progress_bar_callback(progress_bar):
        context = dict(bytes_read_so_far=0)

        def update_progress_bar_callback(monitor):
            new_bytes_read = monitor.bytes_read
            current_delta = new_bytes_read - context['bytes_read_so_far']
            context['bytes_read_so_far'] = new_bytes_read
            progress_bar.update(current_delta)

        return update_progress_bar_callback

    def input_files_from_bucket(self, bucket_paths, cluster_id):
        """
        Args:
            bucket_paths (list(str)):
            cluster_id (str):

        Raises:
            BucketPathsException: In case the bucket path is invalid or missing or has no files

        Returns:
            list - List of files ids registered from the given bucket paths
        """
        input_file_ids = self._request_register_files_from_bucket(bucket_paths, cluster_id)

        return input_file_ids

    def _request_register_files_from_bucket(self, bucket_paths, cluster_id):
        """
        Args:
            bucket_paths (list(str)):
        cluster_id (str):

        Returns:
            list - List of files ids registered from the given bucket paths
        """
        params = {'bucketPaths': bucket_paths, 'clusterId': cluster_id}
        registered_input_files = self.rest(url='/files/bucket', data=params, method='post')

        if registered_input_files is None:
            return []

        return [input_file.get('id') for input_file in registered_input_files]


def upload_file(file_name, file, cluster=None, show_progress_bar=True):
    """Legacy: Uploads file to DISCO, see `Assest.upload` for more info.

    Args:
        file_name (str):
        file: `file` can be either the file contents,
                in binary or string forms, a file
                object, or a Path` object that points to a file.
        cluster (ClusterDetails):
        show_progress_bar (bool):

    Returns:
        str: The id of the uploaded file.
    """
    return Asset().upload(file_name, file, cluster=cluster, show_progress_bar=show_progress_bar)


def input_files_from_bucket(bucket_paths, cluster_id):
    """
    Will scan the provided bucket paths for input files to be used in a job

    Args:
        bucket_paths (list(str)): List of paths in a bucket, can include wildcards
        cluster_id (str): A cluster id with a bucket to scan

    Raises:
        BucketPathsException: In case the bucket path is invalid or missing or has no files

    Returns:
        list - List of files ids registered from the given bucket paths
    """
    return Asset().input_files_from_bucket(bucket_paths, cluster_id)
