"""
Cryptographic functions for your tests. Here you can find hashing functions to check file contents.
"""
import hashlib


def hash_file(file_path: str) -> str:
    """ Hash file content with SHA-256.

    This way we can check two files have same content.

    :param file_path: Absolute path name.
    :return: File hash string.
    """
    content = ""
    with open(file_path, mode="rb") as file:
        content = file.read()
    content_hash = hashlib.sha256(content).hexdigest()
    return content_hash
