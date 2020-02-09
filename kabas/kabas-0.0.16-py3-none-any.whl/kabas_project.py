from datetime import datetime, timedelta
import os
import shutil

from kabas._kabas_client import KabasClient
from kabas._kabas_cache import KabasCache
from kabas.kabas_file import KabasFile

class KabasProject:

    def __init__(self, project_id, project_name, access_type, project_key = None):

        self.project_name = project_name
        self.project_id = project_id
        self._project_key = project_key
        self.access_type = access_type

        self._client = KabasClient(project_key = project_key)
        
        self._open = True

    def __enter__(self):

        return self

    def get_files(self):

        project_detail = self._client.get_project(self.project_id)

        return project_detail.files

    def open_file(self, file_name, permissions, encoding = 'utf-8'):

        files = self.get_files()
        file_details = list(filter(lambda x : x.file_name == file_name, files))[0]

        return KabasFile(file_details, permissions, encoding, self._client)

    def download(self, file_name, target_directory):

        self._client.download_file(self.project_id, file_name, target_directory)

    def add_file(self, file_path):

        self._client.upload_file(self.project_id, file_path)

    def update_file(self, file_name, file_path):

        self._client.update_file(self.project_id, file_name, file_path)

    def display(self):

        project_header = "project {0}".format(self.project_name)
        separator = "-" * len(project_header)
        
        print(separator)
        print(project_header)
        print(separator)

        print("")

        files = self.get_files()
        for f in files:
            print(f)
            
        print("")

    def delete_file(self, file_name):

        self._client.delete_file(self.project_id, file_name)

    # def delete(self, skip_confirmation = False):

    #     if not skip_confirmation:

    #         entered_name = input("Are you sure you want to delete the current project? Please enter the project name to confirm")

    #         if (entered_name != self.project_name):

    #             print("Name was incorrect, project not deleted")
    #             return
                

    #     self._client.delete_project(self.project_id)
    #     print("Project {0} deleted".format(self.project_name))
    #     print("Closing connection")
    #     self.close()

    def close(self):

        if self._open:

            self._open = False
            self._client.close()

    def __exit__(self, exc_type, exc_value, traceback):

        self.close()