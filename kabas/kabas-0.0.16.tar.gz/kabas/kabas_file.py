import os

from kabas._kabas_cache import KabasCache

class KabasFile:

    def __init__(self, 
                file_details,
                file_permissions,
                file_encoding,
                client):

        self.project_id = file_details.project_id
        self.file_id = file_details.file_id
        self.file_name = file_details.file_name
        
        self._client = client

        self._file_permissions = file_permissions
        self._file_encoding = file_encoding
        self._location = self.download()
        self._f = open(self._location, self._file_permissions, encoding = file_encoding)
        self._seek = self._f.tell()

    def write(self, text):

        self._f.write(text)

    def read(self):

        return self._f.read()

    def download(self):

        return self._client.download_file(self.project_id, self.file_name)

    def update_remote_file(self):

        self._client.update_file(self.project_id, self.file_name)

    def __enter__(self):

        return self

    def close(self):

        closing_seek = self._f.tell()
        self._f.close()

        if closing_seek != self._seek:

            try:
                self.update_remote_file()

            except:            
                
                    f = open(self._location, self._file_permissions, encoding = self._file_encoding)
                    f.seek(self._seek, os.SEEK_SET)
                    f.truncate(self._seek)

    def __exit__(self, exc_type, exc_value, traceback):

        self.close()