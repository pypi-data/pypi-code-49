import os
from typing import List, Tuple, Optional

from trezor_file_encryption.crypt import encrypt_raw, decrypt_raw

storage_dir = '.trezor_enc'


def get_storage_dir(where: str = None):
    if where is None:
        where = os.getcwd()

    return os.path.join(where, storage_dir)


def create_storage_dir(where: str = None):
    directory = get_storage_dir(where)
    exists = os.path.isdir(directory)

    if exists:
        return directory

    os.mkdir(directory, 0o700)
    return directory


def _iterate_over_files(directory: str) -> List[str]:
    files = []

    for filename in os.listdir(directory):
        if filename == storage_dir:  # Skip storage directory
            continue

        full_path = os.path.join(directory, filename)

        if os.path.isdir(full_path):
            files.extend(_iterate_over_files(full_path))
        else:
            files.append(full_path)

    return files


def get_all_files(where: str = None):
    if where is None:
        where = os.getcwd()

    return _iterate_over_files(where)


def encrypt_file(key: bytes, path: str) -> Tuple[bool, Optional[str]]:
    try:
        with open(path, 'rb+') as f:
            data = f.read()
            try:
                enc = encrypt_raw(key, data)
            except Exception as e:
                return False, str(e)
            else:
                f.seek(0)
                f.truncate()
                f.write(enc)
                return True, None
    except (IOError, OSError) as e:
        return False, str(e)


def decrypt_file(key: bytes, path: str) -> Tuple[bool, Optional[str]]:
    try:
        with open(path, 'rb+') as f:
            data = f.read()
            try:
                dec = decrypt_raw(key, data)
            except Exception as e:
                return False, str(e)
            else:
                f.seek(0)
                f.truncate()
                f.write(dec)
                return True, None
    except (IOError, OSError) as e:
        return False, str(e)
