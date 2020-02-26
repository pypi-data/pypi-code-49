import contextlib
import os
import shutil
from urllib.parse import urljoin, urlparse

from dli.client.aspects import analytics_decorator, logging_decorator
from dli.client.components.urls import consumption_urls
from dli.models import log_public_functions_calls_using, AttributesDict


@log_public_functions_calls_using(
    [analytics_decorator, logging_decorator],
    class_fields_to_log=['datafile_id', 'path']
)
class FileModel(AttributesDict):

    @contextlib.contextmanager
    def open(self):
        response = self._client.session.get(
            urljoin(
                self._client._environment.consumption,
                consumption_urls.consumption_download.format(
                    id=self.datafile_id,
                    path=self.path
                )
            ),
            stream=True
        )
        # otherwise you get raw secure
        response.raw.decode_content = True
        yield response.raw
        response.close()

    def download(self, to='./'):
        """
        Download one or more files and save them in the user specified
        directory.

        :return: The path to the directory where the files were written.
        """
        to = os.path.join(
            to, urlparse(self.path).path.lstrip('/')
        )
        print(f'Downloading to: {to}...')

        directory, _ = os.path.split(to)
        os.makedirs(directory, exist_ok=True)

        with self.open() as download_stream:
            with open(to, 'wb') as target_download:
                # copyfileobj is just a simple buffered
                # file copy function with some sane
                # defaults and optimisations.
                shutil.copyfileobj(
                    download_stream, target_download
                )
                print(f'Completed download to: {to}.')

        return to