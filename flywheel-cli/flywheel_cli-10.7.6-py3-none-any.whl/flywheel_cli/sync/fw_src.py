"""Module for sync source"""
import io
import json
import os
import re
import tempfile
import threading
import time
import zipfile

import dateutil
import requests

import flywheel

from .os_dst import OSDestination


class FWSource:
    """Generator yielding `read()`-able download targets for a ticket"""
    # pylint: disable=too-few-public-methods, too-many-arguments
    def __init__(self, client, project_id, include=None, exclude=None,
                 analyses=False, metadata=False, full_project=False,
                 strip_root=False, unpack=False):
        self.client = client
        self.strip_root = strip_root
        self.unpack = unpack

        payload = {'nodes': [{'level': 'project', '_id': project_id}]}
        filters = []
        if include:
            filters.append({'types': {'+': include}})
        if exclude:
            filters.append({'types': {'-': exclude}})
        if filters:
            payload['filters'] = filters
        params = {'type': 'full', 'prefix': ''}
        if analyses or full_project:
            params['analyses'] = True
        if metadata or full_project:
            params['metadata'] = True

        self.payload = payload
        self.params = params

    def __iter__(self):
        response = get_download_targets_response(self.client, self.payload, self.params)
        for item in response.iter_lines():
            target = json.loads(item)
            fwfile = FWFile(self.client, target, strip_root=self.strip_root)
            if self.unpack and fwfile.is_packed:
                # NOTE potential bottleneck when core uses cloud storage (zip seeks)
                for member in fwfile.members:
                    yield member
            else:
                yield fwfile


class FWFile:
    """Enable `read()`-ing download targets"""
    __slots__ = (
        'name', 'size', 'modified',
        'client', 'container_id', 'filename', 'file', 'bytes_read', 'is_packed',
        'unpack_lock', 'unpacked', '_members', '_tempdir'
    )

    def __init__(self, client, target, strip_root=False):
        strip = r'^/?[^/]+/' if strip_root else r'^/'
        self.name = re.sub(strip, '', target['dst_path'])
        self.size = target['size']
        self.modified = dateutil.parser.parse(target['modified']).timestamp()

        self.client = client
        self.container_id = target['container_id']
        self.filename = target['filename']
        self.file = None
        self.bytes_read = 0
        self.is_packed = (target['filetype'] == 'dicom' and
                          target['filename'].lower().endswith('.zip') and
                          target['download_type'] != 'metadata_sidecar')

        if target['download_type'] == 'metadata_sidecar':
            meta = json.dumps(target['metadata']).encode('utf8')
            self.size = len(meta)
            self.file = io.BytesIO(meta)

        if self.is_packed:
            self.unpack_lock = threading.Lock()
            self.unpacked = False
            self._members = None
            self._tempdir = None

    def read(self, size=-1):
        """Read `size` bytes from the download target GET response"""
        if self.file is None:
            response = get_container_file_response(self.client, self.container_id, self.filename)
            self.file = response.raw
        data = self.file.read(size)
        if not data:
            self.file.close()
        self.bytes_read += len(data)
        return data

    @property
    def members(self):
        """Return list of DICOM zip members"""
        if self._members is None:
            info = self.client.get_container_file_zip_info(self.container_id, self.filename)
            self._members = [FWMember(self, member) for member in info.members if member.size]
        return self._members

    @property
    def tempdir(self):
        """Return path to the downloaded and extracted DICOM zip"""
        with self.unpack_lock:
            if not self.unpacked:
                self._tempdir = tempfile.TemporaryDirectory()
                filename = os.path.basename(self.name)
                temp = OSDestination(self._tempdir.name).file(filename)
                temp.store(self)
                with zipfile.ZipFile(temp.filepath) as zf:
                    zf.extractall(self._tempdir.name)
                temp.delete()  # slices extracted - remove .zip
                self.unpacked = True
        return self._tempdir.name

    def cleanup(self):
        """Remove the temporary directory of extracted DICOM zip members"""
        if self.is_packed and self.unpacked:
            self._tempdir.cleanup()


class FWMember:
    """Enable `read()`-ing (DICOM) zip members from a locally unpacked FWFile"""
    # pylint: disable=too-few-public-methods
    __slots__ = ('name', 'size', 'modified', 'packfile', 'path', 'file', 'bytes_read')

    def __init__(self, packfile, member):
        # NOTE using member basenames instead of full paths (assumes unique names within zip)
        dirname = re.sub(r'(\.(dcm|dicom))?\.zip$', '/', packfile.name, flags=re.IGNORECASE)
        self.name = dirname + os.path.basename(member.path)
        self.size = member.size
        self.modified = packfile.modified

        self.packfile = packfile
        self.path = member.path
        self.file = None
        self.bytes_read = 0

    def read(self, size=-1):
        """Read `size` bytes from the locally unpacked DICOM zip member"""
        if self.file is None:
            filepath = f'{self.packfile.tempdir}/{self.path}'
            self.file = open(filepath, mode='rb')
        data = self.file.read(size)
        self.bytes_read += len(data)
        if not data:
            self.file.close()
        return data

    def cleanup(self):
        """Remove the locally unpacked DICOM slice"""
        if self.packfile.unpacked:
            os.remove(f'{self.packfile.tempdir}/{self.path}')


def retry(func):
    """Decorator for retrying temporary HTTP errors with exponential backoff"""
    def wrapped(*args, **kwargs):
        # pylint: disable=broad-except, no-member
        attempt = 0
        retries = 5
        while True:
            attempt += 1
            retriable = False
            try:
                return func(*args, **kwargs)
            except Exception as exc:
                if isinstance(exc, requests.ConnectionError):
                    # NOTE low-level network issues
                    retriable = True
                if isinstance(exc, requests.HTTPError):
                    # NOTE 429 for (future) google storage rate-limit error support
                    retriable = 500 <= exc.status_code < 600 or exc.status_code == 429
                if isinstance(exc, flywheel.ApiException):
                    # TODO retry functionality in SDK instead
                    retriable = 500 <= exc.status < 600
                if attempt > retries or not retriable:
                    raise
                time.sleep(2 ** attempt)
    return wrapped


@retry
def get_download_targets_response(client, payload, params):
    """Get download target response"""
    response = client.api_client.call_api(
        f'/download/targets', 'POST',
        auth_settings=['ApiKey'],
        query_params=list(params.items()),
        body=payload,
        _return_http_data_only=True,
        _preload_content=False
    )
    response.raise_for_status()
    return response


@retry
def get_container_file_response(client, container_id, filename):
    """Get container file response"""
    response = client.api_client.call_api(
        f'/containers/{container_id}/files/{filename}', 'GET',
        auth_settings=['ApiKey'],
        _return_http_data_only=True,
        _preload_content=False
    )
    response.raise_for_status()
    return response


@retry
def get_container_file_zip_info(client, container_id, filename):
    """Get container file zip info"""
    return client.get_container_file_zip_info(container_id, filename)
