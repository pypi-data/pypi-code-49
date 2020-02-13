
import os
from pathlib import Path

def get_dir_root():
    return  Path(__file__).parent


def get_data_path():
    return  os.path.join(Path(__file__).parent, 'data')