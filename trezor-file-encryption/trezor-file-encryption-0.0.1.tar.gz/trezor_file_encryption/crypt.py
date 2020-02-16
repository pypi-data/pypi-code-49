from Crypto import Random
from Crypto.Cipher import AES

block_size = AES.block_size


def _pad(s):
    return s + ((block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)).encode()


def _unpad(s):
    return s[:-ord(s[len(s) - 1:])]


def encrypt_raw(key: bytes, b: bytes) -> bytes:
    iv = Random.new().read(block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(_pad(b))


def decrypt_raw(key: bytes, b: bytes) -> bytes:
    iv = b[:block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return _unpad(cipher.decrypt(b[block_size:]))
