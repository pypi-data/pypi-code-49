import os
import warnings
from google.cloud import storage
import gcsfs
import pandas as pd
from treebeard.helper import get_notebook_name, get_run_path

fs = gcsfs.GCSFileSystem(project="treebeard-259315")

storage_client = storage.Client()
bucket_name = 'treebeard-notebook-outputs'

warnings.filterwarnings(
    "ignore", "Your application has authenticated using end user credentials")


def list_files(bucket_name=bucket_name):
    fs.ls(bucket_name)


def save_to_cloud(input_file_name, save_name, bucket_name=bucket_name):
    save_location = os.path.join(
        bucket_name, get_run_path(), "artifacts", save_name)
    print(f"Treebeard saving {input_file_name} to {save_location}")
    fs.put(input_file_name, save_location)


def download(file_name, bucket_name=bucket_name):
    fs.get(f'{bucket_name}/{file_name}', f'{file_name}')


def read_csv(file_name, bucket_name=bucket_name):
    with fs.open(f'{bucket_name}/{file_name}') as f:
        return pd.read_csv(f)
