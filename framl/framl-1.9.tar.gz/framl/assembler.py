import os
import shutil
from typing import Pattern, Optional, Union
import zipfile
from google.cloud import storage
import tempfile
import yaml

class Assembler:

    def __init__(self, destination_path: str):
        self.work_directory: str = destination_path
        self.skeleton_path: str
        self.model_name: Union[str, None] = None

    def download_skeleton(self, bucket_name: str, name: str, tag: str) -> None:

        tmp_dir = tempfile.gettempdir()
        archive_name = f'{name}.{tag}.zip'

        storage_client = storage.Client(project='bbc-data-science')
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(archive_name)

        blob.download_to_filename(tmp_dir + '/' + archive_name)

        archive = zipfile.ZipFile(tmp_dir + '/' + archive_name)
        for file in archive.namelist():
            archive.extract(file, tmp_dir + '/framl-skeleton')

        self.skeleton_path = tmp_dir + '/framl-skeleton'

    def copy_base(self) -> None:
        if self.work_directory is None:
            raise Exception("destination path is not defined")

        for item in os.listdir(self.skeleton_path):
            s = os.path.join(self.skeleton_path, item)
            d = os.path.join(self.work_directory, item)
            if os.path.isdir(s):
                shutil.copytree(s, d)
            else:
                shutil.copy2(s, d)

    def add_file(self, content: str, destination_relative_path: str) -> None:
        pass

    @staticmethod
    def create_config(model_name: str, gcp_project_id: str, description: str, author: str, git_url: str) -> dict:
        model_config = {
            "name":               model_name,
            "gcp_project_id":     gcp_project_id,
            "author":             author,
            "description":        description,
            "git":                git_url,
            "version":            1,
            "flags_refresh_rate": 3600,
            "flags":              [

                "example_flag_1",
                "example_flag_2",

            ],
            "features":       {
                "example_user_id": {
                    "data_type": "integer",
                    "mandatory" : True,
                    "monitored": True
                },
                "example_profile_type": {
                    "data_type": "string",
                    "mandatory": True,
                    "monitored": False
                }
            },
            "model_output": {
                "example_score": {
                    "data_type": "float",
                    "monitored": True
                }
            }
        }

        return model_config

    def save_conf_fil(self, params: dict):
        with open(self.work_directory + '/config.yaml', 'w') as outfile:
            yaml.dump(params, outfile, default_flow_style=False, sort_keys=False)
